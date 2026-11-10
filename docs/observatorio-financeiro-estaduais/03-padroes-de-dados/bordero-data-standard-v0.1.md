# OFC Borderô Data Standard

**Organization:** Open Football Compliance (OFC)  
**Document ID:** OFC-OFE-BORDEROU  
**Version:** 0.1  
**Status:** Draft  
**Domain:** Match-level financial data  
**Initial application:** Observatório Financeiro dos Estaduais (OFE)  
**Last updated:** November 2026

---

## 1. Purpose

Este documento define o padrão canônico para representação de informações financeiras e operacionais extraídas de borderôs e documentos financeiros oficiais de partidas de futebol.

O objetivo é estabelecer uma estrutura independente do layout, da terminologia e da organização documental adotados por federações, clubes e organizadores de competições.

O padrão permite que documentos heterogêneos sejam transformados em registros estruturados, preservando a origem das informações, suas classificações e as transformações realizadas.

## 2. Scope

### 2.1 Included information

O padrão contempla:

- Identificação da partida.
- Competição e temporada.
- Clubes participantes.
- Estádio e informações de realização.
- Público e categorias de acesso.
- Receitas vinculadas à partida.
- Despesas operacionais.
- Taxas, tributos e deduções.
- Resultado financeiro declarado.
- Documentos de origem.
- Evidências de extração e validação.

### 2.2 Exclusions

Este padrão não define:

- Demonstrações financeiras anuais dos clubes.
- Contabilidade geral das organizações esportivas.
- Receitas de contratos não vinculadas à partida.
- Contratos de direitos de transmissão.
- Folha salarial ou custos gerais dos departamentos de futebol.
- Reconciliação bancária.
- Auditoria independente das demonstrações financeiras.

O padrão é específico para dados financeiros no nível de partida e não substitui o Open Football Accounting Standard (OFAS).

## 3. Design principles

### 3.1 Canonical representation

Todos os documentos devem ser convertidos para um modelo canônico, independentemente do formato de origem.

### 3.2 Source preservation

O valor original, a descrição original e a localização da informação na fonte devem ser preservados sempre que disponíveis.

### 3.3 Normalization without information loss

A normalização não deve eliminar informações presentes no documento original.

Valores originais e normalizados devem ser armazenados separadamente.

### 3.4 Explicit uncertainty

Informações ausentes, ambíguas ou não verificadas devem ser identificadas explicitamente.

Um valor ausente não pode ser interpretado automaticamente como zero.

### 3.5 Traceability

Cada informação extraída deve possuir vínculo com a fonte documental e, quando disponível, com a evidência específica que fundamentou sua extração.

### 3.6 Extensibility

O modelo deve permitir incorporar novas rubricas, campos e variações documentais sem exigir alterações incompatíveis em todos os consumidores.

## 4. Conceptual data model

O padrão organiza as informações em seis entidades principais:

| Entity | Description |
|---|---|
| Match | Identificação e contexto da partida |
| Document | Documento financeiro original |
| Attendance | Informações de público |
| Financial Item | Rubrica individual de receita, despesa, taxa ou dedução |
| Financial Summary | Totais e resultados declarados no documento |
| Extraction Record | Proveniência, evidências, confiança e validação |

Uma partida pode estar associada a múltiplos documentos e versões documentais.

Cada documento pode conter diversas rubricas financeiras e informações de público.

## 5. Match entity

A entidade Match identifica a partida à qual os dados financeiros estão associados.

| Field | Type | Required | Description |
|---|---|---|---|
| match_id | string | Yes | Identificador único no sistema consumidor |
| competition_name | string | Yes | Nome da competição |
| competition_season | string | Yes | Temporada |
| stage | string/null | No | Fase da competição |
| match_date | date/null | No | Data da partida |
| home_team | object | Yes | Clube mandante |
| away_team | object | Yes | Clube visitante |
| venue | object/null | No | Estádio ou local |
| match_status | string/null | No | Situação da partida |

### 5.1 Team object

| Field | Type | Required | Description |
|---|---|---|---|
| name | string | Yes | Nome original do clube |
| normalized_name | string/null | No | Nome padronizado |
| federation_id | string/null | No | Identificador federativo, quando disponível |

### 5.2 Venue object

| Field | Type | Required | Description |
|---|---|---|---|
| name | string | Yes | Nome do estádio |
| city | string/null | No | Município |
| state | string/null | No | Estado |
| usable_capacity | integer/null | No | Capacidade utilizável documentada |
| capacity_source | string/null | No | Fonte da capacidade |

A capacidade do estádio deve ser acompanhada de sua fonte e contexto de utilização.

## 6. Document entity

Representa o documento utilizado como fonte dos dados.

