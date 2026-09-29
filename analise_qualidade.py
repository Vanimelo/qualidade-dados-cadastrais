import pandas as pd

# Carrega as abas da base cadastral original
produtos = pd.read_excel("base_cadastral_original.xlsx", sheet_name="Produtos")
clientes = pd.read_excel("base_cadastral_original.xlsx", sheet_name="Clientes")
fornecedores = pd.read_excel("base_cadastral_original.xlsx", sheet_name="Fornecedores")

# Exibe a quantidade de registros de cada base
print("Quantidade de registros:")
print("Produtos:", len(produtos))
print("Clientes:", len(clientes))
print("Fornecedores:", len(fornecedores))

print("\n--- DUPLICIDADES ---")

# Identifica IDs duplicados
print("\nProdutos:")
print(produtos[produtos.duplicated(subset=["ID Produto"], keep=False)])

print("\nClientes:")
print(clientes[clientes.duplicated(subset=["ID Cliente"], keep=False)])

print("\nFornecedores:")
print(fornecedores[fornecedores.duplicated(subset=["ID Fornecedor"], keep=False)])

print("\n--- CAMPOS VAZIOS ---")

# Conta campos vazios em cada coluna
print("\nProdutos:")
print(produtos.isnull().sum())

print("\nClientes:")
print(clientes.isnull().sum())

print("\nFornecedores:")
print(fornecedores.isnull().sum())
