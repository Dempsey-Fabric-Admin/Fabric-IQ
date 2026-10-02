# Microsoft Fabric IQ upstream source

Source: https://github.com/microsoft/skills-for-fabric
Pinned commit: 6c11ad58c25992e5d1435ce7cd80d217d5598a31
Retrieved: 2026-09-30
License: MIT; the upstream license is preserved in LICENSE.

The following files are copied without content changes:
- common/COMMON-CORE.md
- common/COMMON-CLI.md
- common/ITEM-DEFINITIONS-CORE.md
- LICENSE

The common directory preserves the skill's relative reference links.
The upstream APM descriptor is omitted because this plugin does not use APM.
Plugin manifests and the app binding configure the Dempsey deployment.
The Fabric IQ MCP server supplies the tools; this repository does not implement them.
Other skills mentioned upstream, including semantic-model-authoring, are not bundled.
COMMON-CLI is supporting reference material; Azure CLI is not required for the connected ChatGPT Fabric IQ workflow.

To update, select a new upstream commit, copy the same files, update this attribution, increment both manifest versions, and review the diff before updating the marketplace from the local repository.

## Dempsey integration in version 0.1.0

skills/fabriciq/SKILL.md retains the pinned upstream body with one added "Dempsey integration preflight" section immediately before Workflow. This adds conversation workspace selection, domain routing and explicit-scope preservation.
Its relative links point to the bundled skills and shared references.
Reapply this insertion deliberately when updating the upstream skill; do not silently overwrite the integration gate.

analytics-orchestrator, sales-analytics and finance-analytics and their references are workflow additions adapted from the original Fluid integration. Their generic business rules must be checked against each selected model's actual definitions. No hidden Fabric Data Agent instructions or fixed workspace/model assignments have been imported.
