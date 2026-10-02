---
name: sales-analytics
description: "Analyze live sales revenue, orders, customers, products, returns, delivery performance, sales growth and sales versus targets in accessible Power BI models/reports. Use for Sales business questions; apply the shared workspace gate first. Route financial statements, accounting profit and budget questions to Finance."
---

# Sales analytics

## Resources

- Read [workspace selection](../../references/workspace-selection.md) and
  [session context](../../references/session-context.md) first.
- Read [Sales measurement rules](references/measurement-rules.md) for metric,
  target, order, date and delivery interpretation.
- Read [Fabric IQ](../fabriciq/SKILL.md) in full before metadata/query work.
- Use [orchestration](../analytics-orchestrator/SKILL.md) only when routing is
  unresolved or both domains are needed. If already routed here, continue
  directly; do not restart orchestration or the chooser.

## Workflow

1. Pass the shared workspace gate. Preserve the original question when prompting.
2. Find the selected workspace's relevant Sales report/model. Use discovery/resolve,
   not a hardcoded tenant, workspace or artifact ID. Confirm multiple strong candidates.
   An explicit model request takes precedence over report preference.
3. Read report metadata when report-based, then the full semantic model schema.
   Retrieve complete verified answers and CustomInstructions if truncated.
4. Match verified answers before composing a custom query. Apply authoritative
   model/report measures, filters and definitions; use the measurement rules only
   where the selected source does not define different business semantics.
5. Confirm material metric/calendar/currency ambiguity. Do not block on questions
   the selected source already answers. Resolve named customers/products/regions
   with ValueSearch before filtering.
6. Query compact aggregates. For a ranking without an explicit size, return top 10
   and state the scope. For monthly comparisons, return every requested month
   rather than taking the top 10 months. Use source-defined measures.
7. Validate totals, date coverage, targets, units and missing data. Preserve the
   requested period on retries; do not switch years to produce a nonblank number.
8. Lead with the business finding, then a compact table or requested rendered
   visual. Identify workspace/report/model and period; link the returned source.
   Explain applied filters and limits briefly. Avoid internal IDs and query jargon.

## Handoff

Accounting revenue, financial statements, profit/expense/budget analysis belongs
to [Finance](../finance-analytics/SKILL.md). If "revenue" is ambiguous between
invoiced sales, orders and ledger revenue, use source context or ask a focused
clarification. For a genuinely combined question, use orchestration while keeping
the selected workspace context.

Do not call a Fabric Sales Data Agent endpoint. These instructions coordinate
Fabric IQ against the selected semantic model; they do not reproduce a hosted
Data Agent's Lakehouse sources, ontology bindings or hidden agent settings.
