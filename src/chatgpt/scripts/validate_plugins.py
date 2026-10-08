#!/usr/bin/env python3
"""Validate the marketplace's local analytics plugin packages (stdlib only)."""
import json
import re
from pathlib import Path

MARKETPLACE_ROOT = Path(__file__).resolve().parents[1]


def contained(root, path):
    target = (root / path).resolve()
    if not target.is_relative_to(root.resolve()):
        raise ValueError(f"Path escapes package: {path}")
    return target


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def validate(plugin):
    portable = load_json(plugin / "plugin.json")
    native = load_json(plugin / ".codex-plugin/plugin.json")
    assert re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", portable["name"])
    assert plugin.name == portable["name"]
    assert re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+", portable["version"])
    assert not {"skills", "mcpServers", "apps", "interface"} & portable.keys()
    ext = portable["extensions"]["com.openai"]
    assert ext["apps"] == native["apps"] == "./.app.json"
    for key in ("name", "version", "description", "author"):
        assert native[key] == portable[key], f"Manifest mismatch: {key}"
    assert native["interface"] == ext["interface"]
    assert len(ext["interface"]["shortDescription"]) <= 30
    app = load_json(contained(plugin, ext["apps"]))
    assert app["apps"] and all(
        x["required"] is True and
        x["id"].startswith(("asdk_app_", "connector_", "templated_apps_"))
        for x in app["apps"].values()
    )
    assert not (plugin / "mcp.json").exists(), "Imported web plugin must reuse its app"

    skills = {}
    for doc in sorted((plugin / "skills").glob("*/SKILL.md")):
        body = doc.read_text(encoding="utf-8")
        front = re.match(r"^---\n(.*?)\n---(?:\n|$)", body, re.S)
        assert front, f"Missing frontmatter: {doc}"
        name = re.search(r"^name: ([a-z0-9-]+)$", front[1], re.M)
        desc = re.search(r'^description: "(.+)"$', front[1], re.M)
        assert name and desc and desc[1].strip(), f"Invalid skill metadata: {doc}"
        assert name[1] == doc.parent.name and name[1] not in skills
        skills[name[1]] = body
        assert len(body.splitlines()) < 500, f"Split long skill: {doc}"

    for doc in plugin.rglob("*.md"):
        body = doc.read_text(encoding="utf-8")
        for link in re.findall(r"\]\(([^)]+)\)", body):
            path = link.split("#", 1)[0]
            if not path or re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", path):
                continue
            target = (doc.parent / path).resolve()
            assert target.is_relative_to(plugin.resolve()), f"External local link: {doc}: {path}"
            assert target.is_file(), f"Broken link: {doc}: {path}"

    routing = load_json(plugin / "references/analytics-routing.json")
    selection = routing["workspaceSelection"]
    assert selection["mode"] == "discover-artifact-workspaces"
    assert selection["promptOnFirstAnalyticsRequest"] is True
    assert selection["scopeLifetime"] == "current-conversation"
    assert selection["exhaustive"] is False
    assert 1 <= selection["maxResultsPerSearch"] <= 50
    assert selection["initialSearchTerms"] and all(
        isinstance(term, str) and term.strip() and term != "*"
        for term in selection["initialSearchTerms"]
    )
    assert {"analytics-orchestrator", "finance-analytics", "warehouse-operations-analytics", "retail-operations-analytics", "fabriciq"} <= skills.keys()
    assert len({d["name"] for d in routing["domains"]}) == len(routing["domains"])
    expected_domains = {
        "finance": "Microsoft Business Central",
        "warehouse-operations": "Manhattan SCALE",
        "retail-operations": "RMS",
    }
    assert {d["name"]: d["sourceSystem"] for d in routing["domains"]} == expected_domains
    assert "sales-analytics" not in skills, "Sales belongs to Finance"
    for domain in routing["domains"]:
        assert domain["skill"] == domain["name"] + "-analytics"
        assert domain["discoveryTerms"] and domain["intents"]

    for route in [*routing["domains"], routing["fallback"]]:
        assert route["skill"] in skills
        target = (plugin / "references" / route["skillPath"]).resolve()
        assert target.is_relative_to(plugin.resolve()) and target.is_file()
        assert target == (plugin / "skills" / route["skill"] / "SKILL.md").resolve()
    for name in skills:
        assert "workspace-selection.md" in skills[name], f"Missing workspace gate link: {name}"
    print(f"Validated {portable['name']} {portable['version']}: {len(skills)} skills")


def main():
    marketplace = load_json(MARKETPLACE_ROOT / ".agents/plugins/marketplace.json")
    assert len({p["name"] for p in marketplace["plugins"]}) == len(marketplace["plugins"])
    for entry in marketplace["plugins"]:
        assert entry["source"]["source"] == "local"
        plugin = contained(MARKETPLACE_ROOT, entry["source"]["path"])
        assert load_json(plugin / "plugin.json")["name"] == entry["name"]
        validate(plugin)


if __name__ == "__main__":
    main()
