# Retail Operations measurement rules

## Source scope

RMS-derived facts and dimensions define this domain. RMS vendor, version, table
names and available processes are unspecified: inspect the selected model and use
its instructions, verified answers and published measures. Sales, returns, stock,
promotions and store performance are possible questions, not guaranteed coverage.

## Transactions and sales

If supported, distinguish transaction/header, line, tender and return grain.
Use validated identities across stores and periods; do not count fact lines as
transactions or duplicate sales through payment detail. Distinguish gross/net
sales, discounts, taxes, voids and returns using source definitions. Do not deduct
returns twice. Identify whether returns use original-sale date or return date.

## Store and product comparisons

Resolve stores, products and categories through ValueSearch and modeled mappings.
Use source-defined comparable-store cohorts and trading calendars; do not infer
like-for-like growth from all-store totals. Identify store openings, closures and
partial periods only where supported by evidence. Do not assume a promotion caused
a sales change. Margin and basket measures require validated numerator/denominator
and cost definitions, not guessed formulas.

## Inventory and replenishment

Where RMS exposes stock, use its store/location scope, status and as-of rules.
Do not sum snapshots over time or treat Manhattan SCALE warehouse stock as RMS
store stock. Stock movements, transfers and adjustments require source-defined
signs and stages. Retail replenishment remains here when explicitly RMS-based;
warehouse replenishment execution belongs to Warehouse Operations.

## Dates, currency and targets

Distinguish business/trading date from posting date and timestamp. Align currency,
units, entity, calendar and target grain before comparisons. Do not sum mixed
currencies, duplicate monthly targets over transaction rows, average percentages
for totals or turn absent targets into zero performance. Unsupported metrics must
be reported as unavailable.
