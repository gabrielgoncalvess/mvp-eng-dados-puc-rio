import pandas as pd

def split_excel_sheets_into_csv(filename):
    # Ler o arquivo Excel
    with pd.ExcelFile(filename) as xls:
        # Para cada aba no arquivo Excel
        for sheet_name in xls.sheet_names:
            # Ler a aba específica
            df = pd.read_excel(xls, sheet_name)
            
            # Salvar a aba como um novo arquivo CSV
            output_filename = f"{sheet_name}.csv"
            df.to_csv(output_filename, index=False)
            print(f"Arquivo {output_filename} criado com sucesso!")

# Utilizando a função
input_filename = 'FATAL ENCOUNTERS DOT ORG SPREADSHEET (See Read me tab).xlsx' # Substitua 'seu_arquivo.xlsx' pelo nome do seu arquivo
split_excel_sheets_into_csv(input_filename)