# Análise de Padrões de Consumo de Energia em Granjas de Frango de Corte

Este projeto analisa os padrões de consumo de energia em uma granja de frango de corte para testes em novas tecnologias, como o BESS (Battery Energy Storage System). A análise tem como objetivo entender o consumo de energia em diferentes lotes e aviários, identificar padrões e gerar insights para otimização e aplicação de novas tecnologias.

## Estrutura do Projeto

*   `assets/`: Contém os arquivos PDF com os dados de custeio da atividade da granja.
*   `data/`:
    *   `raw/`: Contém os dados brutos, incluindo resumos por aviário e dados de corrente elétrica.
    *   `processed/`: Contém os dados processados e os resultados das análises em formato deTabela.
*   `docs/`: Contém as imagens dos gráficos gerados pela análise.
*   `src/`: Contém os scripts Python para extração, processamento e análise dos dados.
*   `main.py`: O script principal que orquestra a execução de todo o pipeline.
*   `requirements.txt`: As dependências do projeto.

## Análises Realizadas

Os seguintes scripts de análise são executados pelo `main.py`:

*   `analise_consumo_diario.py`: Analisa e gera um gráfico do consumo médio diário de energia.
*   `analise_consumo_total.py`: Analisa e gera um gráfico do consumo total de energia por lote.
*   `analise_eficiencia_energetica.py`: Analisa a eficiência energética, gerando gráficos de consumo por m², por ave e por kg.
*   `analise_corrente_diaria.py`: Analisa a corrente elétrica diária, calculando a média, mediana e máxima.
*   `estimativa_consumo_diario.py`: Estima o consumo diário de energia com base nos dados de corrente elétrica.
*   `analise_detalhada_consumo.py`: Realiza uma análise detalhada do consumo, calculando o consumo por ave e agrupando por ano e aviário.
*   `plot_consumo_medio_por_aviario.py`: Gera um gráfico de barras do consumo médio por aviário e ano.
*   `plot_consumo_acumulado_lote.py`: Gera um gráfico de série temporal do consumo acumulado por lote.

## Dados Estruturados Gerados (`/data/processed`)

*   `analise_eficiencia_energetica.csv`: Dados de consumo de energia por m², por ave e por kg para cada lote.
*   `consumo_acumulado_lote.csv`: Série temporal do consumo de energia acumulado para cada lote.
*   `consumo_medio_diario.csv`: Consumo médio diário de energia ao longo dos dias de vida do lote.
*   `consumo_total_lote.csv`: Consumo total de energia para cada lote.
*   `analise_corrente_diaria.csv`: Análise diária da corrente elétrica (mediana, média, contagem).
*   `max_corrente_por_dia.csv`: Corrente elétrica máxima para cada dia de criação.
*   `estimativa_consumo_diario.csv`: Estimativa do consumo diário de energia em kWh.

## Gráficos Gerados (`/docs`)

*   `consumo_por_m2.png`: Consumo de energia por m² por lote, agrupado por aviário.
*   `consumo_por_ave.png`: Mediana do consumo de energia por ave, agrupado por aviário.
*   `consumo_por_kg.png`: Consumo de energia por kg por lote.
*   `consumo_medio_diario.png`: Gráfico de linha do consumo médio diário de energia.
*   `consumo_total_lote.png`: Gráfico de barras do consumo total de energia por lote.
*   `median_corrente_por_dia.png`: Mediana da corrente elétrica por dia.
*   `mean_corrente_por_dia.png`: Média da corrente elétrica por dia.
*   `max_corrente_por_dia.png`: Máxima da corrente elétrica por dia.
*   `estimativa_consumo_diario.png`: Gráfico de linha da estimativa do consumo diário de energia.
*   `consumo_medio_por_aviario_ano.png`: Gráfico de barras do consumo médio por aviário e por ano.
*   `consumo_acumulado_lote_timeseries.png`: Série temporal do consumo de energia acumulado para cada lote.

## Como Executar o Projeto

1.  **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

2.  **Execute o pipeline completo:**

    ```bash
    python3 main.py
    ```

    Isso executará todas as etapas de extração, processamento e análise de dados. Os gráficos gerados serão salvos no diretório `docs/` e os dados processados no diretório `data/processed/`.