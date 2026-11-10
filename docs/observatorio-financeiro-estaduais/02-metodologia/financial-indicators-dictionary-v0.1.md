# OFC Financial Indicators Dictionary

**Organization:** Open Football Compliance (OFC)  
**Document ID:** OFC-OFE-INDICATORS  
**Version:** 0.1  
**Status:** Draft  
**Initial application:** Observatório Financeiro dos Estaduais (OFE)  
**Currency:** Brazilian Real (BRL)  
**Last updated:** November 2026

---

## 1. Purpose

Este documento estabelece as definições, fórmulas, unidades, condições de cálculo e limitações dos indicadores financeiros e operacionais utilizados pelo Observatório Financeiro dos Estaduais (OFE).

Seu objetivo é assegurar que os indicadores publicados pelo OFC sejam reproduzíveis, rastreáveis e comparáveis, evitando interpretações inconsistentes entre partidas, competições, federações e temporadas.

Os indicadores devem ser calculados a partir dos dados normalizados segundo o OFC Borderô Data Standard, respeitando as regras de elegibilidade e validação definidas neste documento.

## 2. General calculation principles

### 2.1 Source of information

A fonte prioritária é o borderô oficial da partida.

Os valores originais devem ser preservados. Valores normalizados e derivados devem manter vínculo com suas respectivas fontes e transformações.

### 2.2 Missing values

A ausência de informação deve ser representada como `null`.

Valores ausentes não podem ser tratados automaticamente como zero.

Um valor zero somente deve ser considerado válido quando declarado na fonte ou obtido por derivação explicitamente autorizada pela metodologia.

### 2.3 Monetary precision

Valores monetários devem ser armazenados com precisão decimal exata, preferencialmente em centavos.

O arredondamento deve ocorrer apenas na apresentação dos resultados, nunca durante os cálculos intermediários.

### 2.4 Denominator validation

Quando o denominador de um indicador for zero, negativo ou ausente, o indicador não deve ser calculado.

O resultado deve ser `null`, acompanhado do motivo de inelegibilidade.

### 2.5 Indicator-specific eligibility

A elegibilidade deve ser avaliada individualmente para cada indicador.

A ausência de um campo não implica automaticamente a exclusão da partida de todas as análises.

### 2.6 Aggregation

Indicadores expressos como razões ou percentuais devem, como regra, ser calculados sobre os totais agregados elegíveis, e não pela média aritmética simples dos indicadores individuais.

A quantidade de partidas elegíveis deve ser informada em cada agregação.

### 2.7 Interpretation

Indicadores calculados representam relações entre valores documentados ou derivados segundo a metodologia do OFE.

Não devem ser interpretados como demonstrações contábeis completas ou como confirmação independente da movimentação financeira efetiva dos clubes.

---

## 3. Indicator classification

Os indicadores são organizados em cinco grupos:

| Group | Description |
|---|---|
| Revenue | Receitas vinculadas à partida |
| Operational costs | Despesas operacionais e custos do evento |
| Financial result | Resultado financeiro e retenção de receita |
| Attendance | Público, participação e ocupação |
| Estimates | Indicadores estimados e análises condicionais |

## 4. Revenue indicators

### 4.1 Gross Match Revenue

**Code:** `OFE-REV-001`

**Definition:** Total de receita bruta vinculada à partida, conforme declarado no borderô oficial e interpretado segundo as regras de normalização do OFC.

**Formula:**

Valor de receita bruta declarado no documento oficial, ou soma de rubricas explicitamente definidas como componentes dessa receita pela metodologia.

**Unit:** BRL.

**Required fields:**
- Gross revenue.
- Source document and evidence.

**Interpretation:** Representa a receita bruta atribuída à partida segundo o documento de origem e as regras adotadas pelo OFE.

**Limitations:**
- A composição da receita pode variar entre federações.
- Receitas de associados, ingressos e outras categorias podem receber tratamentos distintos.
- Não incluir receitas gerais do clube que não estejam vinculadas à partida.

### 4.2 Gross Revenue per Paying Attendee

**Code:** `OFE-REV-002`

**Definition:** Receita bruta da partida dividida pelo público pagante declarado.

**Formula:**

`Gross Match Revenue / Paying Attendance`

**Unit:** BRL per paying attendee.

**Required fields:**
- Gross revenue.
- Paying attendance greater than zero.

