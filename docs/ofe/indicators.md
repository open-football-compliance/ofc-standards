# Indicadores do OFE

**Versão:** 1.0.0

Este documento define os indicadores utilizados pelo Observatório Financeiro dos Estaduais. Os cálculos usam os dados extraídos dos borderôs e organizados conforme o [padrão de dados](data-standard.md).

## Regras gerais
- Valores monetários são expressos em reais (BRL).
- Dados ausentes não são tratados como zero.
- Os valores declarados no borderô são preservados separadamente dos valores calculados pelo OFE.
- Rubricas sem classificação confiável não entram automaticamente nos cálculos.
- Em análises agregadas, somamos os valores das partidas elegíveis antes de calcular percentuais e médias por pessoa.

## Indicadores

| Indicador | Fórmula | Observação |
|---|---|---|
| Receita bruta | Valor declarado no borderô | Receita atribuída à partida. |
| Despesas operacionais | Soma das rubricas classificadas como despesas operacionais | Não inclui tributos, taxas ou outras deduções. |
| Tributos | Soma das rubricas classificadas como tributos | Mantidos separados das despesas operacionais. |
| Taxas | Soma das rubricas classificadas como taxas | Mantidas separadas dos tributos. |
| Outras deduções | Soma das demais deduções identificadas | Não inclui rubricas desconhecidas. |
| Resultado líquido declarado | Valor informado no borderô | Preservado como publicado pela fonte. |
| Resultado líquido metodológico | Receita bruta − despesas operacionais − tributos − taxas − outras deduções | Calculado quando as informações necessárias estiverem completas. |
| Margem de retenção | Resultado líquido metodológico ÷ receita bruta × 100 | Parcela da receita bruta que permanece após as deduções consideradas. |
| Despesa operacional por torcedor | Despesas operacionais ÷ público total | Requer público total maior que zero. |
| Receita bruta por pagante | Receita bruta ÷ público pagante | Não equivale necessariamente ao preço médio do ingresso. |

## Resultado metodológico incompleto
Se existir uma rubrica relevante sem classificação ou faltar informação necessária, o resultado líquido metodológico e a margem de retenção ficam sem valor (`null`). Não se presume que uma rubrica desconhecida seja despesa, taxa, tributo ou dedução.

## Exemplo
Receita bruta de R$ 100.000, despesas operacionais de R$ 40.000, tributos de R$ 5.000, taxas de R$ 3.000 e outras deduções de R$ 2.000:

- Resultado líquido metodológico: R$ 50.000.
- Margem de retenção: 50%.

Exemplo ilustrativo, não referente a uma partida real.
