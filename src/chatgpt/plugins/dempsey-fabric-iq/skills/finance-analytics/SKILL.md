---
name: finance-analytics
description: "Analyze live financial statements, accounting revenue, profit, expenses, actual versus budget, assets, liabilities, cash flow and receivables/payables using accessible Power BI models/reports. Use for Finance business questions; apply the shared workspace gate first. Route sales orders, sales targets and delivery questions to Sales."
---

# Finance analytics

## Resources

- Read [workspace selection](../../references/workspace-selection.md) and
  [session context](../../references/session-context.md) first.
- Read [Finance measurement rules](references/measurement-rules.md) for financial
  signs, period, budget, balance and currency interpretation.
- Read [Fabric IQ](../fabriciq/SKILL.md) in full before metadata/query work.
- Use [orchestration](../analytics-orchestrator/SKILL.md) when routing is unresolved
  or both domains are needed. If already routed here, proceed without restarting it.

## Workflow

1. Pass the shared workspace gate; preserve the pending question when prompting.
2. Discover/resolve a relevant Finance report/model in the selected workspace.
   Income Statement and Balance Sheet are useful additional search terms if
   "Finance" misses report names. Do not assume such a report exists.
   Confirm multiple strong candidates; honor explicit model/report requests.
3. Read report metadata for report-based questions and the full model schema.
   Retrieve all verified answers and CustomInstructions if truncated.
4. Match verified answers and use model-defined financial measures and report
   account hierarchies. Apply the measurement rules only where source definitions
   leave the semantics open.
5. Establish company/entity, calendar/fiscal period, reporting currency, unit,
   scenario/version and consolidation basis from source context. Ask only for
   unresolved choices that materially alter the result. Resolve named accounts,
   entities, categories and scenario values with ValueSearch.
6. Query focused statement/variance/ratio results using Fabric IQ. A claim about
   financial performance requires returned data, not metadata alone.
7. Check signs, aggregation, budget availability, as-of dates and period coverage.
   Preserve explicit period/entity filters on retries. A missing KPI or failed
   query is unavailable data, not zero.
8. Return one clear financial answer with source workspace/report/model links,
   dates, currency, scaling and scenario. Explain favorable/unfavorable variance
   only when source semantics establish the direction. Render requested visuals
   from verified results; never fabricate a statement line or ratio.

## Handoff

Sales order/customer/product/target/delivery analysis belongs to
[Sales](../sales-analytics/SKILL.md). For questions requiring both Sales and Finance,
use orchestration and reconcile definitions before comparing sources.

Do not call a Fabric Finance Data Agent endpoint or invent its unpublished
instructions. This skill works against supported reports/semantic models through
Fabric IQ; it does not supply financial posting, Lakehouse/ontology querying or
investment/tax/legal advice.