| Field | Type | Required | Description |
|---|---|---|---|
| document_id | string | Yes | Identificador único do documento |
| match_id | string | Yes | Partida associada |
| document_type | string | Yes | Tipo documental |
| source_url | string/null | No | URL da publicação original |
| source_organization | string/null | No | Federação ou entidade publicadora |
| publication_date | date/null | No | Data de publicação |
| collection_timestamp | datetime | Yes | Data e hora de coleta |
| original_filename | string/null | No | Nome original do arquivo |
| mime_type | string/null | No | Tipo MIME |
| file_hash | string/null | No | Hash criptográfico do arquivo |
| document_version | string/null | No | Identificação da versão documental |
| is_official | boolean | Yes | Indica se a fonte foi identificada como oficial |

### 6.1 Document types

Valores iniciais:

- `official_match_report`
- `financial_match_report`
- `match_bordero`
- `corrected_bordero`
- `supporting_document`
- `other`

Um documento retificado deve ser registrado como nova versão, sem sobrescrever silenciosamente o documento anterior.

## 7. Attendance entity

Representa as informações de público declaradas no documento.

| Field | Type | Required | Description |
|---|---|---|---|
| total_attendance | integer/null | No | Público total |
| paying_attendance | integer/null | No | Público pagante |
| non_paying_attendance | integer/null | No | Público não pagante |
| paying_categories | array | No | Categorias de público pagante |
| non_paying_categories | array | No | Categorias de público não pagante |
| attendance_notes | string/null | No | Observações |

Cada categoria pode possuir:

- `source_label`: descrição original.
- `normalized_category`: categoria normalizada.
- `quantity`: quantidade declarada.

Categorias desconhecidas devem ter sua descrição original preservada.

Não se deve derivar automaticamente público não pagante subtraindo pagantes do total sem registrar que o valor foi calculado.

## 8. Financial Item entity

Representa cada rubrica financeira individual encontrada no documento.

É a entidade central para lidar com diferenças entre os borderôs.

| Field | Type | Required | Description |
|---|---|---|---|
| item_id | string | Yes | Identificador do item |
| document_id | string | Yes | Documento de origem |
| source_label | string | Yes | Descrição original da rubrica |
| normalized_label | string/null | No | Descrição normalizada |
| financial_class | string | Yes | Classe financeira |
| canonical_category | string/null | No | Categoria padronizada |
| amount | decimal | Yes | Valor monetário |
| currency | string | Yes | Moeda |
| accounting_role | string/null | No | Papel da rubrica na composição financeira |
| evidence_id | string/null | No | Evidência de origem |
| classification_status | string | Yes | Situação da classificação |

### 8.1 Financial classes

Valores iniciais:

- `revenue`
- `operating_expense`
- `tax`
- `fee`
- `deduction`
- `adjustment`
- `other`
- `unknown`

A classificação `unknown` deve ser utilizada quando não houver evidência suficiente para determinar a natureza da rubrica.

### 8.2 Accounting roles

Valores iniciais:

- `gross_revenue_component`
- `operating_expense_component`
- `tax_component`
- `fee_component`
- `deduction_component`
- `adjustment_component`
- `informational_only`
- `unclassified`

A classe financeira e o papel contábil são dimensões diferentes. Por exemplo, uma taxa pode ser classificada como `fee` e possuir papel `fee_component`.

### 8.3 Financial category examples

Categorias iniciais sugeridas:

**Revenue**
- `ticket_sales`
- `membership_revenue`
- `other_match_revenue`

**Operating expenses**
- `security`
- `cleaning`
- `medical_services`
- `ambulance`
- `var_services`
- `stadium_operations`
- `other_operational_expense`

**Taxes and fees**
- `taxes`
- `federation_fees`
- `administrative_fees`
- `other_fees`

**Deductions**
- `ticketing_deductions`
- `withholdings`
- `other_deductions`

Este catálogo é inicial e não deve ser considerado exaustivo.

## 9. Financial Summary entity

Representa os totais declarados diretamente no documento.

| Field | Type | Required | Description |
|---|---|---|---|
| gross_revenue_reported | decimal/null | No | Receita bruta declarada |
| operating_expenses_reported | decimal/null | No | Despesas operacionais declaradas |
| taxes_reported | decimal/null | No | Tributos declarados |
| fees_reported | decimal/null | No | Taxas declaradas |
| deductions_reported | decimal/null | No | Deduções declaradas |
| net_revenue_reported | decimal/null | No | Resultado líquido declarado |
| other_totals | array | No | Outros totais declarados |

Os totais declarados devem ser preservados independentemente dos valores recalculados pelo OFE.

Diferenças entre os totais e a soma das rubricas devem gerar registros de validação.

## 10. Extraction Record entity

Registra como cada informação foi obtida e validada.

| Field | Type | Required | Description |
|---|---|---|---|
| extraction_id | string | Yes | Identificador da execução |
| document_id | string | Yes | Documento processado |
| extraction_method | string | Yes | Método de extração |
| extraction_timestamp | datetime | Yes | Data e hora da extração |
| model_or_tool | string/null | No | Modelo ou ferramenta utilizada |
| pipeline_version | string/null | No | Versão do pipeline |
| review_status | string | Yes | Situação da revisão |
| validation_status | string | Yes | Resultado geral da validação |

### 10.1 Extraction methods

- `manual`
- `ocr`
- `automated`
- `hybrid`

### 10.2 Review status

