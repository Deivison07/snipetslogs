from openpyxl import Workbook

# Cria um novo workbook (arquivo Excel)
workbook = Workbook()

# Seleciona a planilha ativa (a primeira planilha criada automaticamente)
sheet = workbook.active

# Define o título da planilha (opcional)
sheet.title = "Minha Planilha"

# Dados a serem inseridos (personalize conforme necessário)
dados = [
    ["Produto", "Quantidade", "Preço"],
    ["Maçã", 50, 1.20],
    ["Banana", 100, 0.80],
    ["Laranja", 75, 1.50]
]

# Insere os dados na planilha
for linha in dados:
    sheet.append(linha)

# Salva o novo arquivo Excel
workbook.save("novo_arquivo.xlsx")

print("Novo workbook criado e salvo como 'novo_arquivo.xlsx'.")
