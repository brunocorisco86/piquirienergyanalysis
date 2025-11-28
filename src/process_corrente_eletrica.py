import pandas as pd
import glob

def process_corrente_eletrica():
    """
    This function processes the electric current data.
    """
    path = 'data/raw/corrente_eletrica/corrente_*.csv'
    files = glob.glob(path)

    all_data = []
    for f in files:
        df = pd.read_csv(f, sep=';', skiprows=1, decimal=',')
        all_data.append(df)

    df_final = pd.concat(all_data, ignore_index=True)
    
    # The README says the year is 2025
    df_final['datetime'] = pd.to_datetime(df_final['Data'] + ' ' + df_final['Hora'], format='%d/%m/%Y %H:%M:%S')

    df_final = df_final.sort_values(by='datetime')
    
    df_final = df_final[['datetime', 'Valor', 'Local']]
    df_final = df_final.rename(columns={'Valor': 'corrente', 'Local': 'local'})
    
    df_final.to_csv('data/processed/corrente_eletrica_lote.csv', index=False)

if __name__ == '__main__':
    process_corrente_eletrica()