**Interpretation:** Representa a receita bruta média atribuída a cada pagante.

**Limitations:**
- Não corresponde necessariamente ao preço efetivamente pago por ingresso.
- Pode incorporar diferentes categorias de ingressos e receitas vinculadas à bilheteria.
- A comparação exige definições equivalentes de receita e público pagante.

**Publication label:** Receita bruta por pagante.

## 5. Operational cost indicators

### 5.1 Match Operating Expenses

**Code:** `OFE-CST-001`

**Definition:** Soma das rubricas financeiras classificadas pelo OFC como despesas operacionais diretamente relacionadas à realização da partida.

**Formula:**

`Σ Operating Expense Items`

**Unit:** BRL.

**Required fields:**
- Financial line items.
- Canonical expense categories.
- Validated classification.

**Examples of categories:**
- Security.
- Cleaning.
- Medical services.
- Ambulance.
- VAR and match operations.
- Other operational services.

**Limitations:**
- A composição depende das rubricas efetivamente discriminadas no borderô.
- Taxas, tributos e deduções não devem ser incluídos automaticamente.
- Uma mesma rubrica não pode ser contabilizada em mais de uma categoria.

### 5.2 Operating Expense per Attendee

**Code:** `OFE-CST-002`

**Definition:** Despesa operacional da partida dividida pelo público total presente.

**Formula:**

`Match Operating Expenses / Total Attendance`

**Unit:** BRL per attendee.

**Required fields:**
- Match operating expenses.
- Total attendance greater than zero.

**Interpretation:** Estima o custo operacional documentado por pessoa presente na partida.

**Limitations:**
- Depende da consistência da contagem de público.
- A abrangência das despesas operacionais pode variar entre borderôs.
- Não representa necessariamente o custo econômico integral da realização do evento.

**Publication label:** Despesa operacional por torcedor.

## 6. Financial result indicators

### 6.1 Reported Net Revenue

**Code:** `OFE-RES-001`

**Definition:** Resultado líquido declarado diretamente no borderô oficial.

**Formula:**

Valor informado no campo de receita líquida ou resultado líquido do documento.

**Unit:** BRL.

**Required fields:**
- Reported net revenue.
- Source document and evidence.

**Interpretation:** Valor declarado pela fonte oficial, preservado independentemente do resultado recalculado pelo OFE.

**Limitations:**
- A definição de receita líquida pode variar entre documentos.
- O valor não deve ser tratado automaticamente como receita efetivamente recebida pelo clube.
- Divergências em relação ao cálculo metodológico devem ser registradas.

### 6.2 Methodological Net Match Result

**Code:** `OFE-RES-002`

**Definition:** Resultado financeiro calculado pelo OFE após a dedução das despesas operacionais e demais deduções reconhecidas na metodologia.

**Formula:**

`Gross Match Revenue - Match Operating Expenses - Included Deductions`

**Unit:** BRL.

**Required fields:**
- Gross revenue.
- Operating expenses.
- Included deductions.
- Validated financial classification.

**Interpretation:** Resultado calculado segundo a metodologia do OFE, considerando as receitas, despesas e deduções identificadas no borderô.

**Limitations:**
- Não representa necessariamente o valor que ingressou integralmente no caixa do clube.
- Depende da correta classificação das rubricas.
- Não deve haver dupla contagem entre despesas, taxas e deduções.
- Divergências com o resultado líquido declarado devem ser preservadas e sinalizadas.

### 6.3 Revenue Retention Margin

**Code:** `OFE-RES-003`

**Definition:** Proporção da receita bruta que permanece após as despesas operacionais e deduções consideradas pela metodologia do OFE.

**Formula:**

`Methodological Net Match Result / Gross Match Revenue × 100`

**Unit:** Percentage (%).

**Required fields:**
- Methodological net match result.
- Gross revenue greater than zero.

**Interpretation:** Mede a parcela percentual da receita bruta que permanece após os componentes considerados no cálculo metodológico.

**Limitations:**
- É sensível à composição das despesas e deduções.
- Não deve ser comparada quando as regras de classificação forem diferentes.
- Pode apresentar valores negativos quando despesas e deduções superarem a receita bruta.

**Publication label:** Margem de retenção.

## 7. Financial burden indicators

### 7.1 Taxes and Fees Burden

