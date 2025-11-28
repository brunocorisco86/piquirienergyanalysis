import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def analise_eficiencia_energetica():
    """
    This function analyzes the energy efficiency.
    """
    df_consumo = pd.read_csv('data/processed/consumo_energia_por_lote.csv')
    df_zootecnico = pd.read_csv('data/processed/dados_zootecnicos.csv')
    df_resultados = pd.read_excel('data/processed/resultado_lotes.xlsx')

    # Merge df_consumo with df_zootecnico to get aves_abatidas and peso_total_kg
    df = pd.merge(df_consumo, df_zootecnico[['lote', 'aviario', 'aves_abatidas', 'peso_total_kg']], on=['lote', 'aviario'], how='left')

    # Merge df with df_resultados to get the 'Fazenda' column
    df['Número Composto'] = df['aviario'].astype(str) + '-' + df['lote'].astype(str)
    df = pd.merge(df, df_resultados[['Número Composto', 'Fazenda']], on='Número Composto', how='left')
    
    if df.empty:
        print("Não há dados para gerar os gráficos de eficiência energética.")
        return

    # Drop rows where necessary columns might be NaN after merges
    df.dropna(subset=['aves_abatidas', 'peso_total_kg', 'Fazenda'], inplace=True)
    df = df[df['aves_abatidas'] > 0] # Avoid division by zero

    df_consumo_total = df.groupby(['lote', 'aviario', 'aves_abatidas', 'peso_total_kg', 'Fazenda'])['energia_kwh'].sum().reset_index()
    
    # The area of the aviary is not available in the data. I will assume a value of 1500 m2 for all aviaries.
    area_aviario = 1500
    df_consumo_total['kwh_por_m2'] = df_consumo_total['energia_kwh'] / area_aviario
    df_consumo_total['kwh_por_ave'] = df_consumo_total['energia_kwh'] / df_consumo_total['aves_abatidas']
    df_consumo_total['kwh_por_kg'] = df_consumo_total['energia_kwh'] / df_consumo_total['peso_total_kg']
    
    # Save the processed data
    df_consumo_total.to_csv('data/processed/analise_eficiencia_energetica.csv', index=False)
    
    # Plot kwh_por_m2
    plt.figure(figsize=(16, 8))
    
    # Sort by 'Fazenda' (aviary) and 'lote' for grouped plotting
    df_consumo_total.sort_values(by=['Fazenda', 'lote'], inplace=True)
    
    # Create color mapping for aviaries
    unique_aviaries = df_consumo_total['Fazenda'].unique()
    num_aviaries = len(unique_aviaries)
    color_map = plt.get_cmap('tab10')
    aviary_color_map = {aviary: color_map(i/num_aviaries) for i, aviary in enumerate(unique_aviaries)}
    
    bar_colors = [aviary_color_map[aviary] for aviary in df_consumo_total['Fazenda']]
    
    x_labels = df_consumo_total['aviario'].astype(str) + '-' + df_consumo_total['lote'].astype(str)
    
    plt.bar(x_labels, df_consumo_total['kwh_por_m2'], color=bar_colors)
    
    plt.xlabel('Aviário-Lote')
    plt.ylabel('Consumo de Energia por m² (kWh/m²)')
    plt.title('Consumo de Energia por m² por Lote, Agrupado por Aviário')
    plt.xticks(rotation=90)
    
    # Create custom legend for aviaries
    from matplotlib.lines import Line2D
    legend_elements = [Line2D([0], [0], color=aviary_color_map[aviary], lw=4, label=f'Aviário {aviary}') for aviary in unique_aviaries]
    plt.legend(handles=legend_elements, title="Aviários")
    
    plt.tight_layout()
    plt.savefig('docs/consumo_por_m2.png')

    # Plot kwh_por_ave (Median per Aviary)
    plt.figure(figsize=(12, 6))
    
    # Group by 'Fazenda' (aviary) and calculate the median of 'kwh_por_ave'
    median_kwh_per_ave_by_aviary = df_consumo_total.groupby('Fazenda')['kwh_por_ave'].median().reset_index()

    plt.bar(median_kwh_per_ave_by_aviary['Fazenda'].astype(str), median_kwh_per_ave_by_aviary['kwh_por_ave'])
    plt.xlabel('Aviário')
    plt.ylabel('Mediana do Consumo de Energia por Ave (kWh/ave)')
    plt.title('Mediana do Consumo de Energia por Ave por Aviário')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('docs/consumo_por_ave.png')
    
    # Plot kwh_por_kg
    plt.figure(figsize=(12, 6))
    df_consumo_total.sort_values(by=['Fazenda', 'lote'], inplace=True)
    bar_colors_kg = [aviary_color_map[aviary] for aviary in df_consumo_total['Fazenda']]
    x_labels_kg = df_consumo_total['aviario'].astype(str) + '-' + df_consumo_total['lote'].astype(str)
    plt.bar(x_labels_kg, df_consumo_total['kwh_por_kg'], color=bar_colors_kg)
    plt.xlabel('Lote-Aviário')
    plt.ylabel('Consumo de Energia por kg (kWh/kg)')
    plt.title('Consumo de Energia por kg por Lote e Aviário')
    plt.xticks(rotation=90)
    plt.legend(handles=legend_elements, title="Aviários")
    plt.tight_layout()
    plt.savefig('docs/consumo_por_kg.png')


if __name__ == '__main__':
    analise_eficiencia_energetica()