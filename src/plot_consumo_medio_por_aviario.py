
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_average_consumption_by_aviary_and_year():
    """
    Generates a grouped bar chart of the average total consumption per lot,
    grouped by aviary and year.
    """
    # Read the processed data
    data_path = 'data/processed/analise_detalhada_consumo.csv'
    df = pd.read_csv(data_path)

    # Pivot the data for easy plotting
    pivot_df = df.pivot(index='year', columns='Fazenda', values='consumo_medio')

    # Plotting
    ax = pivot_df.plot(kind='bar', figsize=(12, 7), rot=0)
    
    plt.title('Consumo Médio de Energia por Aviário e Ano')
    plt.xlabel('Ano')
    plt.ylabel('Consumo Médio (kWh)')
    plt.legend(title='Aviário')
    plt.grid(axis='y', linestyle='--')
    
    # Add labels to the bars
    for container in ax.containers:
        ax.bar_label(container, fmt='%.0f')

    # Save the plot
    output_plot_path = 'docs/consumo_medio_por_aviario_ano.png'
    plt.savefig(output_plot_path)
    plt.close()

    print(f"Gráfico de consumo médio por aviário e ano salvo em '{output_plot_path}'.")

if __name__ == '__main__':
    plot_average_consumption_by_aviary_and_year()