**Code:** `OFE-FEE-001`

**Definition:** Participação de tributos, taxas e encargos selecionados sobre a receita bruta da partida.

**Formula:**

`(Taxes + Included Fees) / Gross Match Revenue × 100`

**Unit:** Percentage (%).

**Required fields:**
- Gross revenue greater than zero.
- Tax and fee line items.
- Validated classification.

**Interpretation:** Indica a proporção da receita bruta destinada às rubricas classificadas como tributos e taxas pela metodologia.

**Limitations:**
- A composição da cesta de rubricas deve ser explicitada.
- Não incluir despesas operacionais nessa cesta.
- Comparações dependem da equivalência das rubricas consideradas.

## 8. Attendance indicators

### 8.1 Total Attendance

**Code:** `OFE-ATT-001`

**Definition:** Quantidade total de pessoas presentes na partida, conforme declarado no borderô oficial.

**Formula:**

Valor total declarado no documento.

Quando o total não estiver disponível, a soma de pagantes e não pagantes somente poderá ser utilizada se ambos estiverem disponíveis, forem compatíveis e a metodologia autorizar a derivação.

**Unit:** People.

**Required fields:**
- Total attendance, or validated attendance components.

**Limitations:**
- Os critérios de contagem podem variar entre federações.
- Valores derivados devem ser identificados como tais.

### 8.2 Non-Paying Attendance Share

**Code:** `OFE-ATT-002`

**Definition:** Proporção do público total classificada como não pagante.

**Formula:**

`(Total Attendance - Paying Attendance) / Total Attendance × 100`

**Unit:** Percentage (%).

**Required fields:**
- Total attendance greater than zero.
- Paying attendance.
- Compatible attendance definitions.

**Interpretation:** Mede a participação de público não pagante no total de pessoas presentes.

**Limitations:**
- Cortesias, gratuidades, credenciais e outras categorias podem variar entre documentos.
- Não representa taxa de ocupação do estádio.

**Publication label:** Participação de público não pagante.

### 8.3 Stadium Occupancy Rate

**Code:** `OFE-ATT-003`

**Definition:** Proporção da capacidade utilizável do estádio ocupada pelo público total da partida.

**Formula:**

`Total Attendance / Usable Stadium Capacity × 100`

**Unit:** Percentage (%).

**Required fields:**
- Total attendance.
- Usable stadium capacity greater than zero.
- Reliable source for stadium capacity and match configuration.

**Interpretation:** Indica a utilização da capacidade disponibilizada para a partida.

**Limitations:**
- Capacidade nominal do estádio não deve ser confundida com capacidade utilizável.
- Interdições, obras, restrições de setores e sanções podem alterar a capacidade efetivamente disponível.
- A fonte e a data de referência da capacidade devem ser registradas.

## 9. Estimated indicators

### 9.1 Estimated Ticketing Break-even

**Code:** `OFE-EST-001`

**Definition:** Estimativa da quantidade de pagantes necessária para atingir um resultado de equilíbrio financeiro, considerando hipóteses explícitas sobre custos e receitas.

**Conceptual formula:**

`(Attributable Fixed Costs - Other Attributable Revenue) / Net Average Revenue per Paying Attendee`

**Unit:** Paying attendees.

**Required fields:**
- Attributable fixed costs.
- Other attributable revenue, when applicable.
- Net average revenue per paying attendee.
- Documented calculation assumptions.

**Interpretation:** Estimativa de público pagante necessário para atingir o equilíbrio sob as hipóteses adotadas.

**Limitations:**
- Não é um valor diretamente observado no borderô.
- Exige separação entre custos fixos e variáveis.
- Exige identificação de receitas não provenientes de ingressos.
- Deve ser apresentado como estimativa, nunca como dado oficial.

**Publication rule:** Não publicar enquanto os componentes necessários não forem identificáveis e validados.

## 10. Indicator eligibility

A elegibilidade deve ser avaliada individualmente.

| Missing or inconsistent information | Affected indicators |
|---|---|
| Gross revenue | Revenue per paying attendee, financial burden, methodological net result and retention margin |
| Operating expenses | Operating expenses per attendee and methodological net result |
| Paying attendance | Revenue per paying attendee and non-paying attendance share |
| Total attendance | Operating expenses per attendee, non-paying attendance share and occupancy |
| Stadium capacity | Occupancy rate |
| Taxes and fees | Taxes and fees burden |
| Fixed costs or other attributable revenue | Estimated ticketing break-even |

