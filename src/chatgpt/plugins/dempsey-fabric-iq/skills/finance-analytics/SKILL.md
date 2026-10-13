---
name: finance-analytics
description: "Analyze live Finance questions using Power BI reports/models based on Microsoft Business Central. Scope includes financial statements, sales revenue, sales orders, customers, returns, sales targets, profit, expenses, budget, receivables, payables, cash flow. Apply shared source resolution first; resolve source-system ambiguity before selecting a model."
---

# Finance analytics

Finance facts and dimensions derived from Microsoft Business Central finance-related tables, including typical sales analytics: sales, orders, customers, products, returns and targets alongside statements, profit, budget and balances.

## Resources

- Read [workspace selection](../../references/workspace-selection.md) and
  [session context](../../references/session-context.md) first.
- Read [measurement rules](references/measurement-rules.md) before interpreting metrics.
- Read [Fabric IQ](../fabriciq/SKILL.md) in full before metadata or query work.
- Use [orchestration](../analytics-orchestrator/SKILL.md) for unresolved routing or
  questions spanning domains. If already routed here, proceed without restarting it.

## Workflow

1. Resolve the source through the shared environment/workspace/artifact workflow
   and preserve the pending question.
2. Prefer the confirmed canonical semantic model `Finance Analytics`. Honor an
   explicit report/model request. Otherwise discover that exact name first and
   apply the configured Production -> Test -> Development priority. Use broader
   Finance routing terms only when the canonical search misses. Ask only when
   multiple candidates remain materially plausible, and validate source relevance
   from returned metadata.
3. Read report metadata for report-based requests and the full semantic model
   schema, CustomInstructions and verified answers. Retrieve missing context if truncated.
4. Prefer matched verified answers and published measures. Inspect actual facts,
   dimensions, relationships, keys, grain and date roles; source-system names do not
   establish a physical schema or prove every source table is present in the model.
5. Establish period, entity/site, units, currency and relevant process/status scope
   from source definitions. Resolve named filters with ValueSearch. Ask only about
   unresolved choices that materially change the answer.
6. Query compact aggregates through Fabric IQ. For rankings with no requested size,
   use top 10 and disclose that limit; period breakdowns include all requested periods.
7. Check totals, grain, date coverage and missing data. Preserve explicit scope on
   retries. Missing measures, targets or unsupported processes are unavailable, not zero.
8. Answer with verified results, source links, period, units and relevant filters.
   Render requested visuals when supported. Distinguish observed contributions from
   hypotheses; metadata alone does not establish business performance.

## Domain boundaries

Finance includes Business Central sales analytics. Warehouse Operations owns
Manhattan SCALE inventory, replenishment, receiving, putaway and picking. Retail
Operations owns RMS-based analytics. Route by the requested process and source,
not a shared word such as sales or inventory. Clarify when source context does not
resolve ambiguity. For combined questions, retain the workspace and use orchestration.

Use read-only Fabric IQ access to supported reports/semantic models. Do not query
source-system databases directly, change operational records, invoke Data Agents,
or invent missing tables, KPIs or source-system mappings.

For sales questions, also read [sales measurement rules](references/sales-measurement-rules.md). Sales is part of Finance, not a separate domain.
