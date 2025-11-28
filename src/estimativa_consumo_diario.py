import pandas as pd
import matplotlib.pyplot as plt

def estimativa_consumo_diario():
    """
    This function estimates the daily energy consumption based on the electric current data.
    """
    # Load the processed data
    df_corrente = pd.read_csv('data/processed/corrente_eletrica_lote.csv')

    # Convert 'datetime' column to datetime objects
    df_corrente['datetime'] = pd.to_datetime(df_corrente['datetime'])

    # Define the start date of the batch
    start_date = pd.to_datetime('2025-10-07')

    # Calculate the day of creation for each row
    df_corrente['dia_criacao'] = (df_corrente['datetime'] - start_date).dt.days

    # Calculate power in Watts
    VOLTAGE = 220  # Volts
    POWER_FACTOR = 0.9
    df_corrente['power_w'] = VOLTAGE * df_corrente['corrente'] * POWER_FACTOR

    # Calculate time difference between rows (assuming data is ordered)
    df_corrente['time_diff_h'] = df_corrente['datetime'].diff().dt.total_seconds() / 3600
    df_corrente['time_diff_h'] = df_corrente['time_diff_h'].fillna(0) # Fill NaN for the first row

    # Calculate energy consumption in Wh for each interval
    df_corrente['energy_wh'] = df_corrente['power_w'] * df_corrente['time_diff_h']

    # Group by day of creation and sum the energy consumption
    consumo_diario = df_corrente.groupby('dia_criacao')['energy_wh'].sum().reset_index()
    
    # Convert energy from Wh to kWh
    consumo_diario['energy_kwh'] = consumo_diario['energy_wh'] / 1000

    # Save the results to a CSV file
    consumo_diario.to_csv('data/processed/estimativa_consumo_diario.csv', index=False)

    # Plot the estimated daily energy consumption
    plt.figure(figsize=(12, 6))
    plt.plot(consumo_diario['dia_criacao'], consumo_diario['energy_kwh'])
    plt.xlabel('Dia de Criação')
    plt.ylabel('Consumo de Energia Estimado (kWh)')
    plt.title('Consumo de Energia Estimado por Dia de Criação')
    plt.grid(True)
    plt.savefig('docs/estimativa_consumo_diario.png')

    # Print the results
    print("Estimativa de consumo diário de energia salva em 'data/processed/estimativa_consumo_diario.csv'")
    print("Gráfico da estimativa de consumo diário de energia salvo em 'docs/estimativa_consumo_diario.png'")

if __name__ == '__main__':
    estimativa_consumo_diario()
