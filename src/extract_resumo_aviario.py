import pandas as pd
import glob
import re

def extract_resumo_aviario():
    """
    This function extracts the energy consumption data from the summary files by aviary.
    """
    path = 'data/raw/resumo_por_aviario/aviario_*/*.xlsx'
    files = glob.glob(path)

    all_data = []
    for f in files:
        df = pd.read_excel(f)
        df.columns = df.columns.str.strip()
        
        aviario = f.split('/')[-2].split('_')[-1]
        lote = f.split('/')[-1].split('.')[0].split('-')[-1]
        
        df['aviario'] = aviario
        df['lote'] = lote

        all_data.append(df)

    df_final = pd.concat(all_data, ignore_index=True)

    df_final = df_final[['aviario', 'lote', 'Semanas', 'Energia (kWh)']]
    df_final = df_final.rename(columns={'Semanas': 'dia', 'Energia (kWh)': 'energia_kwh'})

    df_final['dia'] = df_final['dia'].astype(str).str.extract(r'(\d+)').fillna(0).astype(int)
    
    df_final = df_final[df_final['dia'] > 0]

    df_final = df_final.dropna(subset=['energia_kwh'])
    
    df_final.to_csv('data/processed/consumo_energia_por_lote.csv', index=False)

if __name__ == '__main__':
    extract_resumo_aviario()
