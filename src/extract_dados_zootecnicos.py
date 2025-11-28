import pandas as pd

def extract_dados_zootecnicos():
    """
    This function extracts the zootechnical data from the lots.
    """
    df = pd.read_excel('data/processed/resultado_lotes.xlsx')

    df_processed = df[['Lote', 'Data do Abate', 'Fazenda', 'Aves Alojadas', 'Aves Abatidas', 'GMD']]
    df_processed = df_processed.rename(columns={
        'Lote': 'lote',
        'Data do Abate': 'data_abate',
        'Fazenda': 'aviario',
        'Aves Alojadas': 'aves_alojadas',
        'Aves Abatidas': 'aves_abatidas',
        'GMD': 'peso_medio_kg' # Assuming GMD is the average weight
    })

    df_processed['peso_total_kg'] = df_processed['aves_abatidas'] * df_processed['peso_medio_kg']
    
    df_processed['ano'] = pd.to_datetime(df_processed['data_abate']).dt.year

    df_processed = df_processed.drop(columns=['data_abate'])

    df_processed.to_csv('data/processed/dados_zootecnicos.csv', index=False)

if __name__ == '__main__':
    extract_dados_zootecnicos()
