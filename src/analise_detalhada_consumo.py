
import pandas as pd
import glob
import os
import matplotlib.pyplot as plt

def BESS_detailed_analysis_by_year_and_aviary():
    """
    Performs a detailed analysis of energy consumption, including consumption per bird,
    grouped by year and aviary.
    """
    # Path to the raw data files
    path = 'data/raw/resumo_por_aviario/aviario_*/*.xlsx'
    files = glob.glob(path)
    
    consumption_data = []

    for file in files:
        try:
            df = pd.read_excel(file, sheet_name=0)
            acumulado_row = df[df.iloc[:, 0].astype(str).str.contains('ACUMULADO DO LOTE:', na=False)]
            
            if not acumulado_row.empty:
                if 'Energia (kWh)' in df.columns:
                    energia_col_index = df.columns.get_loc('Energia (kWh)')
                    total_consumption = acumulado_row.iloc[0, energia_col_index + 1]

                    aviario_lote = os.path.basename(file).replace('.xlsx', '')
                    
                    consumption_data.append({
                        'Número Composto': aviario_lote,
                        'total_consumption': total_consumption,
                    })
        except Exception as e:
            print(f"Error processing file {file}: {e}")

    if not consumption_data:
        print("No consumption data found.")
        return

    consumption_df = pd.DataFrame(consumption_data)

    # Read the results file
    results_path = 'data/processed/resultado_lotes.xlsx'
    results_df = pd.read_excel(results_path)

    # Merge the dataframes
    merged_df = pd.merge(consumption_df, results_df, on='Número Composto', how='left')
    
    #
    # Filter out rows where 'Aves Abatidas' is NaN or zero to avoid division by zero
    merged_df = merged_df.dropna(subset=['Aves Abatidas'])
    merged_df = merged_df[merged_df['Aves Abatidas'] > 0]


    # Extract year from 'Data do Abate'
    merged_df['year'] = pd.to_datetime(merged_df['Data do Abate']).dt.year

    # Calculate consumption per bird
    merged_df['consumo_por_ave'] = merged_df['total_consumption'] / merged_df['Aves Abatidas']
    
    # Group by year and aviary
    analysis = merged_df.groupby(['year', 'Fazenda']).agg(
        consumo_medio=('total_consumption', 'mean'),
        consumo_medio_por_ave=('consumo_por_ave', 'mean')
    ).reset_index()

    # Save the result
    output_csv_path = 'data/processed/analise_detalhada_consumo.csv'
    analysis.to_csv(output_csv_path, index=False)

    print(f"Análise detalhada do consumo concluída. Resultados salvos em '{output_csv_path}'.")

if __name__ == '__main__':
    BESS_detailed_analysis_by_year_and_aviary()
