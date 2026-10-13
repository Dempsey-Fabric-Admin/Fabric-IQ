# Environment, workspace and artifact selection

## Connector scope

Use only the Fabric IQ app bound in [the app configuration](../.app.json) for
discovery, item resolution, metadata, value search and queries. Match the
connection by app identity, not a similar display or tool name. Never substitute
another connection when the configured app is unavailable or returns no matches.
If the host cannot access it, ask the user to connect it before making analytics
calls. Use the connected app's runtime tool definitions for tool names and arguments.

## Domain availability

Read [analytics routing](analytics-routing.json) before discovery. A domain with
`availability: confirmed` may be queried. A domain with `availability: planned`
must not trigger broad discovery or substitution until its canonical model has
been configured. Explain that its semantic model is not yet available.

Finance is currently confirmed through the `Finance Analytics` semantic model.
Warehouse Operations and Retail Operations are planned and have no configured
canonical model. A user-supplied URL or artifact ID does not silently change this
configuration; resolve it for identity, then ask whether the plugin configuration
should be updated before treating it as the domain source.

## Environment priority

Unless the user explicitly requests an environment, select the strongest suitable
source using this order:

1. Production: names without DEV, TST, TEST or other explicit non-production markers.
2. Test: names explicitly marked TST or TEST, when no suitable Production source exists.
3. Development: names explicitly marked DEV or DEVELOPMENT, only when neither
   Production nor Test has a suitable source.

Environment classification from names is a selection heuristic, not proof of the
deployment tier. Keep the returned workspace and artifact names visible. Honor an
explicit Production, TST/TEST or DEV request. Do not ask merely because a fallback
to Test or Development is required, but disclose the fallback prominently. Never
combine copies from different environments unless the user asks for that comparison.

## Resolve the source

For the first live analytics request in a conversation:

1. Preserve the original question as `pendingQuestion`.
2. Determine the domain and check its configured availability.
3. If the user supplied a Fabric/Power BI URL or unknown GUID, use
   ResolveFabricItem and retain its canonical identity.
4. Otherwise, discover the configured canonical artifact name first, followed by
   focused domain terms only when needed. Use artifact types `SemanticModel` and
   `Report` with at most 50 results per search.
5. Apply explicit environment scope or the default environment priority.
6. Select the strongest uniquely suitable artifact and continue without a separate
   confirmation prompt. If multiple candidates remain materially plausible, show
   their environment, workspace and artifact names and ask the smallest clarifying
   question. Even one workspace can contain multiple plausible artifacts.

For conceptual explanations without live data, skip discovery.

## Discovery limits

DiscoverArtifacts returns search matches, not an exhaustive workspace inventory.
The connection has no ListWorkspaces tool and no supported discovery pagination.
Never use an empty term, wildcard enumeration or workspace/item REST APIs.

Use only returned artifacts:

- Deduplicate by canonical artifact ID and type.
- Group workspaces by returned workspace ID when available. Identical names do
  not establish identical identities.
- Keep environment markers visible and retain source links.
- Treat a discovery hit as a candidate, not proof that it answers the question.
- Do not store discovery results, IDs, tokens or business data in Git or share
  them between users.

## Continue and switch

After source resolution, record environment, workspace, artifact and pending
question in conversational context, following [session context](session-context.md).
For a report, use GetReportMetadata to obtain its actual underlying semantic model;
never infer a model ID from its name. If a report binds to a model in another
workspace, retain that binding and its filters and disclose the distinction.

Reuse the resolved source for relevant follow-ups. On an explicit workspace,
artifact or environment switch, clear source-specific metadata, schema, values and
verified answers, then resolve again. A reply such as “2” refers to the latest
displayed candidates. Continue the pending question after resolution without
requiring the user to repeat it.

## Missing content and failures

No matches means no matching content was found, not that the user has no access.
Ask for a report/model name or browser URL. If the configured canonical Finance
model is not found, report that specifically and allow a focused search for Finance,
Income Statement or Balance Sheet; do not substitute an unrelated model.

Label partial results when a search fails. Do not turn authentication, throttling
or timeout errors into an empty inventory. On authentication failure, stop affected
calls and guide the user to reconnect. Retry a transient timeout once and respect
rate-limit backoff without blocking the conversation indefinitely.
