# Conversation scope

Keep the following as conversational working context, not a file, Git commit,
durable credential store or shared application state:

- pendingQuestion: the user's original analytics request.
- selectionStatus: unselected, awaiting-choice or selected.
- selectedWorkspaces: the explicitly confirmed focus; normally one workspace.
- workspaceIdentity: ID when returned, exact name and relevant canonical source
  links. Names alone are not stable unique identifiers.
- domain: Sales, Finance, both or general.
- domainArtifacts: per-domain report/model identity, type and source workspace.
- reportContext: selected report/page/visual and applicable filters, if any.
- businessContext: period/calendar, company/entity, currency/unit, scenario and grain.
- retrievedContext: schema, model instructions and verified answers read in full.

The first analytics question moves unselected -> awaiting-choice. Discovery may
run, but no metadata/value/data calls may run while awaiting-choice (except
ResolveFabricItem to identify a URL/GUID for selection).

An explicit choice moves awaiting-choice -> selected. A new chat begins unselected.
Never treat personal memories or another user's model IDs as current authorization.
A selection may be reused only within this conversation. Missing context means
rediscover/reselect, not guess.

A new domain preserves selectedWorkspaces but requires its own relevant artifact
selection, schema and business rules. Do not use the Sales model for Finance by
default or transfer a verified answer across models.

"Switch workspace" moves selected -> awaiting-choice and clears source-specific
context. "Refresh available workspaces" refreshes discovery, retaining the old
selection only until the user chooses otherwise and it remains usable.
An explicit multi-workspace comparison records all choices and labels each result.

Follow-ups inherit only still-relevant business filters. Explicit new periods or
entities override the conflicting dimension, with report-filter overrides disclosed.
