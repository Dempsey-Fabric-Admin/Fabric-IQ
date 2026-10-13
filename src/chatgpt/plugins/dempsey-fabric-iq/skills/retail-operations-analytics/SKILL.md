---
name: retail-operations-analytics
description: "Handle Retail Operations questions for RMS. The domain is planned and must not be queried until a canonical semantic model is configured; once available, scope can include store sales, returns, inventory and other modeled retail processes."
---

# Retail Operations analytics

Retail Operations facts and dimensions derived from RMS tables. Determine the available retail processes and metrics from the selected model; do not assume a particular RMS vendor, version or table layout.

## Current availability

Retail Operations is planned, but no canonical semantic model is configured.
Explain that retail analytics is not yet available and do not discover or
substitute unrelated models. A model becomes usable only after its canonical name
and `availability: confirmed` are set in analytics-routing.json.

## Resources

- Read [workspace selection](../../references/workspace-selection.md) and
  [session context](../../references/session-context.md) first.
- Read [measurement rules](references/measurement-rules.md) before interpreting metrics.
- Read [Fabric IQ](../fabriciq/SKILL.md) in full before metadata or query work.
- Use [orchestration](../analytics-orchestrator/SKILL.md) for unresolved routing or
  questions spanning domains. If already routed here, proceed without restarting it.

## Workflow

1. Check domain availability in analytics-routing.json. While it is `planned`,
   preserve the pending question, explain the limitation and stop before discovery.
2. Once configured, resolve the source through the shared environment/workspace/
   artifact workflow, then discover or resolve the relevant Retail Operations model.
   Use [routing terms](../../references/analytics-routing.json) as search hints,
   not guaranteed artifact names. Confirm multiple strong candidates and honor
   explicit report/model requests. Validate source relevance from available metadata.
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
