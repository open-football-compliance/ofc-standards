# OFE Reference Document Validation — FPF Boletim Financeiro 21181

**Validation record:** OFE-VAL-FPF-21181  
**Reference document:** Boletim Financeiro FPF nº 21181  
**Match:** Náutico - PE x Sport Recife - PE  
**Competition shown in source:** Campeonato Brasileiro Série B  
**Match date:** 26 September 2026  
**Document:** 2 pages  
**Standard under review:** OFC Borderô Data Standard 1.0.0  
**Validation status:** Structural and arithmetic checks completed; financial interpretation partially unresolved  
**Date recorded:** November 2026

---

## 1. Purpose and limitation

This record documents the first empirical review of the OFC canonical match record against a real FPF financial bulletin.

The source is a Série B match, not a state championship fixture. It is used only to inspect the FPF document structure. It does not establish that the OFE's state-competition coverage has been empirically validated, nor does it establish compatibility with other federations.

## 2. Source structure observed

The two-page bulletin contains:

- Match and competition identification.
- Ticket table with location, available, returned, sold, unit price and proceeds.
- Expense sections B1 (rentals and insurance), B2 (fees and taxes) and B3 (operating expenses).
- Total expenses and reported net revenue.
- Net revenue distribution among clubs, with tax IDs, percentages, discounts and net payable amounts.

## 3. Ticket-table reconciliation

| Check | Source / normalized result |
|---|---:|
| Ticket lines transcribed | 26 |
| Available quantity total | 10,056 |
| Returned quantity total | 0 |
| Sold quantity total | 10,056 |
| Ticket proceeds total | BRL 569,746.50 |
| Declared ticket-table proceeds | BRL 569,746.50 |

The ticket-line proceeds reconcile exactly to the gross revenue printed in the source. Sold tickets are not treated as attendance or paying attendance.

## 4. Financial-section reconciliation

All 17 financial line items were represented: one in B1, two in B2 and fourteen in B3.

| Source section | Sum of transcribed line items | Declared section total | Check |
|---|---:|---:|---|
| B1 | BRL 321.79 | BRL 321.79 | Match |
| B2 | BRL 56,974.66 | BRL 56,974.66 | Match |
| B3 | BRL 245,865.58 | BRL 245,865.58 | Match |
| Total expenses | BRL 303,162.03 | BRL 303,162.03 | Match |

The declared gross revenue is BRL 569,746.50 and the declared net revenue is BRL 266,584.47. The source arithmetic reconciles:

`569,746.50 - 303,162.03 = 266,584.47`

Source-section totals are preserved separately from OFC financial-class totals. The B1/B2/B3 headings do not automatically determine the OFC classification.

## 5. Classification decisions and unresolved item

- `SEGURO TORCEDOR`: mapped provisionally to match insurance / operating expense.
- `5% - FEDERAÇÃO LOCAL`: mapped to federation fee.
- The two INSS lines: mapped provisionally to tax/statutory charge based on their descriptions, even though one appears in B3.
- The refereeing service line: mapped to operating expense.
- Other identified B3 operational lines: mapped to their corresponding operating expense categories.
- `INGRESSO PROMOCIONAL` (BRL 89,825.00): remains unclassified.

The source label “INGRESSO PROMOCIONAL” does not establish whether the amount represents a discount, subsidy, waived ticket revenue, promotional allocation or another expense. It must not be automatically included as an operating expense or deduction without further evidence.

Because this is a material unresolved line, the example's methodological net result and retention margin remain unavailable (`null`). The source's reported net revenue is retained as declared.

The INSS classifications are methodological mappings based on source descriptions and require accounting/legal review before being used for external comparisons as definitive tax treatment.

## 6. Revenue distribution reconciliation

| Beneficiary | Share | Net payable |
|---|---:|---:|
| Náutico - PE | 100% | BRL 266,584.47 |
| Sport Recife - PE | 0% | BRL 0.00 |
| **Total** | **100%** | **BRL 266,584.47** |

Percentages and net payable values reconcile to the distribution shown in the source.

## 7. Schema and automated validation

The repository includes:
- JSON Schema Draft 2020-12 for the canonical record.
- A reference example containing the 26 ticket rows, 17 financial items and two distribution records.
- A Python validation script for JSON Schema validation, catalog/document references and sample-specific arithmetic checks.
- A GitHub Actions workflow to run these checks on relevant pushes and pull requests.

The existence of the workflow and script is not itself evidence of a successful CI run. The first GitHub Actions execution must be inspected and confirmed before this validation is marked as CI-passed.

## 8. Remaining limitations

1. Only one FPF document has been used as the reference sample.
2. The sample belongs to Série B, not a state championship.
3. No document from another federation has been tested.
4. Attendance is not inferred from sold ticket quantities.
5. The promotional-ticket line is unresolved, preventing a complete methodological result for this example.
6. The INSS mappings require further accounting review.
7. The document hash and page-level evidence coordinates have not yet been populated in the example.

## 9. Conclusion

The sample supports the canonical representation of match identification, ticket lines, source sections, financial line items, source-section totals and revenue distribution for the examined FPF bulletin.

It does not support a complete methodological net result for this match because one material financial line remains unclassified. It also does not establish universal FPF coverage or compatibility with other federations.

The sample is therefore accepted as a structural reference fixture with explicit limitations, not as proof of universal compatibility or complete financial classification.
