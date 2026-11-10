# OFC Borderô Data Standard

**Organization:** Open Football Compliance (OFC)  
**Document ID:** OFC-OFE-BORDEROU  
**Version:** 1.0.0  
**Status:** Proposed  
**Domain:** Match-level financial and attendance data  
**Initial application:** Observatório Financeiro dos Estaduais (OFE)  
**Last updated:** November 2026

---

## 1. Purpose

Este documento define o modelo canônico do OFC para estruturar informações financeiras e operacionais de partidas de futebol a partir de borderôs oficiais.

O padrão estabelece um contrato comum para identificação da partida, público, bilheteria, rubricas financeiras, distribuição da renda, totais declarados e proveniência documental. Seu objetivo é permitir análises consistentes sem eliminar os rótulos, valores e contextos presentes na fonte.

## 2. Scope

### 2.1 Initial document scope

A versão 1.0.0 tem como referência o modelo de borderô da Federação Pernambucana de Futebol (FPF) observado no documento de referência nº 21181. O documento utilizado é de uma partida do Campeonato Brasileiro Série B, disputada em Pernambuco, e serve para validar a estrutura documental da FPF — não como amostra de uma competição estadual.

O escopo inicial não pretende oferecer compatibilidade genérica com qualquer layout de relatório financeiro. A compatibilidade empírica com documentos de outras federações ainda não foi verificada e não é declarada nesta versão.

As diferenças tratadas nesta versão concentram-se em:
- nomenclatura dos campos e rubricas;
- presença ou ausência de informações;
- detalhamento e agrupamento de rubricas;
- convenções de preenchimento e significado das informações.

Uma variação que altere materialmente a estrutura documental de referência deverá ser registrada e avaliada antes de ser declarada compatível.

### 2.2 Included data

- Identificação da partida, competição, temporada e participantes.
- Estádio e capacidade utilizável, quando documentada.
- Público total, pagante e não pagante, além de categorias discriminadas.
- Linhas de ingressos: localização, modalidade, quantidades, preço e arrecadação.
- Rubricas de receita vinculadas à partida.
- Despesas operacionais.
- Tributos, taxas e outras deduções.
- Distribuição da renda líquida entre beneficiários, quando apresentada.
- Totais por seção original do borderô e totais financeiros declarados.
- Dados de coleta, extração, validação e evidência.

### 2.3 Exclusions

Este padrão não define demonstrações financeiras anuais dos clubes, contabilidade geral, receitas não atribuíveis à partida, folha salarial geral, contratos de transmissão, reconciliação bancária ou auditoria independente.

O padrão é específico para dados financeiros no nível de partida e não substitui o Open Football Accounting Standard (OFAS).

## 3. Normative principles

### 3.1 Preserve source information

O rótulo original, o valor original e a referência à fonte devem ser preservados. A normalização não pode sobrescrever o conteúdo original.

### 3.2 Separate data layers

Cada registro deve permitir distinguir:
1. **Original:** informação conforme apresentada na fonte.
2. **Normalized:** informação mapeada para o vocabulário e os campos canônicos.
3. **Derived:** valores calculados por regra documentada.
4. **Interpretation:** análise editorial ou conclusão do OFC.

### 3.3 Missing is not zero

Informação ausente deve ser representada como `null`. Zero só pode ser utilizado quando declarado pela fonte ou obtido por derivação documentada e validada.

### 3.4 No unsupported classification

Rubricas ambíguas ou sem mapeamento confiável devem permanecer não classificadas até revisão. Similaridade textual, isoladamente, não comprova equivalência semântica.

### 3.5 No double counting

Uma rubrica não pode integrar mais de uma classe financeira no mesmo cálculo. Totais declarados, totais por seção e somas de rubricas são preservados separadamente e não devem ser somados entre si.

## 4. Canonical record

O registro canônico de uma partida é composto pelos seguintes blocos:

