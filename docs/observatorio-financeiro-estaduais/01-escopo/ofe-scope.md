# Observatório Financeiro dos Estaduais (OFE)

**Organization:** Open Football Compliance (OFC)  
**Document ID:** OFC-OFE-SCOPE  
**Version:** 0.1  
**Status:** Draft  
**Initial season:** 2027  
**Last updated:** November 2026

---

## 1. Overview

O Observatório Financeiro dos Estaduais (OFE) é uma iniciativa institucional do Open Football Compliance (OFC) dedicada à coleta, estruturação, análise e publicação de informações financeiras relacionadas às partidas dos campeonatos estaduais de futebol brasileiro.

A iniciativa busca centralizar informações atualmente dispersas em documentos oficiais publicados por federações e organizadores de competições, especialmente borderôs financeiros de partidas.

A partir desses documentos, o OFE pretende construir uma base estruturada e comparável de informações sobre receitas, despesas operacionais, público e resultados financeiros dos eventos.

O observatório tem como finalidade ampliar a transparência, apoiar análises econômicas e contribuir para o debate sobre a sustentabilidade financeira das competições estaduais.

## 2. Objectives

### 2.1 General objective

Desenvolver uma base estruturada de informações financeiras das partidas dos campeonatos estaduais, permitindo acompanhar, analisar e comparar aspectos econômicos e operacionais dessas competições.

### 2.2 Specific objectives

- Centralizar informações financeiras publicadas oficialmente pelas federações.
- Estruturar dados de borderôs em um modelo padronizado.
- Desenvolver indicadores financeiros e operacionais por partida e competição.
- Identificar padrões de receitas, despesas e público.
- Analisar a sustentabilidade econômica dos eventos.
- Disponibilizar informações e relatórios para pesquisadores, imprensa, gestores e torcedores.
- Estimular maior transparência na divulgação de informações financeiras do futebol.

## 3. Scope

### 3.1 Unit of analysis

A unidade primária de análise do OFE é a **partida de futebol**.

Cada partida deve possuir um identificador único dentro da respectiva competição e temporada.

Os documentos financeiros publicados para uma partida são tratados como fontes documentais associadas a essa unidade de análise.

Uma partida poderá possuir mais de uma versão documental, por exemplo, em situações de retificação ou republicação de borderô.

### 3.2 Initial scope

A iniciativa começa com os campeonatos estaduais brasileiros, priorizando competições profissionais e seus documentos financeiros oficiais.

O escopo inicial contempla:

- Receitas de bilheteria e outras receitas vinculadas à partida, quando discriminadas.
- Público pagante e não pagante.
- Público total.
- Despesas operacionais.
- Taxas, tributos e deduções.
- Resultado financeiro declarado ou calculado conforme a metodologia do OFE.

### 3.3 Competition expansion phases

A expansão nacional será conduzida progressivamente.

| Phase | Competitions / States | Objective |
|---|---|---|
| Phase 1 | Campeonato Pernambucano | Initial pilot and methodology validation |
| Phase 2 | Ceará, Bahia and Paraíba | Regional expansion |
| Phase 3 | Pará | Expansion to the North region |
| Phase 4 | São Paulo and Rio de Janeiro | Expansion to major national competitions |

The expansion sequence may be revised according to document availability, data quality, operational capacity and institutional partnerships.

## 4. Inclusion criteria

A match may be included in the OFE dataset when it satisfies the following conditions:

1. It belongs to an official professional competition included in the observatory's scope.
2. It has an identifiable match record.
3. An official financial document, preferably a borderô, is available or can be obtained from an official source.
4. Financial information can be associated with the respective match.
5. The source and its provenance can be documented.

The existence of a document does not automatically mean that all its information is eligible for every indicator.

## 5. Exclusion criteria

The following items are outside the initial scope:

- National and regional competitions, including Campeonato Brasileiro, Copa do Brasil, Copa do Nordeste and Copa Verde.
- Friendly matches and preseason events.
- Financial estimates without verifiable supporting documentation.
- General club revenues not directly attributable to a match, such as general broadcasting or sponsorship revenues not reported in the event's financial document.
- Records whose association with a specific match cannot be established.

Exclusion from the analytical dataset does not imply deletion of the original source or its collection history.

## 6. Data sources

### 6.1 Primary sources

The primary source is the official financial document of the match, especially the borderô published by the relevant federation or competition organizer.

### 6.2 Supporting sources

Additional sources may be used to identify or contextualize information, including:

