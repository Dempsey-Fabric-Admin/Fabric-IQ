# Dempsey ChatGPT analytics plugins

This directory is the Git-managed marketplace root. Dempsey Fabric IQ 0.1.3 bundles the tenant's Fabric IQ app connection and six instruction skills for a fresh deployment:

| Skill | Responsibility |
| --- | --- |
| analytics-orchestrator | Source resolution, domain routing and cross-domain synthesis |
| analytics-visualization | PNG charts from retrieved and validated analytics results |
| finance-analytics | Microsoft Business Central Finance, including typical sales analytics |
| warehouse-operations-analytics | Manhattan SCALE inventory, replenishment, receiving/inbound, putaway and outbound picking |
| retail-operations-analytics | RMS-based Retail Operations facts and dimensions |
| fabriciq | Discovery, metadata, verified answers, value resolution and read-only DAX |

The assistant reads and follows these skills in one conversation. They are not separate hosted agents. Runtime tool definitions come from the connected MCP app.

The required connector is **Fabric IQ**, app ID `asdk_app_6ac7c2b7d71881c78074e8e10232776c`, configured in [`plugins/dempsey-fabric-iq/.app.json`](plugins/dempsey-fabric-iq/.app.json). Use this connection for every analytics operation, including discovery.

The confirmed canonical model is **Finance Analytics**. Warehouse Operations and
Retail Operations are planned; their skills must not query or substitute a model
until a canonical artifact name is configured and marked confirmed in
`references/analytics-routing.json`.

## First-question behavior

1. The user asks an analytics question.
2. Fabric IQ resolves the requested domain and checks whether its semantic model is configured.
3. It prioritizes suitable Production, then Test, then Development sources unless the user requests an environment.
4. It continues with the strongest unique artifact, or asks a focused question when material ambiguity remains.
5. Follow-ups retain the resolved source during this conversation. A source switch clears source-specific context. A new chat resolves the source again.

If the first question supplies a workspace or artifact URL, resolve it and continue when the source is unique; ask only if material ambiguity remains. Conceptual questions do not require source discovery.

Discovery is not an exhaustive workspace inventory. The current Fabric IQ tools cannot list all accessible workspaces or paginate a search. Present choices as "workspaces found through accessible content"; allow names/browser URLs for missing items. Do not interpret zero matches as proof of no access.

## Deployment and source control

Azure DevOps is the source of record. Maintain and develop the marketplace in a local clone, using the current local branch (`main` for this initial deployment).
The marketplace root is `src/chatgpt`; its local plugin entry points to `./plugins/dempsey-fabric-iq`.

For this fresh tenant deployment:
1. Use this local repository and its current branch as the deployment source.
2. Validate the marketplace using the command below.
3. Import the marketplace/plugin from the local source using the target host's supported import workflow.
4. Confirm Dempsey Fabric IQ 0.1.3 lists all six skills and requires the Fabric IQ app identified above. Configure installation policy and app availability for the intended roles. Members must authenticate and have Power BI access.
5. Run the acceptance scenarios in a fresh chat.
6. Commit the deployment source and push the branch to the Azure DevOps repository.

For subsequent updates:
1. Clone the Azure DevOps repository locally, or update an existing local clone, and check out the branch used for the deployment.
2. Make changes in the local repository, update both manifest versions together, and run validation.
3. Update the marketplace/plugin from that local repository through the host's supported update workflow, then run the acceptance scenarios.
4. Commit and push the same changes to Azure DevOps so the deployment source is available for the next update.

The local repository supplies deployment content; 
- Azure DevOps stores its version history. 
- A push to Azure DevOps does not by itself update an installed plugin. 
- OAuth secrets/tokens stay in app settings. Importing does not grant data access.

## Structure and extension

The plugin root has portable and native compatibility manifests. skills/ holds the six workflows and domain references. references/ holds source selection, session context and analytics-routing.json. common/ contains pinned Microsoft references. UPSTREAM.md records attribution and the local integration insertion.

To add another domain:
1. Add a named skill folder with matching frontmatter and focused measurement rules.
2. Add its entry and discovery terms to references/analytics-routing.json.
3. Add its routing branch to analytics-orchestrator and relevant handoff guidance.
4. Extend the acceptance scenarios, validate, and increment both manifest versions.
5. Update the marketplace from the local repository, run the new-chat smoke tests,    and commit/push the same changes to Azure DevOps.

analytics-routing.json is an instruction resource read by the assistant, not an executed routing service. Skill triggering and conversational source resolution require host verification; the plugin has no deterministic UI/authorization enforcement beyond the connected service's permissions.

## Validation and release

Run from the repository root:
`python3 src/chatgpt/scripts/validate_plugins.py`

Review [acceptance scenarios](tests/analytics-scenarios.md) and compare real answers with Power BI under the same user, filters, calendar, currency and period.
Static validation and simulated scenarios do not prove installed behavior.

Maintain all plugin files in the local Azure DevOps clone. Review the changes before updating the marketplace, and push every deployed change to Azure DevOps.

Read [upstream attribution](plugins/dempsey-fabric-iq/UPSTREAM.md) before updating Microsoft's source, and reapply the documented workspace/domain preflight.