| Block | Purpose |
|---|---|
| `schema_version` | Versão do contrato de dados |
| `match` | Identificação e contexto da partida |
| `documents` | Documento(s) oficial(is) e versões |
| `attendance` | Totais e categorias de público |
| `ticket_sales` | Disponibilidade, devoluções, vendas, preços e arrecadação por linha de ingresso |
| `revenue_distribution` | Rateio da renda líquida entre clubes ou beneficiários |
| `financial_items` | Rubricas financeiras individuais e seção original do documento |
| `financial_summary` | Totais declarados, totais por seção e valores calculados |
| `extraction_records` | Execuções de extração, revisão e validação |
| `evidence` | Referências às evidências no documento |
| `notes` | Observações e ressalvas do registro |

Uma partida pode estar associada a mais de um documento ou versão documental. Retificações devem ser registradas sem apagar o documento anterior.

## 5. Match

O bloco `match` identifica a partida.

| Field | Type | Requirement | Description |
|---|---|---|---|
| `match_id` | string | Required | Identificador único no sistema consumidor |
| `competition` | object | Required | Nome, organizador e contexto da competição |
| `season` | string | Required | Temporada |
| `stage` | string/null | Optional | Fase |
| `round` | string/null | Optional | Rodada |
| `match_date` | date/null | Optional | Data da partida |
| `match_time` | time/null | Optional | Horário local, quando disponível |
| `home_team` | object | Required | Clube mandante |
| `away_team` | object | Required | Clube visitante |
| `venue` | object/null | Optional | Estádio ou local |
| `match_status` | string/null | Optional | Situação da partida |

Os clubes são objetos com, no mínimo, `name`. Quando disponíveis, `normalized_name` e identificadores oficiais podem ser incluídos.

A competição deve preservar seu nome original e identificar o organizador quando conhecido. O tipo da competição deve permitir identificar o âmbito estadual ou nacional.

O bloco `venue` pode incluir nome, município, estado e país. A capacidade utilizável deve ser informada apenas com fonte e contexto que permitam relacioná-la à partida.

## 6. Documents

Cada elemento de `documents` descreve um documento-fonte.

| Field | Type | Requirement | Description |
|---|---|---|---|
| `document_id` | string | Required | Identificador do documento |
| `document_type` | string | Required | Tipo documental |
| `source_organization` | string/null | Optional | Federação ou entidade publicadora |
| `source_url` | string/null | Optional | URL da fonte original |
| `publication_date` | date/null | Optional | Data de publicação |
| `collection_timestamp` | date-time | Required | Data e hora da coleta |
| `original_filename` | string/null | Optional | Nome original do arquivo |
| `mime_type` | string/null | Optional | Tipo MIME |
| `file_hash` | string/null | Optional | SHA-256 do arquivo, quando calculado |
| `document_version` | string/null | Optional | Versão ou identificação de retificação |
| `official` | boolean | Required | Indica se a origem foi identificada como oficial |

Tipos documentais iniciais: `bordero`, `corrected_bordero`, `supporting_document` e `other`.

O documento original deve ser preservado sempre que legal e tecnicamente possível. Uma versão corrigida deve gerar novo registro documental e manter vínculo com a versão anterior por meio de identificador ou nota explícita.

## 7. Attendance

O bloco `attendance` contém os números de público informados no documento.

| Field | Type | Requirement | Description |
|---|---|---|---|
| `total_attendance` | integer/null | Optional | Público total |
| `paying_attendance` | integer/null | Optional | Público pagante |
| `non_paying_attendance` | integer/null | Optional | Público não pagante |
| `categories` | array | Optional | Categorias discriminadas |
| `notes` | string/null | Optional | Observações |

Cada categoria deve preservar `source_label`, podendo incluir `normalized_category` e `quantity`.

Não derivar público não pagante ou total sem registrar a fórmula e os valores de origem. Cortesias, gratuidades, credenciais e categorias similares devem manter o rótulo original; o enquadramento como pagante ou não pagante depende do significado documentado.

