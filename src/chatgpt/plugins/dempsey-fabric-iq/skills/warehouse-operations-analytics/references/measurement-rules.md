# Warehouse Operations measurement rules

## Source and grain

Use Manhattan SCALE-derived model definitions, verified answers and published
measures. Identify warehouse/site, owner, SKU, location, lot and inventory status
only where modeled. Distinguish order, line, task, receipt and handling-unit grain;
repeated events or split tasks must not inflate distinct business-object counts.
Never assume table names, status codes or joins from familiarity with SCALE.

## Inventory

Separate on-hand, available, allocated, held and in-transit quantities according
to source definitions. Inventory snapshots are as-of stocks; do not sum successive
snapshots. Distinguish movement flows from balances. Align units of measure and
validated conversions before combining eaches, cases, pallets or weight. Do not
interpret warehouse quantities as Business Central valuation or RMS store stock.

## Replenishment

Distinguish requested, released, completed and outstanding replenishment using
modeled statuses. Separate task counts from lines and moved units. Derive backlog
as of the requested time, not from today's open status alone. Do not equate a
replenishment task with a purchase receipt or assume completion means availability.

## Receiving and putaway

Receiving, inbound arrival and putaway completion are different events. Use the
source's expected/received/accepted quantities, timestamps and completion rules.
Do not count the same stock at receiving and putaway as two inbound receipts.
Dock-to-stock and putaway duration require validated start/end events, time zones,
partial-receipt handling and exclusions. Missing completion timestamps are not
zero duration; report open work separately where the model supports it.

## Outbound and picking

Separate order release, allocation, picking, packing and shipping when available.
Picked quantity is not automatically shipped or delivered quantity. Use source
rules for partial picks, shorts, cancellations, rework and completion. Do not infer
customer delivery performance from pick completion alone.

## Rates and periods

Use source-defined accuracy, productivity, service and throughput measures. A
units-per-labor-hour metric requires the defined labor-hour denominator; elapsed
shift time is not a substitute. Aggregate valid numerators and denominators rather
than averaging percentages. Align shifts, time zones, sites and units. Treat
missing targets or zero denominators as undefined unless the source says otherwise.
