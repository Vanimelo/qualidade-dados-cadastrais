# 📊 Qualidade de Dados Cadastrais

Projeto desenvolvido para aplicar conceitos de análise, tratamento, padronização e qualidade de dados utilizando **Microsoft Excel e Python**.

A base utilizada contém dados fictícios de **produtos, clientes e fornecedores**, com inconsistências inseridas para simular problemas encontrados em bases cadastrais reais.

## 🎯 Objetivo

Identificar, analisar e tratar problemas de qualidade de dados que podem impactar relatórios, indicadores, integrações entre sistemas e processos de negócio.

O projeto também utiliza Python para automatizar parte das validações realizadas inicialmente no Excel.

## 🔎 Análise realizada

Foram analisados **42 registros** distribuídos entre as bases de:

- Produtos
- Clientes
- Fornecedores

Durante a análise foram identificadas **37 inconsistências**.

| Tipo de inconsistência | Quantidade |
|---|---:|
| Duplicidades | 3 |
| Campos vazios | 10 |
| Falta de padronização | 18 |
| Formatos inválidos | 2 |
| Valores inválidos | 3 |
| Valores inconsistentes | 1 |
| **Total** | **37** |

## ⚠️ Problemas encontrados

Entre os problemas identificados estavam:

- Registros duplicados
- Campos obrigatórios sem preenchimento
- IDs fora do padrão
- Categorias e status escritos de formas diferentes
- CPF fora do padrão definido
- Telefones sem padronização ou com valores inválidos
- E-mails com formato inválido
- UF preenchida incorretamente
- Valores de preço negativos
- Diferenças de maiúsculas, minúsculas e acentuação

## 🧹 Tratamento dos dados

Após a análise, foi criada uma versão tratada da base.

As principais ações realizadas foram:

- Remoção de registros duplicados
- Padronização de textos
- Correção de IDs
- Padronização de categorias e status
- Padronização de UF, cidade, CPF, telefone e e-mail
- Identificação de campos vazios para validação
- Identificação e correção de valores inválidos ou inconsistentes

## 🐍 Automação com Python

Após a análise no Excel, foi desenvolvido um script em Python utilizando a biblioteca **pandas**.

O script realiza automaticamente verificações de:

- Duplicidades
- Campos vazios
- Falta de padronização
- Formatos inválidos
- Valores inválidos
- Valores inconsistentes

O resultado da análise automatizada confirmou:

- **42 registros analisados**
- **37 inconsistências identificadas**

## 📈 Indicadores de qualidade

Foi criada uma área de análise no Excel para consolidar os principais indicadores de qualidade dos dados e facilitar a visualização das inconsistências encontradas.

Também foi criado um gráfico para apresentar a distribuição dos problemas identificados na base cadastral.

## 🛠️ Tecnologias utilizadas

- Microsoft Excel
- Python
- pandas
- openpyxl
- Google Colab
- GitHub

## 📁 Estrutura do projeto

```text
qualidade-dados-cadastrais/
│
├── README.md
├── analise_qualidade.py
├── base_cadastral_original.xlsx
├── base_cadastral_tratada.xlsx
└── requirements.txt
