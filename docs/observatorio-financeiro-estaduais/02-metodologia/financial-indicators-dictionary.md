# OFC Financial Indicators Dictionary

**Organization:** Open Football Compliance (OFC)  
**Document ID:** OFC-OFE-INDICATORS  
**Version:** 1.0.0  
**Status:** Proposed  
**Initial application:** Observatório Financeiro dos Estaduais (OFE)  
**Currency:** Brazilian Real (BRL)  
**Last updated:** November 2026

---

## 1. Purpose and scope

Este documento define os indicadores financeiros e operacionais do Observatório Financeiro dos Estaduais (OFE), incluindo suas definições, fórmulas, unidades, requisitos de dados, regras de elegibilidade, agregação e limitações.

Os indicadores são calculados a partir de dados normalizados segundo o OFC Borderô Data Standard. O dicionário aplica-se às partidas de competições estaduais profissionais masculinas e femininas abrangidas pelo OFE.

Este documento não constitui um padrão de demonstrações contábeis dos clubes e não substitui o Open Football Accounting Standard (OFAS).

## 2. General calculation principles

### 2.1 Source hierarchy and traceability

O borderô ou documento financeiro oficial da partida é a fonte primária. Fontes complementares podem fornecer contexto, como capacidade utilizável do estádio, mas devem ser identificadas separadamente.

Valores originais, valores normalizados e valores derivados devem permanecer distinguíveis e rastreáveis à fonte e à regra de transformação utilizada.

### 2.2 Missing values and zero

Informação ausente deve ser representada como `null`, nunca presumida como zero.

Zero é um valor válido quando explicitamente informado pela fonte ou obtido por derivação autorizada, documentada e verificável.

### 2.3 Monetary precision

Valores monetários devem ser armazenados em centavos inteiros de BRL no modelo canônico. Cálculos devem utilizar aritmética exata, sem arredondamentos intermediários. O arredondamento ocorre apenas na apresentação, para duas casas decimais.

### 2.4 Denominators

Se o denominador estiver ausente ou for igual a zero, o indicador não será calculado e deverá retornar `null`, acompanhado do motivo de inelegibilidade. Denominadores negativos também tornam o indicador inelegível, salvo regra específica documentada.

### 2.5 Indicator-specific eligibility

A elegibilidade é avaliada individualmente para cada indicador. A ausência de um campo não exclui automaticamente a partida de todas as análises.

### 2.6 Aggregation

Para razões e percentuais agregados, a regra padrão é dividir a soma dos numeradores elegíveis pela soma dos denominadores correspondentes. Não utilizar a média aritmética simples dos indicadores individuais como substituta dessa regra.

Toda agregação deve informar o número de partidas elegíveis.

### 2.7 Interpretation

Os indicadores representam relações entre valores documentados ou derivados conforme esta metodologia. Não constituem auditoria independente, demonstração contábil completa ou confirmação de recebimento efetivo de recursos pelo clube.

## 3. Financial classification policy

Cada rubrica financeira deve preservar sua descrição original e receber uma classificação normalizada, conforme o catálogo de categorias financeiras do OFC.

As classes são distintas:

| Class | Tratamento metodológico |
|---|---|
| `revenue` | Componentes que integram a receita bruta da partida |
| `operating_expense` | Custos operacionais diretamente relacionados à realização da partida |
| `tax` | Tributos e encargos fiscais |
| `fee` | Taxas administrativas, federativas ou institucionais |
| `deduction` | Outras deduções da receita que não sejam despesas operacionais, tributos ou taxas |
| `adjustment` | Ajustes, correções, repasses ou transferências com efeito financeiro identificado |
| `other` | Rubricas conhecidas sem enquadramento nas classes anteriores |
| `unknown` | Rubricas cuja natureza não pôde ser identificada com segurança |

### 3.1 No double counting

Uma rubrica não pode compor mais de uma classe de dedução no mesmo cálculo.

A classificação deve considerar a natureza econômica e o papel da rubrica no documento, não apenas seu rótulo. Termos como “taxa”, “despesa”, “repasse” ou “retenção” não são suficientes, isoladamente, para determinar o tratamento.

### 3.2 Unclassified items

Rubricas classificadas como `unknown` ou `other` não entram automaticamente nos cálculos de despesas, tributos, taxas ou deduções. Seu tratamento deve ser resolvido por revisão documentada antes de sua inclusão em um indicador afetado.

