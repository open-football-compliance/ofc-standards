# Observatório Financeiro dos Estaduais (OFE)

**Organization:** Open Football Compliance (OFC)  
**Document ID:** OFC-OFE-SCOPE  
**Version:** 1.0.0  
**Status:** Proposed  
**Initial season:** 2027  
**Last updated:** November 2026

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

### 3.2 Competition scope

O OFE abrange **competições estaduais profissionais de futebol, masculinas e femininas**, realizadas no território brasileiro.

A inclusão de uma competição não depende do gênero da modalidade, mas do atendimento aos critérios de escopo, da natureza profissional da competição e da disponibilidade de documentação financeira oficial por partida.

O escopo contempla informações como:

- Receitas de bilheteria e outras receitas vinculadas à partida, quando discriminadas.
- Público pagante e não pagante.
- Público total.
- Despesas operacionais.
- Taxas, tributos e deduções.
- Resultado financeiro declarado ou calculado conforme a metodologia do OFE.

A implantação será progressiva, começando pelo Campeonato Pernambucano e avançando para outras competições estaduais conforme disponibilidade documental, qualidade dos dados e capacidade operacional.

### 3.3 Initial pilot

O Campeonato Pernambucano será utilizado como piloto inicial para validação da metodologia, do padrão de dados e dos processos de coleta e análise.

A utilização de uma competição como piloto não limita a abrangência nacional do observatório.

## 4. Inclusion criteria

Uma partida poderá ser incluída na base do OFE quando atender às seguintes condições:

1. Pertencer a uma competição estadual oficial de futebol profissional, masculina ou feminina, abrangida pelo observatório.
2. Possuir registro identificável da partida.
3. Ter documento financeiro oficial disponível ou obtível junto a uma fonte oficial.
4. Permitir associar as informações financeiras à respectiva partida.
5. Possuir fonte e procedência documental registráveis.

A existência de um documento não significa que todas as suas informações sejam elegíveis para todos os indicadores.

## 5. Exclusion criteria

Estão fora do escopo:

- Competições nacionais e regionais, incluindo Campeonato Brasileiro, Copa do Brasil, Copa do Nordeste e Copa Verde.
- Partidas amistosas e eventos de pré-temporada.
- Estimativas financeiras sem documentação verificável.
- Receitas gerais dos clubes que não possam ser atribuídas diretamente a uma partida.
- Registros cuja associação com uma partida específica não possa ser estabelecida.

A exclusão da base analítica não implica a eliminação da fonte original ou de seu histórico de coleta.

## 6. Data sources

### 6.1 Primary sources

A fonte primária é o documento financeiro oficial da partida, especialmente o borderô publicado pela federação ou pelo organizador da competição.

### 6.2 Supporting sources

Fontes adicionais poderão ser utilizadas para identificar ou contextualizar informações, incluindo:

- Publicações oficiais das federações.
- Regulamentos oficiais das competições.
- Documentação sobre estádios e capacidade.
- Comunicados oficiais dos clubes.
- Outras publicações institucionais relevantes para a partida.

As fontes complementares devem ser identificadas separadamente do documento financeiro primário.

### 6.3 Source preservation

Sempre que legal e tecnicamente possível, o documento original deverá ser preservado.

O observatório deverá manter rastreabilidade entre as informações publicadas e suas fontes originais.

## 7. Data classification

O OFE distingue quatro camadas de informação:

### 7.1 Original data

Valores e descrições exatamente como apresentados no documento de origem.

### 7.2 Normalized data

Valores mapeados para o OFC Borderô Data Standard, incluindo rótulos, categorias, unidades e formatos padronizados.

Os valores originais devem permanecer preservados.

### 7.3 Derived data

Indicadores e cálculos produzidos a partir dos dados normalizados, de acordo com o OFE Financial Indicators Dictionary.

### 7.4 Interpretations

Observações analíticas, comparações, alertas de anomalia e conclusões editoriais produzidas pelo OFC.

Essas camadas devem permanecer distinguíveis no fluxo de dados e nas análises publicadas.

## 8. Data quality and analytical eligibility

### 8.1 Missing information

Informações ausentes devem ser representadas como `null`, nunca como zero.