A ausência de um campo secundário não deve invalidar indicadores que não dependam dele.

Quando houver inconsistência não resolvida, o indicador afetado deve ser marcado como inelegível.

## 11. Aggregation methodology

### 11.1 General rule

Para indicadores expressos como razões ou percentuais, a agregação padrão utiliza a soma dos numeradores dividida pela soma dos denominadores elegíveis.

A média simples dos resultados individuais não deve ser utilizada como substituta dessa regra.

### 11.2 Competition-level indicators

| Indicator | Aggregation formula |
|---|---|
| Gross revenue | Σ Gross Match Revenue |
| Operating expenses | Σ Match Operating Expenses |
| Methodological net result | Σ Methodological Net Match Result |
| Revenue retention margin | Σ Methodological Net Match Result / Σ Gross Match Revenue × 100 |
| Operating expense per attendee | Σ Operating Expenses / Σ Total Attendance |
| Revenue per paying attendee | Σ Gross Revenue / Σ Paying Attendance |
| Non-paying attendance share | Σ Non-Paying Attendance / Σ Total Attendance × 100 |

Somente partidas elegíveis para o indicador correspondente devem participar do cálculo.

### 11.3 Coverage disclosure

Toda publicação agregada deve informar:

- Total de partidas da competição.
- Número de documentos oficiais encontrados.
- Número de partidas com dados validados.
- Número de partidas elegíveis para cada indicador.
- Critérios de exclusão e limitações relevantes.

## 12. Illustrative calculation example

Os dados abaixo são hipotéticos e servem apenas para demonstrar as fórmulas.

**Match data:**

| Field | Value |
|---|---:|
| Gross revenue | R$ 500,000.00 |
| Operating expenses | R$ 160,000.00 |
| Included deductions | R$ 40,000.00 |
| Paying attendance | 10,000 |
| Non-paying attendance | 1,000 |
| Total attendance | 11,000 |
| Usable stadium capacity | 20,000 |

**Calculated indicators:**

| Indicator | Calculation | Result |
|---|---|---:|
| Methodological net result | 500,000 - 160,000 - 40,000 | R$ 300,000.00 |
| Revenue retention margin | 300,000 / 500,000 × 100 | 60.0% |
| Operating expense per attendee | 160,000 / 11,000 | R$ 14.55 |
| Gross revenue per paying attendee | 500,000 / 10,000 | R$ 50.00 |
| Non-paying attendance share | 1,000 / 11,000 × 100 | 9.1% |
| Stadium occupancy rate | 11,000 / 20,000 × 100 | 55.0% |

## 13. Publication requirements

Toda publicação que apresentar indicadores do OFE deve informar, quando aplicável:

- Código e nome do indicador.
- Definição e fórmula.
- Unidade de medida.
- Período e competição analisados.
- Número de partidas elegíveis.
- Cobertura documental.
- Versão do dicionário metodológico.
- Limitações e ressalvas relevantes.

Alterações em fórmulas, escopo ou regras de elegibilidade devem ser versionadas e documentadas.

Mudanças que afetem a comparabilidade histórica devem ser explicitamente identificadas.

## 14. Pending methodological decisions

Os seguintes pontos exigem validação antes da aprovação normativa:

1. Aprovar a taxonomia de despesas operacionais.
2. Definir a cesta de tributos, taxas e deduções.
3. Definir o tratamento de receitas de associados e outras receitas vinculadas à partida.
4. Definir critérios para cortesias, gratuidades e credenciais.
5. Estabelecer fontes oficiais para capacidade utilizável dos estádios.
6. Definir o tratamento de divergências entre resultado líquido declarado e resultado metodológico.
7. Validar as fórmulas com borderôs de diferentes federações.

## 15. Related documents

- `ofe-scope.md` — escopo institucional e operacional do OFE.
- `bordero-data-standard-v0.1.md` — contrato canônico de dados de borderôs.
- `bordero-v0.1.schema.json` — schema de validação dos dados.
- `financial-categories-v0.1.json` — catálogo inicial de categorias financeiras.

## 16. Version history

| Version | Date | Description |
|---|---|---|
| 0.1 | November 2026 | Initial indicator definitions and calculation methodology |