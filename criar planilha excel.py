from openpyxl import Workbook

# Cria um novo arquivo Excel
workbook = Workbook()

# Seleciona a planilha ativa
sheet = workbook.active

# Define o título da planilha
sheet.title = "Dados de Exemplo"

# Dados a serem inseridos (você pode personalizar conforme necessário)
dados = [
    ["Nome", "Idade", "Cidade"],
    ["Alice", 30, "São Paulo"],
    ["Bob", 25, "Rio de Janeiro"],
    ["Carlos", 35, "Belo Horizonte"]
]

# Insere os dados na planilha
for linha in dados:
    sheet.append(linha)

# Salva o arquivo Excel
workbook.save("dados_exemplo.xlsx")

print("Dados inseridos com sucesso na planilha 'dados_exemplo.xlsx'.")
