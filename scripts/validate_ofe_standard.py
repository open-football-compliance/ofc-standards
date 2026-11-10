#!/usr/bin/env python3
"""Validate the OFE v1.0.0 schema, example and semantic reconciliation checks."""
import json
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "docs/observatorio-financeiro-estaduais/03-padroes-de-dados"

def load(path):
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)

schema = load(BASE / "schemas/bordero.schema.json")
example = load(BASE / "examples/match-example.json")
catalog = load(BASE / "catalogs/financial-categories.json")

Draft202012Validator.check_schema(schema)
errors = sorted(
    Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(example),
    key=lambda error: list(error.absolute_path),
)
if errors:
    for error in errors:
        location = ".".join(str(part) for part in error.absolute_path) or "<root>"
        print(f"SCHEMA ERROR at {location}: {error.message}")
    raise SystemExit(1)

category_by_code = {item["code"]: item for item in catalog["categories"]}
document_ids = {item["document_id"] for item in example["documents"]}

for item in example["financial_items"]:
    if item["document_id"] not in document_ids:
        raise SystemExit(f"Unknown document_id in financial item {item['item_id']}")
    code = item["canonical_category"]
    if code is not None:
        category = category_by_code.get(code)
        if category is None:
            raise SystemExit(f"Unknown category {code} in {item['item_id']}")
        for field in ("financial_class", "accounting_role"):
            if item[field] != category[field]:
                raise SystemExit(
                    f"Category mismatch in {item['item_id']}: {field} "
                    f"{item[field]} != {category[field]}"
                )

for group in ("ticket_sales", "revenue_distribution"):
    for item in example.get(group, []):
        if item["document_id"] not in document_ids:
            raise SystemExit(f"Unknown document_id in {group}: {item}")

ticket_sales = example.get("ticket_sales", [])
financial_items = example["financial_items"]
sections = example["financial_summary"]["declared_source_sections"]
sum_minor = lambda rows, field: sum(row[field] for row in rows)

# Reconciliation checks for the committed FPF reference fixture.
assert len(ticket_sales) == 26, "Unexpected ticket-line count in reference fixture"
assert sum_minor(ticket_sales, "sold_quantity") == 10056
assert sum_minor(ticket_sales, "proceeds_minor") == 56974650
assert sum_minor([x for x in financial_items if x["source_section"].startswith("B1")], "amount_minor") == sections["b1_minor"]
assert sum_minor([x for x in financial_items if x["source_section"].startswith("B2")], "amount_minor") == sections["b2_minor"]
assert sum_minor([x for x in financial_items if x["source_section"].startswith("B3")], "amount_minor") == sections["b3_minor"]
assert sections["b1_minor"] + sections["b2_minor"] + sections["b3_minor"] == sections["total_expenses_minor"]
assert sum_minor(example["revenue_distribution"], "share_percentage") == 100
assert sum_minor(example["revenue_distribution"], "net_payable_minor") == example["financial_summary"]["declared"]["net_revenue_minor"]

# The unresolved promotional-ticket line must never be silently counted as an expense.
unclassified = [
    item for item in financial_items
    if item["source_label"] == "INGRESSO PROMOCIONAL"
]
assert len(unclassified) == 1
assert unclassified[0]["financial_class"] == "unknown"
assert unclassified[0]["canonical_category"] is None
assert example["financial_summary"]["calculation_status"] == "partial"
assert example["financial_summary"]["calculated"]["net_revenue_minor"] is None

print("OFE v1.0.0 validation passed:")
print("- JSON Schema Draft 2020-12 and format validation")
print("- category and document references")
print("- 26 ticket lines, 10,056 sold, R$ 569,746.50 proceeds")
print("- B1/B2/B3 subtotals and declared expense total")
print("- revenue distribution reconciliation")
print("- unresolved promotional-ticket item excluded from methodological result")
