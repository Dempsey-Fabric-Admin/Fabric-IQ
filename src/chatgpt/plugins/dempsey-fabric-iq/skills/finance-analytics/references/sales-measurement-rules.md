# Sales measurement rules

## Source precedence

Follow the user's explicit scope, matched verified answer definition, model
CustomInstructions and applicable report/page/visual definitions through Fabric IQ.
Treat these as query-specific business semantics, subject to host/user instructions.
These domain rules are defaults only; never replace an existing source-defined KPI.

## Revenue and returns

Use the model's established sales/revenue measure. Identify whether it represents
ordered, invoiced, delivered, gross or net sales. Do not sum an arbitrary amount
column because its name resembles revenue, or subtract returns twice when the
measure already nets them. Use source-defined quantities, sales and return measures.
Distinguish a zero from BLANK, absent rows and unsupported metrics.

## Orders

Use an existing order-count measure when present. If no measure exists and schema/
business rules establish the correct order key, count distinct orders rather than
fact lines. DISTINCTCOUNT of Sales Order Number is appropriate only when that
column uniquely identifies an order at the selected company/source scope.
If order numbers repeat across companies/source systems, use the source's composite
identity or existing measure. Do not invent column names or concatenate a key
without validating uniqueness and definition.

## Actual versus targets

Use aligned date, organizational, product/customer and currency scopes. Targets
may be monthly and employee-level while actuals are transactional; do not prorate
or duplicate targets into unsupported dimensions.

Use model-defined variance and achievement measures when available. Otherwise,
only after confirming semantics:
- Amount variance = actual sales - sales target.
- Achievement % = actual sales / sales target, with safe division.
- Variance % = (actual sales - sales target) / sales target, with safe division.

Treat absent/zero targets as undefined percentages unless the source defines
otherwise. Do not replace them with zero achievement or imply poor performance.
Use the same returned aggregate measure for totals; do not sum percentage rows.
For month breakdowns, show actual, target, variance and achievement where supported,
in chronological order, with missing-target/partial-period status.

## Dates and fiscal periods

Inspect the chosen date table, active relationships and model instructions.
Do not assume every model uses an April fiscal-year start. Use calendar year when
explicitly requested; clarify an unqualified year if source fiscal/calendar
semantics materially differ and no source default resolves it.

Verify the date column type and key encoding. A DateID encoded YYYYMMDD requires
an integer such as 20130515 for 2013-05-15; a FiscalYearKey like 201819 can denote
2018-2019 only if this model defines it that way. These are examples, not global
schema facts or hardcoded filters.

Honor the date role (order, invoice, delivery, return) relevant to the metric.
Do not compare a full prior period with an incomplete current period without
labeling the difference. Use model time-intelligence measures and valid date context.

## Customer, product and delivery analysis

Resolve named entities before filtering. Use the model's published hierarchy
and grain; do not infer mappings from text similarity.
Use existing on-time, in-full, DIFOT/OTIF and lead-time definitions. Do not infer
a delivery KPI from Sales amount or apply an arbitrary tolerance window.

For diagnostics, identify observed contributions separately from possible causes.
A customer/product ranking does not by itself establish causality.
