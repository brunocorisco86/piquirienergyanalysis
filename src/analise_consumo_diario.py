import pandas as pd
import matplotlib.pyplot as plt

def analise_consumo_diario():
    """
    This function analyzes the daily energy consumption.
    """
    df_consumo = pd.read_csv('data/processed/consumo_energia_por_lote.csv')
    df_zootecnico = pd.read_csv('data/processed/dados_zootecnicos.csv')

    df = pd.merge(df_consumo, df_zootecnico, on=['lote', 'aviario'])

    df_consumo_diario = df.groupby('dia')['energia_kwh'].mean().reset_index()

    if df_consumo_diario.empty:
        print("Não há dados para gerar o gráfico de consumo médio diário.")
        return

    df_consumo_diario.to_csv('data/processed/consumo_medio_diario.csv', index=False)

    plt.figure(figsize=(12, 6))
    plt.plot(df_consumo_diario['dia'], df_consumo_diario['energia_kwh'])
    plt.xlabel('Dia de Vida do Lote')
    plt.ylabel('Consumo Médio de Energia (kWh)')
    plt.title('Consumo Médio de Energia por Dia de Vida do Lote')
    plt.grid(True)
    plt.savefig('docs/consumo_medio_diario.png')

if __name__ == '__main__':
    analise_consumo_diario()
