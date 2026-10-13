---
name: analytics-visualization
description: "Create a polished PNG chart from verified business-analytics query results when the user requests a visual or graphical context materially improves a trend, comparison, composition, ranking or variance. Use after retrieval and validation; do not use for a single KPI or sparse or ambiguous data."
---

# Analytics Visualization

Turn verified analytics results into a clear chart and include it with the data
answer in the same response.

## Resources and trigger

Read [workspace selection](../../references/workspace-selection.md) and
[session context](../../references/session-context.md) so the chart retains the
resolved source and environment. Use this skill after Fabric IQ retrieval when:

- The user asks for a chart, graph, visualization or visual comparison.
- A time series, category comparison, composition, ranking or variance is
  substantially easier to understand visually.

Do not force a chart for a single KPI, a tiny result with no useful comparison,
unresolved units or categories, or data that would be misleading when plotted.
If an explicitly requested chart cannot be supported, explain the data limitation
instead of fabricating or padding values.

## Workflow

1. Complete Fabric IQ retrieval and validation first. Chart only returned values.
2. Preserve environment, workspace, model/report, period, filters, units and
   currency from the analytics answer.
3. Choose one primary chart:
   - Time series: line chart; use grouped bars when discrete periods or a few
     short series are clearer.
   - Category comparison: vertical bars.
   - Variance or bridge: waterfall only when components genuinely reconcile;
     otherwise grouped bars.
   - Composition: donut or pie only for a small set of mutually exclusive parts
     of one whole; otherwise bars.
   - Ranking: horizontal bars ordered by value.
4. Use an available runtime plotting capability to create a PNG. Do not return
   ASCII art, chart-spec JSON or plotting code as the requested visualization.
5. Keep transformations auditable. Do not silently aggregate, interpolate,
   normalize, convert currencies, combine domains or remove outliers. State any
   necessary transformation.
6. Present the written answer and compact table before the chart when both are
   useful, and surface the PNG in the same response. If the host cannot render or
   attach a PNG, provide the verified table and state that limitation plainly.

## Chart standards

Every chart must have:

- A descriptive title naming the metric and scope
- Labeled axes with units where applicable
- A legend when more than one series is present
- Readable labels without excessive clutter
- Professional, high-contrast colors and a clean background
- Appropriate currency, percentage and thousands formatting
- Source context in accompanying text rather than an unreadable block in the image

Do not use 3D effects, decorative gradients, misleading truncated axes or more
series than remain legible. Start quantitative bar axes at zero unless a clearly
disclosed analytical reason requires otherwise.

## Output contract

- 1-4 KPIs: bold values with short commentary; no chart unless comparison or
  trend context exists.
- Larger datasets: compact table, brief narrative and one clarifying chart.
- Trends: narrative, compact table and line or grouped-bar chart.
- Comparisons: valid absolute and percentage variance plus grouped bars or a
  justified waterfall.
- Recommendations: short paragraphs with actions tied to verified findings.
- Drill-downs: structured hierarchy with a chart at the level that best answers
  the question.

Always retain traceability: environment, workspace, model/report, reporting period,
material filters, units and currency. For cross-domain visuals, label every source
and never imply separately queried models were joined unless alignment is explicit
and valid.