### 3.3 Adjustments

Ajustes só podem afetar o resultado metodológico quando sua natureza, sinal e efeito sobre o resultado estiverem documentados e validados. Ajustes sem tratamento inequívoco permanecem fora do cálculo e devem ser sinalizados.

## 4. Indicator classification

| Group | Description |
|---|---|
| Revenue | Receitas vinculadas à partida |
| Operational costs | Despesas operacionais da partida |
| Financial result | Resultados e retenção de receita |
| Financial burden | Tributos e taxas |
| Attendance | Público e ocupação |
| Estimates | Indicadores estimados e condicionais |

## 5. Revenue indicators

### 5.1 Gross Match Revenue

**Code:** `OFE-REV-001`  
**Definition:** Receita bruta total vinculada à partida, conforme declarada no documento oficial ou calculada pela soma das rubricas classificadas como componentes de receita bruta, quando a metodologia permitir essa derivação.  
**Formula:** Valor total declarado como receita bruta; na ausência de total declarado, soma dos itens com papel `gross_revenue_component`, desde que todos os componentes relevantes estejam disponíveis e validados.  
**Unit:** BRL.  
**Required data:** Total de receita bruta declarado ou rubricas de receita bruta classificadas e validadas.  
**Interpretation:** Valor bruto atribuído à partida segundo o documento e as regras de normalização do OFE.  
**Limitations:** A composição da receita pode variar entre documentos. Receitas gerais do clube não vinculadas à partida ficam excluídas. Receitas de bilheteria, associados e outras fontes devem permanecer identificáveis quando discriminadas.

### 5.2 Gross Revenue per Paying Attendee

**Code:** `OFE-REV-002`  
**Definition:** Receita bruta da partida dividida pelo público pagante.  
**Formula:** `Gross Match Revenue / Paying Attendance`  
**Unit:** BRL por pagante.  
**Required data:** Receita bruta elegível e público pagante maior que zero.  
**Interpretation:** Receita bruta atribuída, em média, a cada pagante.  
**Limitations:** Não equivale necessariamente ao preço médio do ingresso. Pode incluir outras receitas vinculadas à partida. Comparações exigem definições equivalentes de receita e público.  
**Publication label:** Receita bruta por pagante.

## 6. Operational cost indicators

### 6.1 Match Operating Expenses

**Code:** `OFE-CST-001`  
**Definition:** Soma das rubricas classificadas como despesas operacionais diretamente relacionadas à realização da partida.  
**Formula:** `Σ Operating Expense Items`  
**Unit:** BRL.  
**Required data:** Rubricas financeiras, categorias canônicas e classificação validada.  
**Examples:** Segurança, limpeza, serviços médicos, ambulância, VAR, operação do estádio, pessoal e logística da partida.  
**Limitations:** Tributos, taxas e outras deduções não integram este indicador. A abrangência depende das rubricas discriminadas no documento. Não representa necessariamente o custo econômico integral do evento.

### 6.2 Operating Expense per Attendee

**Code:** `OFE-CST-002`  
**Definition:** Despesa operacional da partida dividida pelo público total.  
**Formula:** `Match Operating Expenses / Total Attendance`  
**Unit:** BRL por pessoa presente.  
**Required data:** Despesas operacionais elegíveis e público total maior que zero.  
**Interpretation:** Despesa operacional documentada por pessoa presente.  
**Limitations:** Depende da consistência da contagem de público e da abrangência das despesas discriminadas.  
**Publication label:** Despesa operacional por torcedor.

## 7. Financial result indicators

### 7.1 Reported Net Revenue

**Code:** `OFE-RES-001`  
**Definition:** Valor identificado no documento oficial como renda líquida, receita líquida ou resultado líquido declarado.  
**Formula:** Valor declarado pela fonte, preservado sem substituição pelo cálculo metodológico.  
**Unit:** BRL.  
**Required data:** Valor declarado e evidência documental.  
**Interpretation:** Resultado informado pela entidade emissora do documento.  
**Limitations:** A composição pode variar entre federações e documentos. Não deve ser tratado automaticamente como valor recebido pelo clube ou como equivalente ao resultado metodológico do OFE.

### 7.2 Methodological Net Match Result

