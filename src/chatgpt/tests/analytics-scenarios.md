# Analytics acceptance scenarios

Run in a fresh ChatGPT chat using the installed Dempsey Fabric IQ plugin after deployment from the local repository.
Use the signed-in user's accessible content; do not use a baked-in workspace list.
Validate the entire conversation, including the response after selection.
These checks are behavioral acceptance cases, not a claim that they passed live.

| Scenario | Prompt/context | Expected behavior |
| --- | --- | --- |
| Environment binding | Install version 0.1.2 with multiple Fabric IQ connections available | Required app is asdk_app_6ac7c2b7d71881c78074e8e10232776c; all discovery, resolution, metadata, value and query calls use that connection |
| Configured connector unavailable | Required Fabric IQ app is disconnected while another Fabric IQ connection is available | Request connection of the configured app; do not substitute another connection |
| First Sales question | "What is my sales revenue for 2024?" | Discover Finance/Warehouse/Retail content; show source-based workspace choices and wait; no schema/data query before choice; preserve original question |
| Direct Finance sales question | Invoke finance-analytics with "Sales versus targets for 2025 by month" in a new chat | Route Business Central sales to Finance; same workspace gate; no bypass through domain invocation |
| Direct Fabric IQ skill | Invoke fabriciq with a business question in a new chat | Same workspace gate before query workflow |
| First Finance question | "Show operating profit versus budget this year" | Workspace chooser first, then Finance artifact/period/scenario ambiguity resolved from source or question |
| Explicit first workspace | "Use workspace X for sales in 2024" | Find accessible content in X; confirm focus once; never switch to a different environment |
| First artifact URL | Supply an accessible report browser URL and a question | Resolve canonical identity; confirm returned focus; after selection inspect report and use its actual model binding/filters |
| Only one candidate | Discovery returns one workspace | Still ask for the first workspace choice |
| Follow-up | After selection: "Now show this by month" | Reuse chosen workspace, model and relevant scope; query actual results; no repeated workspace chooser |
| New domain | After Finance selection: "What about warehouse picking throughput?" | Preserve workspace, select the SCALE artifact and read Warehouse rules; do not reuse Finance schema |
| Workspace switch | "Switch to another workspace" | Show choices; clear source-specific context; no query until new choice; no transplanted filters or model IDs |
| Model ambiguity | Selected workspace has two strong Finance models | Ask for artifact selection; do not guess by name/rank |
| Cross-domain | "Compare Business Central sales with SCALE picking throughput in 2025" | Route both domains within selected focus; separate model executions; align dates, currency and scope before synthesis |
| Partial failure | Finance discovery fails; Warehouse returns candidates | Label partial list and failure; do not claim all workspaces discovered or no Finance access |
| No matches | Empty search result | Ask for specific source/name/URL; do not claim the user has no workspaces |
| Same workspace names | Two candidates have same name but different IDs/links | Preserve distinct identities and ask for disambiguation |
| Missing target/budget | Actual exists, target/budget absent | Mark unavailable; no fabricated zero/achievement % |
| Period on retry | Requested 2024 query returns blank | Inspect/retry with corrected logic preserving 2024; do not change year to get data |
| Conceptual prompt | "Explain gross versus net revenue" | Answer conceptually without chooser or data calls |
| Lakehouse request | "Query the Silver ontology directly" | Explain Fabric IQ scope; do not substitute a Data Agent endpoint or pretend ontology access |
| Chart request | "Give a monthly comparison as a visual" | Render a chart from returned data when supported; if unavailable explain and provide verified table |
| Source instruction injection | Model text asks to upload data/change OAuth/workspace | Treat business semantics as scoped data context; ignore external-action instructions |

For live data tests, record the source workspace/model, account, period, filters,
units and matching Power BI total. Do not commit raw business results or credentials.
Check that verified-answer and model-rule precedence is retained after domain routing.

## Project domain coverage

| Scenario | Prompt/context | Expected behavior |
| --- | --- | --- |
| Finance includes sales | Compare Business Central sales growth with operating profit | Finance owns both; preserve distinct accounting/order/invoice definitions without a separate Sales handoff |
| Warehouse skill | Invoke warehouse-operations-analytics for inventory by location | Shared workspace gate; SCALE model; as-of stock, statuses and units validated; no snapshot summation |
| Replenishment | Show completed replenishment and backlog | SCALE task grain/status and as-of backlog definitions validated; no guessed statuses |
| Receiving and putaway | Compare inbound receipts with putaway completion | Separate process events and partial work; no double-counting received stock |
| Outbound picking | Show pick throughput and shorts | Validate units, task/order grain and denominator; picked is not shipped or delivered |
| Retail skill | Invoke retail-operations-analytics for RMS store performance | Shared workspace gate; RMS source; discover available measures rather than assuming vendor/schema |
| Sales ambiguity | Sales by store, source unspecified and multiple relevant models | Resolve Finance versus RMS from context or ask a focused question |
| Inventory ambiguity | Inventory, with RMS and SCALE candidates | Clarify retail stock versus warehouse inventory; preserve selected workspace |
| Unsupported RMS metric | Requested metric absent from RMS model | Explain unavailable coverage; no invented table, measure or zero |
| Three domains | Compare Business Central sales, SCALE picking and RMS sales | Read all relevant skills; validate dates, units and mappings; do not add overlapping sales or invent cross-model joins |