Ingressos vendidos não equivalem necessariamente a público pagante ou público presente.

## 8. Ticket sales

O bloco `ticket_sales` representa cada linha da tabela de ingressos do borderô. Cada linha deve preservar:
- `ticket_line_id`: identificador único da linha;
- `document_id`: documento de origem;
- `source_label`: descrição integral apresentada na coluna de localização/modalidade;
- `sector`: setor ou localização, quando separável com segurança;
- `ticket_type`: tipo de ingresso, por exemplo inteira ou meia, quando identificável;
- `admission_category`: categoria como sócio, credenciamento ou gratuidade, quando identificável;
- `available_quantity`, `returned_quantity` e `sold_quantity`;
- `unit_price_minor` e `proceeds_minor`, em centavos de BRL;
- `currency` e `evidence_id`.

Quantidades e arrecadação devem ser preservadas como declaradas. Linhas com preço zero permanecem no detalhamento. A soma da arrecadação por linha deve ser comparada ao total da tabela, gerando divergência quando não fechar. A soma de ingressos vendidos não deve preencher automaticamente campos de público.

## 9. Revenue distribution

O bloco `revenue_distribution` representa a distribuição da renda líquida declarada entre clubes ou outros beneficiários. Cada registro pode conter:
- `distribution_id` e `document_id`;
- `beneficiary_name` e `beneficiary_tax_id`, quando disponível;
- `share_percentage`;
- `discount_minor`;
- `net_payable_minor`;
- `currency` e `evidence_id`.

A distribuição não altera retroativamente a receita bruta nem as despesas da partida. Os valores devem ser preservados como declarados e não devem ser confundidos com receita reconhecida contabilmente pelo clube. A soma dos percentuais e dos valores líquidos deve ser verificada contra o total distribuído, mas divergências devem ser registradas, não corrigidas automaticamente.

## 10. Financial items

Cada rubrica individual deve ser representada em `financial_items`.

| Field | Type | Requirement | Description |
|---|---|---|---|
| `item_id` | string | Required | Identificador do item no registro |
| `document_id` | string | Required | Documento de origem |
| `source_label` | string | Required | Rótulo original |
| `source_section` | string/null | Optional | Seção original do borderô, por exemplo B1, B2 ou B3 |
| `normalized_label` | string/null | Optional | Rótulo normalizado |
| `financial_class` | string | Required | Classe financeira |
| `canonical_category` | string/null | Optional | Código do catálogo OFC |
| `amount_minor` | integer | Required | Valor em centavos inteiros |
| `currency` | string | Required | Código ISO 4217; BRL no escopo inicial |
| `accounting_role` | string | Required | Papel no cálculo financeiro |
| `evidence_id` | string/null | Optional | Evidência associada |
| `classification_status` | string | Required | Situação da classificação |
| `notes` | string/null | Optional | Justificativa ou ressalva |

Valores permitidos para `financial_class`: `revenue`, `operating_expense`, `tax`, `fee`, `deduction`, `adjustment`, `other` e `unknown`.

Valores permitidos para `accounting_role`: `gross_revenue_component`, `operating_expense_component`, `tax_component`, `fee_component`, `deduction_component`, `adjustment_component`, `informational_only` e `unclassified`.

`source_section` preserva a organização visual do documento e não determina a classificação financeira. A classe descreve a natureza da rubrica; o papel indica se e como ela participa dos totais metodológicos. Uma rubrica apresentada em B3, por exemplo, não é automaticamente uma despesa operacional se sua natureza for tributária ou permanecer ambígua.

Valores monetários são representados em centavos inteiros de BRL. Os valores são armazenados como magnitudes não negativas; sua natureza e seu efeito no cálculo são determinados por `financial_class` e `accounting_role`. A fonte original deve continuar disponível na evidência.