**Code:** `OFE-RES-002`  
**Definition:** Resultado calculado pelo OFE a partir da receita bruta, deduzindo separadamente despesas operacionais, tributos, taxas e outras deduções elegíveis.  
**Formula:**

`Gross Match Revenue - Operating Expenses - Taxes - Fees - Other Included Deductions +/- Validated Adjustments`

**Unit:** BRL.  
**Required data:** Receita bruta; despesas operacionais; tributos; taxas; outras deduções incluídas; classificação validada; e ajustes, quando aplicáveis.  
**Interpretation:** Resultado padronizado calculado segundo as classes e regras deste dicionário.  
**Limitations:**
- Cada rubrica só pode ser considerada uma vez.
- Classes ausentes não podem ser presumidas como zero quando a documentação não permite confirmar sua inexistência.
- Ajustes só entram quando validados e com efeito identificado.
- O resultado não representa necessariamente o valor que ingressou no caixa do clube.
- Se uma classe relevante estiver incompleta ou sem classificação confiável, o indicador será inelegível ou deverá ser publicado com ressalva explícita, conforme a regra de validação aplicável.

### 7.3 Revenue Retention Margin

**Code:** `OFE-RES-003`  
**Definition:** Proporção da receita bruta que permanece após as despesas operacionais, tributos, taxas e outras deduções consideradas no resultado líquido metodológico.  
**Formula:**

`Methodological Net Match Result / Gross Match Revenue × 100`

**Unit:** Percentual (%).  
**Required data:** Resultado líquido metodológico elegível e receita bruta maior que zero.  
**Interpretation:** Mede a parcela da receita bruta remanescente após os componentes incluídos no cálculo metodológico do OFE.  
**Limitations:** Depende da completude e da classificação consistente das rubricas. Pode ser negativa quando os componentes deduzidos superarem a receita bruta. Não deve ser confundida com margem de lucro contábil do clube.  
**Publication label:** Margem de retenção.

A margem agregada de uma competição deve ser calculada pela soma dos resultados líquidos metodológicos dividida pela soma das receitas brutas elegíveis, multiplicada por 100.

## 8. Financial burden indicators

### 8.1 Taxes and Fees Burden

**Code:** `OFE-FEE-001`  
**Definition:** Participação conjunta de tributos e taxas identificados sobre a receita bruta da partida.  
**Formula:**

`(Taxes + Fees) / Gross Match Revenue × 100`

**Unit:** Percentual (%).  
**Required data:** Receita bruta maior que zero, rubricas de tributos e taxas classificadas e validadas.  
**Interpretation:** Indica a parcela da receita bruta atribuída às classes de tributos e taxas.  
**Limitations:** Despesas operacionais e outras deduções não integram o numerador. A composição das rubricas deve ser divulgada para permitir comparação. Se a documentação não permitir identificar essas classes de forma suficiente, o indicador será inelegível.  
**Publication label:** Peso de tributos e taxas.

Tributos e taxas devem permanecer disponíveis separadamente na base, mesmo quando o indicador agregado for publicado.

## 9. Attendance indicators

### 9.1 Total Attendance

**Code:** `OFE-ATT-001`  
**Definition:** Público total declarado no documento oficial.  
**Formula:** Valor declarado. Na ausência desse total, poderá ser derivado pela soma de público pagante e não pagante somente quando ambos estiverem disponíveis, forem compatíveis e a derivação for registrada.  
**Unit:** Pessoas.  
**Required data:** Público total declarado ou componentes validados.  
**Limitations:** Critérios de contagem podem variar entre federações. Valores derivados devem ser identificados.

### 9.2 Non-Paying Attendance Share

**Code:** `OFE-ATT-002`  
**Definition:** Proporção do público total classificada como não pagante.  
**Formula:** `Non-Paying Attendance / Total Attendance × 100`  
**Unit:** Percentual (%).  
**Required data:** Público não pagante e público total maior que zero, com definições compatíveis. O público não pagante pode ser declarado diretamente ou derivado como `Total Attendance - Paying Attendance` quando ambos forem válidos e comparáveis.  
**Interpretation:** Participação de pessoas não pagantes no público total.  
**Limitations:** Cortesias, gratuidades, credenciais e outras categorias podem variar. Não representa taxa de ocupação do estádio.  
**Publication label:** Participação de público não pagante.

