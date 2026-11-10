# Padrão de dados do OFE

**Versão:** 1.0.0

Este documento define como o OFE organiza os dados extraídos dos borderôs. O objetivo é manter um formato simples e comum para analisar partidas de diferentes competições.

## 1. Partida
Registrar competição, temporada, data, mandante, visitante e estádio, quando disponíveis.

## 2. Público e bilheteria
Registrar separadamente, quando disponíveis:
- público total;
- público pagante;
- público não pagante;
- ingressos vendidos;
- arrecadação de ingressos.

**Importante:** ingressos vendidos não são necessariamente iguais ao público presente ou ao público pagante.

## 3. Dados financeiros
Registrar os totais declarados no documento, quando disponíveis: receita bruta, despesas operacionais, tributos, taxas, outras deduções e resultado líquido declarado.

O OFE também calcula o resultado líquido metodológico quando houver informação suficiente.

### Rubricas individuais
Cada rubrica deve conter:
- `source_label`: descrição original do borderô;
- `amount`: valor em reais;
- `category`: classificação normalizada, quando conhecida.

As categorias iniciais são simples: `revenue`, `operating_expense`, `tax`, `fee`, `deduction` e `unknown`. Não é necessário criar uma categoria para cada descrição. O nome original sempre deve ser preservado.

## 4. Fonte
Todo registro deve identificar a federação ou entidade emissora, o documento utilizado e, quando disponível, o endereço público do documento.

## 5. Regras
1. Não alterar o valor ou a descrição original.
2. Não preencher informação ausente com zero.
3. Não classificar uma rubrica sem fundamento.
4. Não somar novamente valores que já estejam incluídos em um total declarado.
5. Preservar separadamente valores declarados e cálculos do OFE.
6. Informar quando um cálculo não puder ser realizado.

## Exemplo e validação
- [Exemplo de partida](../../examples/match-example.json)
- [JSON Schema](../../schemas/match.schema.json)