Uma rubrica não mapeada deve utilizar `financial_class: unknown`, `accounting_role: unclassified` e `canonical_category: null`. Rubricas desconhecidas ou ambíguas não entram automaticamente nos totais metodológicos.

## 11. Financial summary

O bloco `financial_summary` preserva totais declarados pela fonte, totais por seção original e valores calculados pelo processo de normalização.

### 11.1 Declared totals

O objeto `declared` pode conter `gross_revenue_minor`, `operating_expenses_minor`, `taxes_minor`, `fees_minor`, `deductions_minor`, `adjustments_minor` e `net_revenue_minor`. Cada valor é inteiro em centavos ou `null). Deve refletir o total declarado, sem reconstrução silenciosa.

### 11.2 Declared source-section totals

O objeto `declared_source_sections` preserva os subtotais impressos nas seções originais do documento:
- `b1_minor`: total declarado na seção B1;
- `b2_minor`: total declarado na seção B2;
- `b3_minor`: total declarado na seção B3;
- `total_expenses_minor`: total declarado das despesas.

Esses valores descrevem a estrutura da fonte e não equivalem automaticamente aos totais por classe financeira do OFC.

### 11.3 Calculated totals

O objeto `calculated` pode conter os mesmos campos financeiros, calculados a partir de rubricas individuais classificadas e validadas.

A soma de rubricas só pode ser apresentada como total calculado quando os componentes necessários estiverem suficientemente completos. Ausência de rubrica não significa valor zero. Se uma rubrica material permanecer não classificada, os totais metodológicos afetados devem permanecer `null` ou ser explicitamente identificados como parciais, sem serem apresentados como completos.

### 11.4 Calculation status

Valores iniciais: `not_calculated`, `complete`, `partial` e `not_comparable`.

Diferenças entre totais declarados, totais por seção e calculados devem ser registradas em `difference_notes`. Não substituir um pelo outro.

O resultado líquido metodológico do OFE é derivado conforme o OFE Financial Indicators Dictionary, considerando receita bruta, despesas operacionais, tributos, taxas, outras deduções incluídas e ajustes validados. Ele não deve ser confundido com a renda líquida declarada pela fonte.

## 12. Extraction records

Cada execução de extração ou revisão deve ser registrada em `extraction_records`.

Campos principais:
- `extraction_id`, `document_id`;
- `method`: `manual`, `ocr`, `automated` ou `hybrid`;
- `tool_name` e `model_name`, quando aplicáveis;
- `extracted_at` em formato date-time;
- `pipeline_version`;
- `review_status`: `pending`, `reviewed`, `approved` ou `rejected`;
- `validation_status`: `not_validated`, `valid`, `valid_with_warnings` ou `invalid`;
- `extraction_confidence`, quando disponível, entre 0 e 1;
- `notes`.

Confiança de extração, confiança de classificação, validação estrutural e revisão humana são dimensões distintas.

## 13. Evidence and provenance

O bloco `evidence` registra a origem de informações extraídas. Cada evidência deve conter:
- `evidence_id`, `document_id` e `evidence_type`;
- `page_number`, quando aplicável;
- `bounding_box`, quando disponível;
- `source_text`, `extracted_value` e `notes`.

O `bounding_box` deve usar coordenadas normalizadas entre 0 e 1, relativas à página. A evidência deve apontar para o documento e, quando possível, para a região específica que sustenta o campo ou rubrica.

Dados críticos sem evidência localizável devem possuir justificativa explícita. Correções manuais devem ser registradas.

## 14. Normalization and mapping

A normalização deve utilizar o catálogo de categorias financeiras do OFC e preservar o rótulo original.

O mapeamento entre rótulos da fonte e categorias canônicas deve considerar o rótulo original, a categoria e classe canônicas, o papel contábil, a versão do catálogo, a situação da classificação e a justificativa ou evidência quando houver ambiguidade.

A primeira versão considera um modelo documental de referência observado em documentos da FPF. Não se presume compatibilidade com layouts de outras federações sem validação empírica. Não se presume equivalência semântica apenas porque dois campos ocupam posição semelhante no documento.

## 15. Validation rules

### 15.1 Structural

- Todos os campos obrigatórios devem estar presentes.
- Datas e timestamps devem respeitar ISO 8601.
- Moeda deve utilizar código ISO 4217.
- Valores monetários devem ser inteiros em centavos.
- Referências a documentos e evidências devem apontar para registros existentes.
- Identificadores dentro do registro devem ser únicos.

### 15.2 Attendance and ticket sales

- Quantidades devem ser inteiros não negativos.
- Público pagante não deve exceder público total sem inconsistência explicitamente registrada.
- Soma das categorias deve ser comparada aos totais declarados.
- Quantidades de ingressos vendidos não podem ser assumidas como público presente.
- Soma de arrecadação das linhas de ingresso deve ser comparada ao total declarado da tabela.

### 15.3 Financial

- Valores monetários devem ser inteiros não negativos em centavos, exceto ajustes com regra explícita.
- Classe, papel contábil e categoria devem ser compatíveis com o catálogo.
- Uma rubrica não pode ser contada mais de uma vez no mesmo total.
- Totais declarados, totais por seção e calculados devem permanecer separados.
- Diferenças devem gerar aviso ou erro, conforme a regra de validação.
- Rubricas desconhecidas não entram automaticamente nos totais metodológicos.
- Ausência de informação não pode ser tratada como zero sem evidência ou regra de derivação válida.

### 15.4 Revenue distribution

- Percentuais devem estar entre 0 e 100.
- Valores de distribuição devem ser comparados à renda líquida declarada.
- Diferenças não devem ser corrigidas automaticamente.

### 15.5 Provenance and document versions

- Todo documento deve possuir identificador.
- Documentos oficiais devem ter origem identificada ou justificativa explícita para sua classificação.
- Hash SHA-256 deve conter 64 caracteres hexadecimais quando informado.
- Versões retificadas devem preservar a versão anterior.
- Alterações manuais devem ser registradas.

## 16. Conformance

Uma implementação declara conformidade com o OFC Borderô Data Standard v1.0.0 quando produz o registro canônico, preserva rótulos e valores originais, representa valores monetários em centavos inteiros, distingue totais declarados e calculados, aplica classes sem dupla contagem, representa ausências como `null`, preserva rastreabilidade e registra as versões do padrão e do catálogo.

Conformidade estrutural não certifica a veracidade contábil da fonte nem garante que todos os indicadores sejam elegíveis.

## 17. Validation basis and limitations

A revisão empírica desta versão utilizou o Boletim Financeiro FPF nº 21181, de duas páginas, referente a Náutico x Sport, pelo Campeonato Brasileiro Série B, em 26/09/2026. O documento foi utilizado para examinar a estrutura do borderô da FPF, incluindo identificação da partida, tabela de ingressos, seções B1/B2/B3 e divisão da renda líquida.

A amostra não é uma partida de competição estadual e não comprova, por si só, a compatibilidade com todos os documentos da FPF ou com documentos de outras federações. A validação com outras federações permanece pendente e não bloqueia a publicação inicial do padrão, desde que essa limitação seja divulgada.

## 18. Related documents

- `ofe-scope.md` — escopo do Observatório Financeiro dos Estaduais.
- `financial-indicators-dictionary.md` — fórmulas, definições e elegibilidade dos indicadores.
- `schemas/bordero.schema.json` — JSON Schema do contrato.
- `catalogs/financial-categories.json` — catálogo de classes e categorias.
- `examples/match-example.json` — exemplo de registro canônico.

## 19. Version history

| Version | Date | Description |
|---|---|---|
| 0.1 | November 2026 | Initial canonical data model |
| 1.0.0 | November 2026 | Restricted initial document scope; added ticket sales and revenue distribution; preserved original source sections and documented empirical validation basis and limitations |
