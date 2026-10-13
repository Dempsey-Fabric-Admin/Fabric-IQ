# Conversation scope

Keep the following as conversational working context, not a file, Git commit,
durable credential store or shared application state:

- pendingQuestion: the user's original analytics request.
- selectionStatus: unselected, resolving, awaiting-choice, selected or unavailable.
- environment: explicit or resolved Production, Test or Development classification.
- selectedWorkspaces: the resolved or explicitly selected focus; normally one workspace.
- workspaceIdentity: ID when returned, exact name and relevant canonical source
  links. Names alone are not stable unique identifiers.
- domain: Finance, Warehouse Operations, Retail Operations, a combination or general.
- domainArtifacts: per-domain report/model identity, type and source workspace.
- domainAvailability: confirmed or planned, from analytics-routing.json.
- reportContext: selected report/page/visual and applicable filters, if any.
- businessContext: period/calendar, company/entity, currency/unit, scenario and grain.
- retrievedContext: schema, model instructions and verified answers read in full.

The first analytics question moves unselected -> resolving. A unique suitable
source moves resolving -> selected. Material ambiguity moves resolving ->
awaiting-choice. An unconfigured domain moves resolving -> unavailable without
broad discovery. No metadata/value/data calls may run while awaiting-choice.

An explicit choice moves awaiting-choice -> selected. A new chat begins unselected.
Never treat personal memories or another user's model IDs as current authorization.
A resolved selection may be reused only within this conversation. A durable user
preference may be used as a discovery hint, but must be re-resolved and cannot act
as authorization. Missing context means rediscover/reselect, not guess.

A new domain preserves selectedWorkspaces but requires its own relevant artifact
selection, schema and business rules. Do not reuse a model across domains without validating its coverage, or transfer
a verified answer across models. Finance includes Business Central sales.
Record source-system context alongside domain identity when resolving ambiguity.

"Switch workspace", "switch artifact" or "switch environment" moves selected ->
resolving and clears source-specific context. "Refresh available sources" refreshes
discovery, retaining the old selection only until resolution completes and it
remains usable.
An explicit multi-workspace comparison records all choices and labels each result.

Follow-ups inherit only still-relevant business filters. Explicit new periods or
entities override the conflicting dimension, with report-filter overrides disclosed.

If host Memory is available, store only user-confirmed durable preferences such as
a preferred environment, workspace, model, reporting period or display format.
Confirm before replacing an established preference. Never store query results,
artifact discovery inventories, IDs, credentials or sensitive business data.
