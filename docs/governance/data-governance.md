# OFC Data Governance Policy

**Status:** Draft  
**Version:** 0.1  
**Responsible organization:** Open Football Compliance (OFC)

## 1. Purpose

Estabelecer princípios de governança para coleta, organização, validação, armazenamento, interpretação e publicação de dados utilizados pelo Open Football Compliance.

## 2. Data governance principles

### 2.1 Source preservation

Documentos oficiais utilizados como fonte devem ser preservados em sua forma original sempre que legal e tecnicamente possível.

A normalização não deve sobrescrever os valores originais.

### 2.2 Traceability

Dados publicados devem possuir vínculo rastreável com suas fontes e transformações.

Sempre que aplicável, devem ser registrados:

- Identificador da fonte.
- Localização do documento.
- Data de coleta.
- Identificador da partida ou entidade.
- Método de extração.
- Transformações realizadas.
- Validações aplicadas.
- Histórico de revisão.

### 2.3 Data quality

A qualidade dos dados deve ser avaliada considerando:

- Completude.
- Consistência.
- Precisão.
- Validade.
- Atualidade.
- Rastreabilidade.

### 2.4 Separation of data layers

O OFC adota quatro camadas conceituais:

1. **Original data:** informação preservada conforme publicada na fonte.
2. **Normalized data:** informação convertida para os padrões e taxonomias do OFC.
3. **Derived data:** indicadores e cálculos produzidos a partir dos dados normalizados.
4. **Interpretation:** análises, conclusões e observações editoriais.

Essas camadas devem permanecer distinguíveis.

## 3. Data quality and validation

Regras de validação devem ser documentadas e reproduzíveis.

Dados inconsistentes não devem ser corrigidos silenciosamente.

Quando houver divergências, o registro deve preservar os valores de origem e indicar a inconsistência identificada.

A ausência de informação deve ser representada como dado ausente, e não como zero.

## 4. Provenance and auditability

As transformações relevantes devem ser registradas para permitir reconstrução do processo de produção dos dados.

Alterações manuais devem possuir justificativa e histórico de revisão.

A confiança de um processo automatizado de extração não deve ser confundida com a confirmação da veracidade contábil do documento original.

## 5. Access and publication

O acesso aos dados deve considerar:

- Direitos de uso das fontes.
- Restrições legais e contratuais.
- Segurança da informação.
- Necessidade de proteção de dados pessoais.
- Finalidade institucional da publicação.

A publicação de dados não deve pressupor que todo documento obtido pode ser redistribuído publicamente.

## 6. Institutional and technical responsibilities

O OFC é responsável por definir e governar:

- Padrões institucionais.
- Semântica dos dados.
- Taxonomias oficiais.
- Metodologias e indicadores.
- Políticas de publicação.

Implementações tecnológicas podem ser desenvolvidas pelo OFC ou por fornecedores independentes.

A implementação de um padrão não transfere automaticamente sua governança institucional ao fornecedor.

## 7. Standard evolution

Alterações nos padrões devem ser versionadas e documentadas.

Mudanças que afetem a interpretação dos dados ou a comparabilidade histórica devem ser explicitamente identificadas.

## 8. Scope

Esta política aplica-se aos dados e processos institucionais do OFC, incluindo o Observatório Financeiro dos Estaduais e futuros padrões e iniciativas de transparência no futebol.