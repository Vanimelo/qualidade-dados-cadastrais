import pandas as pd

# ============================================================
# PROJETO: QUALIDADE DE DADOS CADASTRAIS
# Análise automática de produtos, clientes e fornecedores
# ============================================================

# Carregamento das bases
produtos = pd.read_excel(
    "base_cadastral_original.xlsx",
    sheet_name="Produtos"
)

clientes = pd.read_excel(
    "base_cadastral_original.xlsx",
    sheet_name="Clientes"
)

fornecedores = pd.read_excel(
    "base_cadastral_original.xlsx",
    sheet_name="Fornecedores"
)


# ============================================================
# 1. REGISTROS ANALISADOS
# ============================================================

registros_analisados = (
    len(produtos)
    + len(clientes)
    + len(fornecedores)
)


# ============================================================
# 2. DUPLICIDADES
# ============================================================

duplicidades = (
    produtos.duplicated(subset=["ID Produto"]).sum()
    + clientes.duplicated(subset=["ID Cliente"]).sum()
    + fornecedores.duplicated(subset=["ID Fornecedor"]).sum()
)


# ============================================================
# 3. CAMPOS VAZIOS
# ============================================================

campos_vazios = (
    produtos.isnull().sum().sum()
    + clientes.isnull().sum().sum()
    + fornecedores.isnull().sum().sum()
)


# ============================================================
# 4. FALTA DE PADRONIZAÇÃO
# ============================================================

# Produtos
pad_produtos = 0

pad_produtos += produtos["Categoria"].isin(
    ["informatica", "INFORMATICA"]
).sum()

pad_produtos += (
    ~produtos["Status"]
    .fillna("")
    .isin(["Ativo", "Inativo", ""])
).sum()

pad_produtos += (
    ~produtos["ID Produto"]
    .astype(str)
    .str.match(r"^PRD\d{3}$")
).sum()

pad_produtos += (
    produtos["Fornecedor"].fillna("") == "Data storage"
).sum()


# Clientes
pad_clientes = 0

cpf = clientes["CPF"].fillna("").astype(str)

pad_clientes += (
    (cpf != "")
    & (~cpf.str.match(r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"))
).sum()

email_cliente = clientes["E-mail"].fillna("").astype(str)

pad_clientes += (
    (email_cliente != "")
    & (email_cliente != email_cliente.str.lower())
).sum()

pad_clientes += (
    clientes["Telefone"]
    .fillna("")
    .astype(str)
    .isin(["11987654321", "11 98888-7777"])
).sum()

pad_clientes += (
    clientes["UF"].fillna("") == "sp"
).sum()

pad_clientes += (
    ~clientes["ID Cliente"]
    .astype(str)
    .str.match(r"^CLI\d{3}$")
).sum()

pad_clientes += (
    ~clientes["Status"]
    .fillna("")
    .isin(["Ativo", "Inativo", ""])
).sum()


# Fornecedores
pad_fornecedores = 0

pad_fornecedores += (
    fornecedores["Segmento"]
    .fillna("")
    .isin(["tecnologia", "TECNOLOGIA"])
).sum()

pad_fornecedores += (
    fornecedores["Cidade"].fillna("") == "Sao Paulo"
).sum()

pad_fornecedores += (
    fornecedores["UF"].fillna("") == "sp"
).sum()

pad_fornecedores += (
    ~fornecedores["Status"]
    .fillna("")
    .isin(["Ativo", "Inativo", ""])
).sum()


falta_padronizacao = (
    pad_produtos
    + pad_clientes
    + pad_fornecedores
)


# ============================================================
# 5. FORMATOS INVÁLIDOS
# ============================================================

email_clientes_invalido = (
    (clientes["E-mail"].fillna("") != "")
    & (
        ~clientes["E-mail"]
        .fillna("")
        .str.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
    )
).sum()

email_fornecedores_invalido = (
    (fornecedores["E-mail"].fillna("") != "")
    & (
        ~fornecedores["E-mail"]
        .fillna("")
        .str.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
    )
).sum()

formatos_invalidos = (
    email_clientes_invalido
    + email_fornecedores_invalido
)


# ============================================================
# 6. VALORES INVÁLIDOS
# ============================================================

precos_invalidos = (
    pd.to_numeric(
        produtos["Preço"],
        errors="coerce"
    ) <= 0
).sum()

telefone_cliente_invalido = (
    clientes["Telefone"].fillna("") == "abc123"
).sum()

telefone_fornecedor_invalido = (
    fornecedores["Telefone"].fillna("") == "telefone"
).sum()

valores_invalidos = (
    precos_invalidos
    + telefone_cliente_invalido
    + telefone_fornecedor_invalido
)


# ============================================================
# 7. VALORES INCONSISTENTES
# ============================================================

valores_inconsistentes = (
    clientes["UF"].fillna("") == "São Paulo"
).sum()


# ============================================================
# 8. TOTAL DE INCONSISTÊNCIAS
# ============================================================

total_inconsistencias = (
    duplicidades
    + campos_vazios
    + falta_padronizacao
    + formatos_invalidos
    + valores_invalidos
    + valores_inconsistentes
)


# ============================================================
# RESULTADO
# ============================================================

print("===== RESUMO DA QUALIDADE DOS DADOS =====")

print("\nRegistros analisados:", registros_analisados)

print("\nDuplicidades:", duplicidades)
print("Campos vazios:", campos_vazios)
print("Falta de padronização:", falta_padronizacao)
print("Formato inválido:", formatos_invalidos)
print("Valores inválidos:", valores_invalidos)
print("Valores inconsistentes:", valores_inconsistentes)

print("\nTOTAL DE INCONSISTÊNCIAS:", total_inconsistencias)
