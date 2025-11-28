import PyPDF2
import pandas as pd
import glob
import re

def extract_custeio_energia():
    """
    This function extracts the energy cost data from the PDF files.
    """
    path = 'assets/SemiDetalhado*.pdf'
    files = glob.glob(path)

    all_data = []
    for f in files:
        year = re.search(r'(\d{4})', f).group(1)
        
        with open(f, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                
                # Use a more general regex to find the line with "ENERGIA ELETRICA"
                match = re.search(r'ENERGIA\s+ELETRICA\s+([\d\.,]+)', text, re.IGNORECASE)
                if match:
                    value_str = match.group(1)
                    value = float(value_str.replace('.', '').replace(',', '.'))
                    all_data.append({'ano': year, 'custo_energia': value})
                    break # Move to next file once value is found

    df = pd.DataFrame(all_data)
    df.to_csv('data/processed/custo_energia.csv', index=False)

if __name__ == '__main__':
    extract_custeio_energia()