- `pending`
- `reviewed`
- `approved`
- `rejected`

### 10.3 Validation status

- `not_validated`
- `valid`
- `valid_with_warnings`
- `invalid`

## 11. Evidence and provenance

Toda informação crítica deve ser rastreável à fonte documental.

A evidência deve permitir identificar, sempre que tecnicamente possível:

- Documento de origem.
- Página.
- Região ou coordenadas da informação.
- Texto original identificado.
- Valor extraído.
- Valor normalizado.
- Método de extração.
- Responsável ou processo que aprovou a informação.

### 11.1 Evidence object

| Field | Type | Required | Description |
|---|---|---|---|
| evidence_id | string | Yes | Identificador da evidência |
| document_id | string | Yes | Documento de origem |
| page_number | integer/null | No | Página |
| bounding_box | object/null | No | Coordenadas da região |
| source_text | string/null | No | Texto original |
| extracted_value | string/null | No | Valor identificado |
| evidence_type | string | Yes | Tipo de evidência |

A evidência deve permanecer associada ao registro correspondente, e não apenas ao documento inteiro.

## 12. Normalization and mapping

A normalização deve ser realizada por meio de mapeamentos entre os rótulos originais e as categorias canônicas do OFC.

Exemplo:

| Source label | Canonical category |
|---|---|
| Segurança | security |
| Serviço de segurança | security |
| Policiamento | security |
| Ambulância | ambulance |
| Serviço médico | medical_services |
| Taxa da federação | federation_fees |

O mapeamento deve registrar:

- Rótulo original.
- Categoria canônica.
- Regra de mapeamento.
- Versão do catálogo.
- Grau de confiança ou situação de revisão.
- Justificativa, quando necessária.

Rótulos semelhantes não devem ser agrupados automaticamente sem considerar seu significado financeiro.

## 13. Validation rules

### 13.1 Structural validation

- Identificadores obrigatórios devem estar presentes.
- Tipos de dados devem respeitar o padrão.
- Valores monetários devem utilizar representação decimal.
- Datas devem seguir ISO 8601.
- Moedas devem utilizar códigos ISO 4217.
- Referências documentais devem ser válidas.

### 13.2 Attendance validation

- Quantidades devem ser inteiros não negativos.
- Público pagante não deve exceder o público total, salvo inconsistência explicitamente registrada.
- Soma das categorias deve ser comparada com os totais declarados.
- Divergências devem gerar avisos ou erros conforme sua gravidade.

### 13.3 Financial validation

- Valores monetários devem ser numericamente válidos.
- Rubricas não podem ser contabilizadas em múltiplas categorias incompatíveis.
- Totais declarados devem ser comparados com a soma das rubricas aplicáveis.
- Diferenças devem ser registradas.
- Não se deve presumir que todas as rubricas são aditivas.

### 13.4 Provenance validation

- Todo documento deve possuir identificação.
- Dados críticos devem possuir evidência ou justificativa de ausência.
- Alterações manuais devem ser registradas.
- Versões documentais devem ser preservadas.

## 14. Confidence and review

A confiança da extração e a validação metodológica são dimensões diferentes.

Uma extração pode apresentar alta confiança textual, mas ainda possuir classificação financeira incorreta.

Por isso, o padrão distingue:

- Confidence in extraction: confiança de que o conteúdo foi identificado corretamente.
- Classification confidence: confiança no mapeamento semântico da rubrica.
- Validation status: resultado das verificações estruturais e financeiras.
- Review status: situação da revisão humana.

Sistemas de extração devem preservar essas dimensões separadamente.

## 15. Versioning and compatibility

O padrão segue versionamento semântico adaptado:

- `0.x`: versões preliminares.
- `1.0`: primeira versão normativa aprovada.
- Incremento de versão menor: novas capacidades compatíveis.
- Incremento de versão maior: alterações incompatíveis.

Campos adicionais devem ser introduzidos de maneira compatível sempre que possível.

Campos desconhecidos não devem causar perda de informações durante a ingestão.

## 16. Conformance

Uma implementação é considerada compatível com o OFC Borderô Data Standard quando:

1. Representa os dados segundo as entidades e definições deste documento.
2. Preserva os valores e rótulos originais.
3. Mantém rastreabilidade documental.
4. Aplica as regras de normalização e validação.
5. Distingue dados originais, normalizados e derivados.
6. Registra informações ausentes e inconsistências.
7. Respeita a versão declarada do padrão.

A conformidade técnica não representa certificação da veracidade contábil dos documentos de origem.

## 17. Related documents

- `ofe-scope.md` — escopo do Observatório Financeiro dos Estaduais.
- `financial-indicators-dictionary-v0.1.md` — definições e fórmulas dos indicadores.
- `schemas/bordero-v0.1.schema.json` — schema de validação.
- `catalogs/financial-categories-v0.1.json` — catálogo de categorias financeiras.
- `examples/match-example-v0.1.json` — exemplo de registro canônico.

## 18. Version history

| Version | Date | Description |
|---|---|---|
| 0.1 | November 2026 | Initial canonical borderô data standard |