### 9.3 Stadium Occupancy Rate

**Code:** `OFE-ATT-003`  
**Definition:** Proporção da capacidade utilizável do estádio ocupada pelo público total da partida.  
**Formula:** `Total Attendance / Usable Stadium Capacity × 100`  
**Unit:** Percentual (%).  
**Required data:** Público total, capacidade utilizável maior que zero e fonte confiável para a capacidade e configuração aplicáveis à partida.  
**Interpretation:** Utilização da capacidade disponibilizada para a partida.  
**Limitations:** Capacidade nominal não equivale necessariamente à capacidade utilizável. Interdições, obras, setores fechados e sanções podem alterar a capacidade disponível. A fonte, data e contexto da capacidade devem ser registrados. Se a capacidade aplicável à partida não puder ser comprovada, o indicador será inelegível.

## 10. Estimated indicators

### 10.1 Estimated Ticketing Break-even

**Code:** `OFE-EST-001`  
**Definition:** Estimativa do número de pagantes necessário para atingir resultado financeiro igual a zero, sob hipóteses explícitas.  
**Conceptual formula:**

`(Attributable Fixed Costs - Other Attributable Revenue) / Net Average Revenue per Paying Attendee`

**Unit:** Pagantes.  
**Required data:** Custos fixos atribuíveis, outras receitas atribuíveis, receita líquida média por pagante e hipóteses documentadas.  
**Limitations:** Não é um valor observado diretamente no borderô. Exige separação entre custos fixos e variáveis e identificação das receitas não provenientes de ingressos.  
**Publication rule:** Não publicar na versão 1.0.0 enquanto os componentes e premissas necessários não forem identificáveis e validados. O indicador permanece definido para desenvolvimento metodológico futuro.

## 11. Indicator eligibility

A elegibilidade é avaliada por indicador e por partida.

| Missing or inconsistent information | Affected indicators |
|---|---|
| Receita bruta | Receita bruta por pagante, resultado metodológico, margem de retenção e peso de tributos e taxas |
| Público pagante | Receita bruta por pagante; participação de não pagantes quando o público não pagante depender dessa derivação |
| Público total | Despesa operacional por torcedor, participação de não pagantes e ocupação |
| Despesas operacionais | Despesa operacional por torcedor, resultado metodológico e margem de retenção |
| Tributos ou taxas sem identificação suficiente | Peso de tributos e taxas; resultado metodológico e margem de retenção quando forem componentes relevantes e não puderem ser quantificados |
| Rubrica material não classificada, como item promocional sem natureza esclarecida | Resultado metodológico e margem de retenção, quando não for possível determinar seu tratamento |
| Outras deduções relevantes sem classificação | Resultado metodológico e margem de retenção |
| Capacidade utilizável do estádio | Taxa de ocupação |
| Custos fixos ou receitas atribuíveis insuficientes | Ponto de equilíbrio estimado |

A ausência de informação só pode ser tratada como zero quando a fonte ou uma regra de derivação validada confirmar esse valor. Quando a documentação não permitir determinar se uma classe de dedução existe ou qual seu valor, não se deve assumir que ela é zero.

Cada indicador inelegível deve apresentar um motivo explícito. Avisos e ressalvas não devem ser confundidos com validação plena.

## 12. Aggregation methodology

### 12.1 General rule

Razões e percentuais agregados devem ser calculados sobre os totais elegíveis, e não pela média simples dos resultados individuais.

### 12.2 Competition-level indicators

| Indicator | Aggregation formula |
|---|---|
| Receita bruta | `Σ Gross Match Revenue` |
| Despesas operacionais | `Σ Match Operating Expenses` |
| Tributos | `Σ Taxes` |
| Taxas | `Σ Fees` |
| Outras deduções incluídas | `Σ Other Included Deductions` |
| Resultado líquido metodológico | `Σ Methodological Net Match Result` |
| Margem de retenção | `Σ Methodological Net Match Result / Σ Gross Match Revenue × 100` |
| Despesa operacional por torcedor | `Σ Operating Expenses / Σ Total Attendance` |
| Receita bruta por pagante | `Σ Gross Match Revenue / Σ Paying Attendance` |
| Participação de não pagantes | `Σ Non-Paying Attendance / Σ Total Attendance × 100` |
| Peso de tributos e taxas | `(Σ Taxes + Σ Fees) / Σ Gross Match Revenue × 100` |
| Taxa de ocupação | `Σ Total Attendance / Σ Usable Stadium Capacity × 100`, somente quando a capacidade por partida for válida e comparável |

