# 🤖 Automação de Cadastro de Produtos com PyAutoGUI (RPA)

Este projeto é uma solução de **Automação de Processos (RPA - Robotic Process Automation)** desenvolvida em Python. O sistema lê uma base de dados de produtos em formato CSV e realiza o cadastro automático de cada item em um formulário Web.

## 🎯 Funcionalidades Principais

- **Automação de Interface (GUI):** Abertura automática do navegador, acesso ao sistema da empresa e autenticação de login.
- **Leitura de Dados:** Integração com a biblioteca `Pandas` para ler e manipular os dados do arquivo `produtos.csv`.
- **Preenchimento de Formulários:** Navegação automatizada entre os campos (código, marca, tipo, categoria, preços e observações) através do `PyAutoGUI`.
- **Tratamento de Dados Opcionais:** Verificação de campos vazios (`NaN`) para garantir que dados incompletos não causem falhas no cadastro.

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python
- **Automação RPA:** PyAutoGUI
- **Análise de Dados:** Pandas

## 🚀 Como Executar o Projeto

1. Clone o repositório:
   ```bash
   git clone [https://github.com/SEU-USUARIO/automacao-cadastro-produtos.git](https://github.com/SEU-USUARIO/automacao-cadastro-produtos.git)
   cd automacao-cadastro-produtos