- Official federation publications.
- Official competition regulations.
- Stadium information and capacity documentation.
- Official club communications.
- Other institutional publications relevant to the match.

Supporting sources must be identified separately from the primary financial document.

### 6.3 Source preservation

Whenever legally and technically possible, the original document must be preserved.

The observatory must maintain traceability between published information and its original source.

## 7. Data classification

The OFE distinguishes four information layers:

### 7.1 Original data

Values and descriptions exactly as presented in the source document.

### 7.2 Normalized data

Values mapped to the OFC Borderô Data Standard, including standardized labels, categories, units and formats.

Original values must remain preserved.

### 7.3 Derived data

Indicators and calculations produced from normalized data according to the OFE Financial Indicators Dictionary.

### 7.4 Interpretations

Analytical observations, comparisons, anomaly alerts and editorial conclusions produced by the OFC.

These layers must remain distinguishable in the data pipeline and in published analyses.

## 8. Data quality and analytical eligibility

### 8.1 Missing information

Missing information must be represented as null, not zero.

A zero value is valid only when the source explicitly reports zero or when a documented and validated derivation produces zero.

### 8.2 Inconsistencies

When information is inconsistent, the original values must be preserved and the inconsistency documented.

Examples include:

- Attendance components that do not reconcile with declared total attendance.
- Differences between reported gross revenue, expenses, deductions and net revenue.
- Missing or ambiguous financial categories.
- Conflicting values between different versions of an official document.

### 8.3 Indicator-specific eligibility

Eligibility must be evaluated independently for each indicator.

The absence of stadium capacity, for example, prevents calculation of occupancy but does not necessarily prevent calculation of retention margin.

Likewise, missing paying attendance prevents calculation of revenue per paying attendee but does not automatically invalidate other indicators.

### 8.4 Structural incompleteness

A match may be classified as structurally incomplete when essential information is absent or when the source contains unresolved inconsistencies that compromise the reliability of the affected financial calculations.

The affected indicators must be marked as ineligible, with an explicit reason.

## 9. Comparability principles

Comparisons must consider differences in:

- Competition and season.
- Document structure and accounting conventions.
- Classification of revenue and expense categories.
- Attendance counting practices.
- Stadium capacity and configuration.
- Restrictions on attendance, including closed-door matches and sanctions.
- Availability and completeness of financial information.

Comparisons should use equivalent data definitions and eligible samples.

When conditions differ materially, the OFE must disclose the limitation or present results in separate groups.

## 10. Coverage and transparency

The OFE must distinguish at least the following quantities:

- Total matches in the competition.
- Matches for which an official document was located.
- Matches with an ingested document.
- Matches with validated financial information.
- Matches eligible for each published indicator.

Coverage information must accompany aggregate reports whenever relevant.

A competition-level average must identify the number of matches effectively used in its calculation.

## 11. Publications

The OFE may publish:

- Match-level financial records.
- Periodic competition bulletins.
- Comparative financial analyses.
- Competition-level summaries.
- Season reports.
- Methodological notes and data quality reports.

Publications must identify their data sources, methodological version, analytical period, coverage and limitations.

## 12. Institutional responsibilities

The Open Football Compliance is responsible for:

- Defining the observatory's scope.
- Establishing the financial methodology.
- Governing the data standards and indicator definitions.
- Reviewing analytical interpretations.
- Approving institutional publications.

Technology providers may develop systems and services for ingestion, extraction, normalization, validation, storage and distribution of data.

Technical implementation does not transfer institutional governance of the OFE methodology or standards to the technology provider.

## 13. Initial implementation roadmap

| Period | Main activity |
|---|---|
| November–December 2026 | Methodology, data standard and historical pilot preparation |
| January 2027 | Public launch of the OFE and monitoring of the Pernambuco championship |
| January–March 2027 | Collection, validation and periodic publication |
| Following phases | Expansion to additional state championships |

Collection and preparation activities should begin before the public launch, using available historical and current-season documents to validate the methodology and technical pipeline.

## 14. Related documents

- `financial-indicators-dictionary-v0.1.md` — formal definitions and calculation rules for financial indicators.
- `bordero-data-standard-v0.1.md` — canonical data contract for match financial documents.
- `bordero-v0.1.schema.json` — machine-readable validation schema.
- `financial-categories-v0.1.json` — initial financial category catalog.

## 15. Version history

| Version | Date | Description |
|---|---|---|
| 0.1 | November 2026 | Initial scope specification |