Somente partidas elegíveis para o indicador correspondente participam do cálculo. Quando as definições ou condições não forem comparáveis, os resultados devem ser separados em grupos ou publicados com ressalva explícita.

### 12.3 Coverage disclosure

Toda publicação agregada deve informar, no mínimo:
- Total de partidas da competição no período.
- Número de documentos oficiais localizados.
- Número de partidas com dados ingeridos e validados.
- Número de partidas elegíveis para cada indicador publicado.
- Critérios de exclusão e limitações relevantes.

## 13. Illustrative calculation example

Os valores a seguir são hipotéticos e demonstram a aplicação das fórmulas.

**Match data:**

| Field | Value |
|---|---:|
| Receita bruta | R$ 500.000,00 |
| Despesas operacionais | R$ 160.000,00 |
| Tributos | R$ 10.000,00 |
| Taxas | R$ 20.000,00 |
| Outras deduções incluídas | R$ 10.000,00 |
| Público pagante | 10.000 |
| Público não pagante | 1.000 |
| Público total | 11.000 |
| Capacidade utilizável | 20.000 |

**Calculated indicators:**

| Indicator | Calculation | Result |
|---|---|---:|
| Resultado líquido metodológico | 500.000 - 160.000 - 10.000 - 20.000 - 10.000 | R$ 300.000,00 |
| Margem de retenção | 300.000 / 500.000 × 100 | 60,0% |
| Despesa operacional por torcedor | 160.000 / 11.000 | R$ 14,55 |
| Receita bruta por pagante | 500.000 / 10.000 | R$ 50,00 |
| Participação de não pagantes | 1.000 / 11.000 × 100 | 9,1% |
| Taxa de ocupação | 11.000 / 20.000 × 100 | 55,0% |
| Peso de tributos e taxas | (10.000 + 20.000) / 500.000 × 100 | 6,0% |

O exemplo pressupõe que todas as classes financeiras estejam identificadas, completas e validadas.

## 14. Publication requirements

Toda publicação de indicadores deve informar, quando aplicável:
- Código e nome do indicador.
- Definição, fórmula e unidade.
- Competição e período analisados.
- Número de partidas elegíveis.
- Cobertura documental.
- Versão do dicionário metodológico.
- Limitações, ressalvas e critérios de exclusão relevantes.

Valores declarados e calculados devem ser identificados separadamente. Alterações em fórmulas, escopo ou elegibilidade devem ser versionadas. Mudanças que afetem comparabilidade histórica devem ser explicitadas.

## 15. Methodological limitations

A versão 1.0.0 estabelece uma metodologia inicial para dados financeiros documentados por partida. Sua aplicação depende da qualidade, completude e consistência dos borderôs disponíveis.

A classificação de rubricas pode exigir revisão humana quando os rótulos forem ambíguos ou quando o tratamento variar entre documentos. O OFE não deve inferir a natureza financeira de uma rubrica sem evidência suficiente. Se uma rubrica material permanecer não classificada, o resultado líquido metodológico e a margem de retenção não devem ser publicados como valores completos.

Indicadores que dependam de dados ainda não disponíveis de forma consistente, como ponto de equilíbrio de bilheteria, permanecem definidos, mas não são autorizados para publicação regular nesta versão.

A inclusão de competições masculinas e femininas no mesmo escopo não implica equivalência econômica ou operacional. Comparações devem considerar contexto, disponibilidade e cobertura dos dados.

## 16. Related documents

- `ofe-scope.md` — escopo institucional e operacional do OFE.
- `bordero-data-standard.md` — contrato canônico de dados de borderôs.
- `schemas/bordero.schema.json` — esquema de validação dos dados.
- `catalogs/financial-categories.json` — catálogo de categorias financeiras.

## 17. Version history

| Version | Date | Description |
|---|---|---|
| 0.1 | November 2026 | Initial indicator definitions and calculation methodology |
| 1.0.0 | November 2026 | Consolidated formulas, financial classification, eligibility, aggregation and publication rules |
