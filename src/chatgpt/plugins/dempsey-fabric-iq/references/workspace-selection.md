# Workspace selection

## Connector scope

Use only the Fabric IQ app bound in [the app configuration](../.app.json)
for discovery, item resolution, metadata, value search and queries. Match the
connection by its app identity, not just a similar display name or tool name.
Never substitute another connection if the configured app is unavailable or
returns no matches.
If the host cannot identify or access the configured connection, ask the user to
connect it before making analytics calls. Use the connected app's runtime tool
definitions for actual tool names and arguments.

## When to prompt

On the first live analytics request in each new conversation, discover accessible
content and ask the user to choose the workspace focus BEFORE metadata, value
search or data queries. Even one candidate requires a choice. A workspace remembered
from another conversation is not a selection for this conversation.

If the first request explicitly names a workspace, find matching content and
present that workspace for confirmation. If it includes an artifact URL or unknown
GUID, use ResolveFabricItem first and present its returned identity/workspace for
confirmation. If resolution does not report a workspace, say it is unknown and ask
whether to focus on that resolved artifact; do not invent a workspace or inspect
its schema merely to bypass the selection gate. Never reinterpret the request as permission to pick another workspace.

Once selected, reuse the focus for follow-ups. Reopen the chooser only on an
explicit switch, a request for another workspace, or loss of usable source context.
A new domain in the same workspace does not require reselection.

For conceptual explanations without live data, skip the chooser.

## Discover choices

Read analytics-routing.json. For an unscoped first analytics request, call
DiscoverArtifacts for each initialSearchTerms entry, with artifactTypes
["SemanticModel", "Report"] and maxResults 50. These are valid non-empty searches.
The searches are independent and may run in parallel.

These are search results, NOT a workspace inventory. The Fabric IQ connection
has no ListWorkspaces tool, and searches may return broad or approximate matches.
Never use an empty search term, wildcard enumeration or workspace/item REST APIs
with this connection. Do not claim the list includes every workspace the user can access.

Use actual returned artifacts only:
- Deduplicate artifacts by canonical artifact ID and type.
- Group workspaces by returned workspace ID when available. If only names are
  known, group for display but retain distinct artifact IDs and links; identical
  names are not proof that workspace identities are identical.
- Keep DEV, TST, OLD and other labels visible. Never prefer a previous user's
  workspace or silently substitute a production/test copy.
- Show matching artifact names/types per workspace as examples, with source links
  where returned. A discovery hit is a candidate, not proof it answers the question.
- Keep every discovered workspace available for selection. If the list is large,
  paginate the display and explicitly offer the remaining choices and search.
- Do not store this user's discovery results, identities, tokens or business data
  in Git or share a candidate list between users.

Suggested first reply:
"I found these workspaces through Sales and Finance content accessible with your
connected account. Which workspace should I use for this chat?"
Follow with a numbered table: Workspace | Example reports/models.
Then: "This is a search-based list and may be incomplete. You can also give me a
workspace or report/model name, or paste its browser URL."

Do not use a fixed two/three-option menu that hides remaining real choices.
A plain numbered table and a direct question are sufficient.

## Resume the pending request

After the user chooses:
1. Record the selected workspace and pending question in current conversation
   context, following session-context.md.
2. Filter candidate artifacts locally to the chosen workspace; DiscoverArtifacts
   currently has no workspaceId filter. If more discovery is needed, use a
   specific domain/artifact search term then filter its returned candidates.
3. A reply like "2" refers to the latest shown choices. If multiple same-name
   identities remain, disambiguate using the returned source links/artifacts;
   do not assume they are one workspace.
4. For workspace-name selection, choose an artifact only when uniquely relevant.
   If several strong models/reports remain, ask the user to select one.
5. Resolve canonical IDs where needed. For a report, use GetReportMetadata to find
   its actual underlying semantic model; never infer the model ID from its name.
6. If the chosen report binds to a model in another workspace, retain the report
   binding and its filters; disclose the source distinction. Do not replace the
   model with a same-name model in the report's workspace.
7. Confirm the focus briefly and continue the original question without requiring
   the user to retype it. If another ambiguity blocks a correct query, ask that
   focused question.

## Missing content and failures

No matches: say no matching content was found, not that the user has no workspaces.
Ask for a report/model name, browser URL or workspace plus domain. For Finance,
a bounded follow-up search for Income Statement or Balance Sheet can help.
Use the fallback domain discovery terms only when needed; avoid repeated broad scans.

Unlisted workspace: search the supplied artifact/workspace/domain terms, show the
returned candidates and confirm. A failed search is not an access-denied verdict.

Truncation/50-result limit: disclose that results may be incomplete and ask for a
narrower name or URL; there is no supported discovery pagination argument.

Partial discovery failure: label the successful choices as partial and disclose
the failed search. Do not interpret authentication, throttling or timeout errors
as an empty inventory. On an authentication failure, stop affected calls and guide
the user to reconnect. On a transient timeout, retry once; respect rate-limit
backoff instructions without blocking the conversation indefinitely.

Workspace switch: invalidate report/model/schema/value/verified-answer context
from the old focus and rediscover or resolve within the new scope. The business
question can be retained, but source identity and filters cannot be transplanted.

Unavailable selected artifact: explain the failure and ask for another accessible
artifact in the selected workspace. Never silently switch workspaces.
