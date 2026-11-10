# OFC Standards

Documentação e padrões abertos do **Open Football Compliance (OFC)**.

Este repositório reúne o mínimo necessário para documentar os dados e indicadores utilizados pelo OFC.

## OFE — Observatório Financeiro dos Estaduais

O OFE organiza informações financeiras de partidas de competições estaduais profissionais masculinas e femininas no Brasil, a partir de borderôs e documentos oficiais.

### Documentos

- [Escopo](docs/ofe/scope.md) — objetivo e abrangência do observatório.
- [Indicadores](docs/ofe/indicators.md) — definições e fórmulas.
- [Padrão de dados](docs/ofe/data-standard.md) — como os dados são organizados.
- [Exemplo de partida](examples/match-example.json) — exemplo em JSON.
- [JSON Schema](schemas/match.schema.json) — validação básica do formato.

## Princípios

- Preservar os dados e descrições da fonte original.
- Não transformar informação ausente em zero.
- Não classificar rubricas sem fundamento.
- Distinguir valores declarados de cálculos do OFE.
- Informar limitações e dados que não puderam ser confirmados.

## Evolução

O padrão deve evoluir a partir de necessidades observadas em documentos reais. Novos campos e categorias serão adicionados quando forem necessários, sem antecipar complexidade.

## Licença

O conteúdo deste repositório está disponibilizado sob a **GNU General Public License v3.0 (GPL-3.0)**, conforme o arquivo [LICENSE](LICENSE).

O nome, os logotipos e as marcas OFC não são licenciados para uso promocional ou como indicação de endosso.
