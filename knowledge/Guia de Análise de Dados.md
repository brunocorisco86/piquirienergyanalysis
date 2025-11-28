# Guia para Análise de Dados de Consumo de Energia

## Objetivo do Documento

Este documento serve como um guia para um agente de IA, detalhando como utilizar os dados e scripts deste projeto para realizar análises sobre o consumo de energia em granjas de frango de corte. O objetivo é capacitar o agente a responder perguntas de forma autônoma, utilizando os recursos disponíveis.

## Estrutura de Dados

O projeto está organizado com os dados brutos e processados em diretórios distintos.

### Dados Brutos (`data/raw/`)

*   **`resumo_por_aviario/`**: Contém arquivos Excel (`.xlsx`) com o resumo diário do lote, incluindo consumo de energia e outros parâmetros. A coluna "Semanas" indica o dia da criação, e a coluna ao lado de "Energia (kWh)" contém o valor do consumo.
*   **`corrente_eletrica/`**: Arquivos CSV com medições de corrente elétrica ao longo do tempo.

### Dados Processados (`data/processed/`)

Este diretório contém os dados já limpos e agregados, prontos para análise. Para uma descrição detalhada de cada arquivo, consulte o `data/processed/README.md`. Os principais arquivos são:

*   `analise_detalhada_consumo.csv`: Consumo médio total e por ave, agrupado por ano e por `Fazenda` (aviário).
*   `consumo_acumulado_lote.csv`: Série temporal do consumo de energia acumulado para cada lote.
*   `analise_eficiencia_energetica.csv`: Dados de consumo por m², por ave e por kg.
*   `consumo_medio_diario.csv`: Consumo médio de energia por dia de vida do lote.

**Colunas Importantes:**
*   `lote`: Identificador do lote.
*   `aviario` / `Fazenda`: Identificador do aviário.
*   `energia_kwh`: Consumo de energia em kilowatt-hora.
*   `aves_abatidas`: Número de aves abatidas no lote.
*   `peso_total_kg`: Peso total do lote em kg.

## Scripts de Análise (`src/`)

Os scripts no diretório `src/` automatizam a análise dos dados. O `main.py` orquestra a execução de todos eles. Cada script gera um arquivo de dados estruturado em `data/processed/` e um ou mais gráficos em `docs/`.

*   `analise_consumo_diario.py`: Calcula e plota o consumo médio diário.
*   `analise_consumo_total.py`: Calcula e plota o consumo total por lote.
*   `analise_eficiencia_energetica.py`: Calcula e plota a eficiência energética (consumo/m², consumo/ave, consumo/kg).
*   `analise_corrente_diaria.py`: Analisa e plota a corrente elétrica diária (média, mediana, máxima).
*   `estimativa_consumo_diario.py`: Estima o consumo de energia a partir da corrente elétrica.
*   `analise_detalhada_consumo.py`: Gera a análise detalhada por ano e aviário.
*   `plot_consumo_medio_por_aviario.py`: Plota o consumo médio por aviário e ano.
*   `plot_consumo_acumulado_lote.py`: Plota a série temporal do consumo acumulado.

## Como Responder a Perguntas Comuns

Para responder a perguntas, um agente deve seguir os seguintes passos:
1.  Identificar a pergunta e os dados necessários.
2.  Carregar o arquivo CSV apropriado de `data/processed/` usando a biblioteca `pandas`.
3.  Realizar as agregações ou filtros necessários.
4.  Apresentar os resultados (em texto, tabela ou gerando um novo gráfico).

### Exemplos de Perguntas e Respostas

**Pergunta:** "Qual o consumo médio de energia por ave para o aviário 1117 no ano de 2023?"
**Resposta:**
1.  Carregar `data/processed/analise_detalhada_consumo.csv`.
2.  Filtrar a tabela para `year == 2023` e `Fazenda == 1117`.
3.  Selecionar a coluna `consumo_medio_por_ave`.

**Pergunta:** "Mostre-me a evolução do consumo do lote 17 do aviário 1117."
**Resposta:**
1.  Carregar `data/processed/consumo_acumulado_lote.csv`.
2.  Filtrar a tabela para `aviario_lote == '1117-17'`.
3.  Gerar um gráfico de linha com `date` no eixo X e `cumulative_consumption` no eixo Y.

**Pergunta:** "Crie um gráfico comparando o consumo total de todos os lotes do aviário 665."
**Resposta:**
1.  Carregar `data/processed/consumo_total_lote.csv`.
2.  Filtrar a tabela para `aviario == 665`.
3.  Gerar um gráfico de barras com `lote` no eixo X e `energia_kwh` no eixo Y.
4.  Salvar o novo gráfico em `docs/` com um nome descritivo (e.g., `comparativo_lotes_aviario_665.png`).

Seguindo este guia, um agente pode eficientemente explorar os dados e fornecer respostas precisas e visualizações claras.
