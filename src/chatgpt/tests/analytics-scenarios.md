# Analytics acceptance scenarios

Run in a fresh ChatGPT chat using the installed Dempsey Fabric IQ plugin after deployment from the local repository.
Use the signed-in user's accessible content; do not use a baked-in workspace list.
Validate the entire conversation, including the response after selection.
These checks are behavioral acceptance cases, not a claim that they passed live.

| Scenario | Prompt/context | Expected behavior |
| --- | --- | --- |
| Environment binding | Install version 0.1.0 with multiple Fabric IQ connections available | Required app is asdk_app_6abf329a7fcc81c79808365fa0e19cb9; all discovery, resolution, metadata, value and query calls use that connection |
| Configured connector unavailable | Required Fabric IQ app is disconnected while another Fabric IQ connection is available | Request connection of the configured app; do not substitute another connection |
| First Sales question | "What is my sales revenue for 2024?" | Discover Sales/Finance content; show source-based workspace choices and wait; no schema/data query before choice; preserve original question |
| Direct Sales skill | Invoke sales-analytics with "Sales versus targets for 2025 by month" in a new chat | Same workspace gate; no bypass through domain invocation |
| Direct Fabric IQ skill | Invoke fabriciq with a business question in a new chat | Same workspace gate before query workflow |
| First Finance question | "Show operating profit versus budget this year" | Workspace chooser first, then Finance artifact/period/scenario ambiguity resolved from source or question |
| Explicit first workspace | "Use workspace X for sales in 2024" | Find accessible content in X; confirm focus once; never switch to a different environment |
| First artifact URL | Supply an accessible report browser URL and a question | Resolve canonical identity; confirm returned focus; after selection inspect report and use its actual model binding/filters |
| Only one candidate | Discovery returns one workspace | Still ask for the first workspace choice |
| Follow-up | After selection: "Now show this by month" | Reuse chosen workspace, model and relevant scope; query actual results; no repeated workspace chooser |
| New domain | After Sales selection: "What about operating expenses?" | Preserve workspace, select Finance artifact and read Finance/source rules; do not reuse Sales schema |
| Workspace switch | "Switch to another workspace" | Show choices; clear source-specific context; no query until new choice; no transplanted filters or model IDs |
| Model ambiguity | Selected workspace has two strong Sales models | Ask for artifact selection; do not guess by name/rank |
| Cross-domain | "Compare sales growth with operating profit in 2025" | Route both domains within selected focus; separate model executions; align dates, currency and scope before synthesis |
| Partial failure | Finance discovery fails; Sales returns candidates | Label partial list and failure; do not claim all workspaces discovered or no Finance access |
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
