import pandas as pd
import matplotlib.pyplot as plt

def analise_consumo_total():
    """
    This function analyzes the total energy consumption per lot.
    """
    df_consumo = pd.read_csv('data/processed/consumo_energia_por_lote.csv')
    df_zootecnico = pd.read_csv('data/processed/dados_zootecnicos.csv')

    df = pd.merge(df_consumo, df_zootecnico, on=['lote', 'aviario'])

    if df.empty:
        print("Não há dados para gerar o gráfico de consumo total por lote.")
        return

    df_consumo_total = df.groupby(['lote', 'aviario'])['energia_kwh'].sum().reset_index()

    df_consumo_total.to_csv('data/processed/consumo_total_lote.csv', index=False)

    plt.figure(figsize=(12, 6))
    plt.bar(df_consumo_total['lote'].astype(str) + '-' + df_consumo_total['aviario'].astype(str), df_consumo_total['energia_kwh'])
    plt.xlabel('Lote-Aviário')
    plt.ylabel('Consumo Total de Energia (kWh)')
    plt.title('Consumo Total de Energia por Lote e Aviário')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig('docs/consumo_total_lote.png')

if __name__ == '__main__':
    analise_consumo_total()
