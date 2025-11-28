
import pandas as pd
import glob
import os
import matplotlib.pyplot as plt
from datetime import timedelta
import re

def plot_cumulative_consumption_timeseries():
    """
    Generates a time series line chart of the cumulative energy consumption per lot.
    """
    # 1. Read lot metadata
    results_path = 'data/processed/resultado_lotes.xlsx'
    lots_df = pd.read_excel(results_path)
    lots_df['Data do Abate'] = pd.to_datetime(lots_df['Data do Abate'])
    
    # Calculate start date, handling potential non-numeric 'Idade Matriz'
    lots_df['Idade Matriz'] = pd.to_numeric(lots_df['Idade Matriz'], errors='coerce')
    lots_df.dropna(subset=['Idade Matriz'], inplace=True) # Drop rows where age is not a number
    lots_df['start_date'] = lots_df.apply(lambda row: row['Data do Abate'] - timedelta(days=row['Idade Matriz']), axis=1)

    all_lots_data = pd.DataFrame()

    # 2. Iterate through raw data files
    path = 'data/raw/resumo_por_aviario/aviario_*/*.xlsx'
    files = glob.glob(path)

    for file in files:
        try:
            aviario_lote = os.path.basename(file).replace('.xlsx', '')
            
            # Find the corresponding lot in the metadata
            lot_info = lots_df[lots_df['Número Composto'] == aviario_lote]
            if lot_info.empty:
                continue
            
            start_date = lot_info.iloc[0]['start_date']
            fazenda = lot_info.iloc[0]['Fazenda']

            df = pd.read_excel(file, sheet_name=0)

            # Filter for daily data
            daily_df = df[df.iloc[:, 0].astype(str).str.contains('DIA', na=False)].copy()
            
            # Extract day number
            daily_df['day'] = daily_df.iloc[:, 0].apply(lambda x: int(re.search(r'(\d+)º', str(x)).group(1)) if re.search(r'(\d+)º', str(x)) else 0)
            daily_df = daily_df[daily_df['day'] > 0]
            
            # Get consumption value from the column next to 'Energia (kWh)'
            if 'Energia (kWh)' in df.columns:
                energia_col_index = df.columns.get_loc('Energia (kWh)')
                daily_df['consumption'] = pd.to_numeric(daily_df.iloc[:, energia_col_index + 1], errors='coerce')
            else:
                continue

            daily_df.sort_values('day', inplace=True)
            daily_df['cumulative_consumption'] = daily_df['consumption'].cumsum()
            
            # Create date for each entry
            daily_df['date'] = daily_df['day'].apply(lambda d: start_date + timedelta(days=d-1))
            
            daily_df['aviario_lote'] = aviario_lote
            daily_df['Fazenda'] = fazenda
            
            all_lots_data = pd.concat([all_lots_data, daily_df[['date', 'cumulative_consumption', 'aviario_lote', 'Fazenda']]])

        except Exception as e:
            print(f"Error processing file {file}: {e}")

    if all_lots_data.empty:
        print("No data to plot.")
        return

    # Save the processed data
    all_lots_data.to_csv('data/processed/consumo_acumulado_lote.csv', index=False)

    # 3. Plotting
    plt.style.use('seaborn-v0_8-whitegrid')
    fig, ax = plt.subplots(figsize=(15, 8))

    # Get unique aviaries and assign colors
    unique_aviaries = all_lots_data['Fazenda'].unique()
    colors = plt.cm.get_cmap('tab10', len(unique_aviaries))
    aviary_color_map = {aviary: colors(i) for i, aviary in enumerate(unique_aviaries)}

    for i, (name, group) in enumerate(all_lots_data.groupby('aviario_lote')):
        aviary = group['Fazenda'].iloc[0]
        ax.plot(group['date'], group['cumulative_consumption'], label=name, color=aviary_color_map[aviary], alpha=0.7)

    # Create custom legend for aviaries
    from matplotlib.lines import Line2D
    legend_elements = [Line2D([0], [0], color=aviary_color_map[aviary], lw=4, label=f'Aviário {aviary}') for aviary in unique_aviaries]
    ax.legend(handles=legend_elements, title="Aviários")

    plt.title('Consumo de Energia Acumulado por Lote')
    plt.xlabel('Data')
    plt.ylabel('Consumo Acumulado (kWh)')
    fig.autofmt_xdate()
    
    # 4. Save the plot
    output_plot_path = 'docs/consumo_acumulado_lote_timeseries.png'
    plt.savefig(output_plot_path)
    plt.close()

    print(f"Gráfico de série temporal do consumo acumulado salvo em '{output_plot_path}'.")

if __name__ == '__main__':
    plot_cumulative_consumption_timeseries()