O valor zero só é válido quando explicitamente informado pela fonte ou quando resultar de derivação documentada e validada.

### 8.2 Inconsistencies

Quando houver inconsistências, os valores originais devem ser preservados e a divergência documentada.

Exemplos:

- Componentes de público que não correspondem ao público total declarado.
- Diferenças entre renda bruta, despesas, deduções e renda líquida.
- Categorias financeiras ausentes ou ambíguas.
- Valores conflitantes entre versões diferentes de um documento oficial.

### 8.3 Indicator-specific eligibility

A elegibilidade deve ser avaliada individualmente para cada indicador.

A ausência da capacidade do estádio, por exemplo, impede o cálculo da taxa de ocupação, mas não necessariamente o cálculo da margem de retenção.

Da mesma forma, a ausência do público pagante impede o cálculo da receita bruta por pagante, mas não invalida automaticamente outros indicadores.

### 8.4 Structural incompleteness

Uma partida poderá ser classificada como estruturalmente incompleta quando informações essenciais estiverem ausentes ou quando houver inconsistências não resolvidas que comprometam a confiabilidade dos cálculos financeiros afetados.

Os indicadores comprometidos devem ser marcados como inelegíveis, acompanhados de uma justificativa explícita.

## 9. Comparability principles

As comparações devem considerar diferenças de:

- Competição e temporada.
- Estrutura documental e convenções contábeis.
- Classificação de receitas e despesas.
- Práticas de contabilização de público.
- Capacidade e configuração dos estádios.
- Restrições de público, incluindo portões fechados e sanções.
- Disponibilidade e completude das informações financeiras.

As comparações devem utilizar definições de dados equivalentes e amostras elegíveis.

Quando as condições diferirem materialmente, o OFE deverá explicitar a limitação ou apresentar os resultados em grupos separados.

### 9.1 Gender and competition comparability

Os dados de competições masculinas e femininas integram o mesmo escopo institucional e padrão de dados.

Entretanto, sua comparação direta não deve pressupor equivalência de contexto econômico, operacional ou de público.

Análises comparativas entre essas competições devem explicitar diferenças relevantes de competição, infraestrutura, calendário, público, receitas, despesas e disponibilidade documental.

## 10. Coverage and transparency

O OFE deverá distinguir, no mínimo:

- Total de partidas da competição.
- Partidas para as quais um documento oficial foi localizado.
- Partidas com documento ingerido.
- Partidas com informações financeiras validadas.
- Partidas elegíveis para cada indicador publicado.

As informações de cobertura deverão acompanhar os relatórios agregados sempre que relevantes.

Uma média por competição deverá identificar a quantidade de partidas efetivamente utilizada no cálculo.

## 11. Publications

O OFE poderá publicar:

- Registros financeiros por partida.
- Boletins periódicos de competições.
- Análises financeiras comparativas.
- Resumos por competição.
- Relatórios por temporada.
- Notas metodológicas e relatórios de qualidade dos dados.

As publicações deverão identificar suas fontes, versão metodológica, período de análise, cobertura e limitações.

## 12. Institutional responsibilities

O Open Football Compliance é responsável por:

- Definir o escopo do observatório.
- Estabelecer a metodologia financeira.
- Governar os padrões de dados e as definições dos indicadores.
- Revisar as interpretações analíticas.
- Aprovar as publicações institucionais.

Provedores de tecnologia poderão desenvolver sistemas e serviços para ingestão, extração, normalização, validação, armazenamento e distribuição dos dados.

A implementação técnica não transfere ao provedor de tecnologia a governança institucional da metodologia ou dos padrões do OFE.

## 13. Related documents

- `financial-indicators-dictionary.md` — definições formais e regras de cálculo dos indicadores financeiros.
- `bordero-data-standard.md` — contrato canônico de dados para documentos financeiros de partidas.
- `schemas/bordero.schema.json` — esquema de validação legível por máquina.
- `catalogs/financial-categories.json` — catálogo de categorias financeiras.

## 14. Version history

| Version | Date | Description |
|---|---|---|
| 0.1 | November 2026 | Initial scope specification |
| 1.0.0 | November 2026 | Consolidation of scope, inclusion of men's and women's professional state competitions, and clarification of comparability principles |