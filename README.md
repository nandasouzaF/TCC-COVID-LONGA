# Trabalho de conclusão de Curso Covid Longa

### Objetivo do Projeto

Este projeto foi desenvolvido com o propósito de oferecer informações pertinentes a pessoas que tenham enfrentado a COVID-19 e possam estar experimentando sintomas persistentes após a infecção, conhecidos como "COVID longa". A análise de dados baseada em conjuntos reais busca fornecer um formulário que possibilite referenciar esses dados, permitindo uma avaliação da probabilidade de um paciente apresentar sintomas associados à COVID longa.

### Funcionalidades Principais

O projeto engloba um formulário que requer autenticação através de login. Dentro deste formulário (teste), os pacientes podem inserir seus dados e relatar possíveis sintomas persistentes após a infecção. Ao concluir o teste, o paciente receberá uma avaliação da probabilidade de estar enfrentando sintomas relacionados à COVID longa. É importante ressaltar que esta avaliação serve como um indicativo e não substitui a consulta médica. Se houver indicação de sintomas persistentes, é altamente recomendável buscar orientação profissional médica.


## Analise de dados 


### Dados
Dados do DATASUS - SRAG 2021 a 2023:
O conjunto de dados utilizado nesta pesquisa foi coletado do DATASUS - Ministério da Saúde, especificamente do Banco de Dados de Síndrome Respiratória Aguda Grave (SRAG) abrangendo os anos de 2021 a 2023. A SRAG é objeto de vigilância pelo Ministério da Saúde desde a pandemia de Influenza A(H1N1)pdm09, e posteriormente, a vigilância da COVID-19 foi incorporada nessa rede de monitoramento.

### Limpeza e Pré-processamento de Dados

Nesta seção, apresentamos o processo de limpeza e pré-processamento dos dados brutos da COVID-19 do DATASUS para os anos 2021, 2022 e 2023. Inicialmente, unimos os dados em um conjunto único e realizamos diversas etapas de pré-processamento para corrigir inconsistências e erros. Esse procedimento foi crucial para garantir a qualidade e confiabilidade das informações ao longo desses três anos. 

Durante a limpeza de dados, identificamos e corrigimos erros como valores ausentes, duplicados e inconsistências. Também padronizamos formatos e validamos informações para assegurar a integridade dos dados. Essa etapa foi essencial para garantir que os dados estivessem precisos e prontos para análise.

## Análise Exploratória de Dados

Nesta seção, conduzimos uma análise estatística e aplicamos tratamentos às variáveis categóricas selecionadas. Métodos utilizados incluem:

- **Contagem de Frequência:** Observação da ocorrência de diferentes valores nas variáveis.
- **Gráfico de Barras:** Representação visual da frequência das variáveis por meio de barras.
- **Visualização da Frequência das Variáveis:** Análise visual para compreensão da distribuição dos dados.
- **Visualização da Distribuição:** Observação e interpretação da distribuição dos dados.
- **Tabela de Contingência:** Análise tabular para compreender relações entre diferentes variáveis.
- **Teste Qui-Quadrado:** Avaliação estatística para verificar associações entre variáveis categóricas.
- **Análise de Variância (ANOVA):** Aplicação em casos específicos para avaliar diferenças significativas entre grupos.

## Hipótese

"Determinadas características pessoais, sintomas e comorbidades estão associados a um maior risco de desenvolver COVID longa."

**Explicação:** Esta suposição está centrada na possível existência de fatores específicos, como características pessoais (sexo
, idade, raça e escolaridade), sintomas (diarreia, desconforto respiratório, perda do paladar, perda do olfato, fadiga e tosse) e 
comorbidades (nosocomial, dispneia, pneumopatia, cardiopatia, Síndrome de Down, asma, diabetes renal, obesidade e condições neurológicas),
que podem estar relacionados a um maior risco de desenvolver COVID longa. Esta hipótese serve como base para a análise exploratória detalhada conduzida neste contexto.


