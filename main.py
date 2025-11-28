from src.extract_resumo_aviario import extract_resumo_aviario
from src.extract_custeio_energia import extract_custeio_energia
from src.extract_dados_zootecnicos import extract_dados_zootecnicos
from src.process_corrente_eletrica import process_corrente_eletrica
from src.analise_consumo_diario import analise_consumo_diario
from src.analise_consumo_total import analise_consumo_total
from src.analise_eficiencia_energetica import analise_eficiencia_energetica
from src.analise_corrente_diaria import analise_corrente_diaria, analise_corrente_maxima
from src.estimativa_consumo_diario import estimativa_consumo_diario
from src.analise_detalhada_consumo import BESS_detailed_analysis_by_year_and_aviary
from src.plot_consumo_medio_por_aviario import plot_average_consumption_by_aviary_and_year
from src.plot_consumo_acumulado_lote import plot_cumulative_consumption_timeseries

def main():
    """
    Main function to run the entire data processing and analysis pipeline.
    """
    print("Starting data extraction and processing...")
    extract_resumo_aviario()
    extract_custeio_energia()
    extract_dados_zootecnicos()
    process_corrente_eletrica()
    print("Data extraction and processing complete.")

    print("Starting data analysis...")
    analise_consumo_diario()
    analise_consumo_total()
    analise_eficiencia_energetica()
    analise_corrente_diaria()
    analise_corrente_maxima()
    estimativa_consumo_diario()
    BESS_detailed_analysis_by_year_and_aviary()
    plot_average_consumption_by_aviary_and_year()
    plot_cumulative_consumption_timeseries()
    print("Data analysis complete. Plots saved in the 'docs' directory.")

if __name__ == '__main__':
    main()
