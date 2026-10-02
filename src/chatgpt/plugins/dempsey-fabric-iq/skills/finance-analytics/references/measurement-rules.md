# Finance measurement rules

## Source precedence and metric definitions

Honor explicit user scope, matched verified answers, model CustomInstructions and
applicable report context through Fabric IQ. Use published measures for revenue,
expenses, profit, margins, ratios and statement totals. Source definitions prevail
over these default interpretation rules.

Keep accounting revenue distinct from sales-order, invoiced and delivered revenue.
Gross profit, operating profit, EBITDA and net profit are different metrics; use
the source's named measure or clarify. Never build a KPI from guessed account lists.

## Statements and account signs

Use the model/report account hierarchy, line ordering and display signs. Ledger
debit/credit conventions may differ from statement presentation. Do not apply ABS,
flip signs or label every negative amount as a loss. Do not double-count hierarchy
subtotals and leaf accounts. Retain source-defined consolidation/elimination rules.

A balance sheet is generally an as-of stock; an income statement is a period flow.
Use the model's established balance measure/date logic. Do not sum balances over
months as if they were revenue. Do not reconstruct cash flow from balance changes
unless the source defines the required adjustment method.

## Actual versus budget

Align period, company/entity, reporting currency, scenario and budget version.
Use source-defined variance measures when available. Otherwise label actual -
budget as an arithmetic variance only after validating the metric and signs.

Positive revenue variance and positive expense variance can have opposite business
interpretations. Do not assign favorable/unfavorable labels using sign alone.
Confirm whether revenue/cost amounts are displayed as positive or signed ledger
values. Treat missing budgets as unavailable; do not fill with zero.

For ratios/percentages, use source measures or safe division only after confirming
numerator/denominator semantics. Do not average or sum row-level percentages to
create a total. Use ratio of valid aggregate measures or the source's total result.

## Period and completeness

Derive fiscal-year boundaries, period labels, closing status and date roles from
the chosen model. Never impose a fiscal calendar from another workspace/model.
An unqualified year requires clarification when source defaults do not resolve a
material fiscal/calendar ambiguity.

Distinguish full-year, YTD, quarter, month and as-of requests. Align comparison
boundaries. Label incomplete/open periods where evidenced; do not assert that a
period is closed without source evidence. Do not infer data freshness from the
clock or a future date dimension row.

## Currency, entity and units

Use source-defined local/group/reporting currency measures and display scaling.
Do not sum multiple currencies as one amount or invent conversion rates.
Clarify the currency/entity choice when it changes the interpretation and the
selected source lacks a default. Keep thousands/millions and percentage vs
percentage-point changes explicit.

## Receivables, payables and working capital

Use the model's aging buckets, due-date/as-of logic and published balance/turnover
measures. Do not assume a 30-day overdue definition, 365-day denominator or working
capital formula when the source defines another. If the necessary fields/KPIs
are absent, explain what the source cannot answer instead of estimating.

Separate observed financial movements from hypotheses about operational causes.
A profit decline alongside a sales change does not establish the cause.
