import pandas as pd
import matplotlib.pyplot as plt

def analise_corrente_diaria():
    """
    This function analyzes the daily electric current.
    """
    # Load the processed data
    df_corrente = pd.read_csv('data/processed/corrente_eletrica_lote.csv')

    # Convert 'datetime' column to datetime objects
    df_corrente['datetime'] = pd.to_datetime(df_corrente['datetime'])

    # Define the start date of the batch
    start_date = pd.to_datetime('2025-10-07')

    # Calculate the day of creation for each row
    df_corrente['dia_criacao'] = (df_corrente['datetime'] - start_date).dt.days

    # Group by day of creation and calculate the median, mean and count
    analise_diaria = df_corrente.groupby('dia_criacao')['corrente'].agg(['median', 'mean', 'count']).reset_index()

    # Save the results to a CSV file
    analise_diaria.to_csv('data/processed/analise_corrente_diaria.csv', index=False)

    # Plot the median current per day
    plt.figure(figsize=(12, 6))
    plt.plot(analise_diaria['dia_criacao'], analise_diaria['median'])
    plt.xlabel('Dia de Criação')
    plt.ylabel('Mediana da Corrente Elétrica')
    plt.title('Mediana da Corrente Elétrica por Dia de Criação')
    plt.grid(True)
    plt.savefig('docs/median_corrente_por_dia.png')
    
    # Plot the mean current per day
    plt.figure(figsize=(12, 6))
    plt.plot(analise_diaria['dia_criacao'], analise_diaria['mean'])
    plt.xlabel('Dia de Criação')
    plt.ylabel('Média da Corrente Elétrica')
    plt.title('Média da Corrente Elétrica por Dia de Criação')
    plt.grid(True)
    plt.savefig('docs/mean_corrente_por_dia.png')

    # Print the results
    print("Análise diária da corrente elétrica salva em 'data/processed/analise_corrente_diaria.csv'")
    print("Gráficos salvos em 'docs/'")

def analise_corrente_maxima():
    """
    This function analyzes the maximum daily electric current.
    """
    # Load the processed data
    df_corrente = pd.read_csv('data/processed/corrente_eletrica_lote.csv')

    # Convert 'datetime' column to datetime objects
    df_corrente['datetime'] = pd.to_datetime(df_corrente['datetime'])

    # Define the start date of the batch
    start_date = pd.to_datetime('2025-10-07')

    # Calculate the day of creation for each row
    df_corrente['dia_criacao'] = (df_corrente['datetime'] - start_date).dt.days

    # Group by day of creation and calculate the maximum current
    max_corrente_por_dia = df_corrente.groupby('dia_criacao')['corrente'].max().reset_index()

    # Save the results to a CSV file
    max_corrente_por_dia.to_csv('data/processed/max_corrente_por_dia.csv', index=False)

    # Plot the maximum current per day
    plt.figure(figsize=(12, 6))
    plt.plot(max_corrente_por_dia['dia_criacao'], max_corrente_por_dia['corrente'])
    plt.xlabel('Dia de Criação')
    plt.ylabel('Máxima da Corrente Elétrica')
    plt.title('Máxima da Corrente Elétrica por Dia de Criação')
    plt.grid(True)
    plt.savefig('docs/max_corrente_por_dia.png')

    # Print the results
    print("Máxima da corrente elétrica por dia de criação salva em 'data/processed/max_corrente_por_dia.csv'")
    print("Gráfico da máxima da corrente elétrica por dia de criação salvo em 'docs/max_corrente_por_dia.png'")


if __name__ == '__main__':
    analise_corrente_diaria()
    analise_corrente_maxima()
