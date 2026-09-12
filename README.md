# Trabalho Para a disciplina de Organização e Abstração na Programação.

ALUNOS

RA / NOME

1139745 - Nick Eduardo dos Santos

1139819 - Lucas Gazolla

1139685 - Endrewell Favaretto

1139541 - Gustavo Durante

```markdown
# Sistema de Controle de Estoque e Vendas (Estruturas de Dados)

Este projeto é um sistema completo de gerenciamento de estoque, cadastro de clientes e controle de vendas desenvolvido em **Python** como trabalho avaliativo da disciplina de **Estrutura de Dados**. 

O programa opera via interface de linha de comando (terminal) e aplica **estruturas de dados encadeadas criadas do zero** para gerenciamento de dados em memória, integrando persistência automática em arquivos `.csv`.

---

## Funcionalidades do Sistema

### Gestão de Clientes
- **Cadastrar Cliente**: Adiciona novos clientes gerando código sequencial automático (`1, 2, 3...`).
- **Listar Clientes**: Exibe todos os clientes cadastrados armazenados na **Lista Simplesmente Encadeada (LSE)**.
- **Buscar Cliente**: Pesquisa cliente por código ou nome.
- **Remover Cliente**: Exclui o cliente da LSE e atualiza os registros.

### Gestão de Produtos e Estoque
- **Cadastrar Produto**: Registra produtos com nome, preço e quantidade com código sequencial automático.
- **Listar Produtos**: Exibe produtos armazenados na **Lista Duplamente Encadeada (LDE)**.
- **Listar Produtos em Ordem Inversa**: Percorre a LDE do fim para o início utilizando os ponteiros anteriores (`anterior`).
- **Buscar Produto**: Consulta produtos por código ou nome.
- **Atualizar Estoque**: Realiza entradas e saídas de itens no estoque.
- **Remover Produto**: Exclui produto da LDE.
- **Listar Produtos Ordenados por ID**: Ordena os produtos utilizando o algoritmo **Insertion Sort** manual.
- **Busca Binária por ID**: Localiza produtos rapidamente por código após ordenação.

### Gestão de Vendas
- **Realizar Venda**: Processa vendas com suporte a múltiplos itens, verificação e baixa automática de estoque, validação de cliente e cálculo do valor total.
- **Fila de Vendas**: Registra e exibe o histórico de vendas na ordem de realização utilizando uma **Fila (FIFO)**.
- **Visualizar Primeira Venda**: Consulta o primeiro elemento da fila de vendas (*peek*).

### Relatórios e Indicadores
- **Valor Total do Estoque**: Soma do valor acumulado (`preço × quantidade`) de todos os produtos em estoque.
- **Valor Total das Vendas**: Faturamento acumulado de todas as vendas processadas.
- **Gastos por Cliente**: Relatório detalhado dos valores totais consumidos por cada cliente.
- **Cliente que Mais Gastou**: Identificação do cliente com maior volume financeiro de compras.
- **Produto Mais Vendido**: Ranking e exibição do item com maior quantidade de unidades vendidas.

### Controle de Operações e Navegação
- **Desfazer Última Operação (Undo)**: Reverte ações recentes (cadastros, remoções, alterações de estoque ou vendas) utilizando uma **Pilha (LIFO)**.
- **Retorno ao Menu**: Permite ao usuário cancelar ou voltar ao menu principal a qualquer momento caso selecione uma opção por engano.

---

## Estruturas de Dados Utilizadas

Conforme os requisitos do trabalho, as estruturas de dados nativas do Python (como listas) são restritas a operações auxiliares ou de persistência. Todas as regras principais de armazenamento em memória utilizam estruturas encadeadas próprias:

| Estrutura | Aplicação no Sistema | Arquivo |
| :--- | :--- | :--- |
| **LSE (Lista Simplesmente Encadeada)** | Armazenamento e manipulação de **Clientes** | `estruturas/lse.py` |
| **LDE (Lista Duplamente Encadeada)** | Armazenamento de **Produtos** (permite travessia direta e inversa) | `estruturas/lde.py` |
| **Fila (FIFO - First In, First Out)** | Registro cronológico do histórico de **Vendas** | `estruturas/fila.py` |
| **Pilha (LIFO - Last In, First Out)** | Histórico de ações para a funcionalidade **Desfazer** | `estruturas/pilha.py` |

---

## Algoritmos Implementados

- **Insertion Sort (`algoritmos/ordenacao.py`)**: Algoritmo de ordenação por inserção implementado manualmente (sem utilizar funções nativas como `sort()` ou `sorted()`) para ordenar os produtos pelo ID.
- **Busca Binária (`algoritmos/busca_binaria.py`)**: Algoritmo de busca binária ($O(\log n)$) para localização rápida de produtos na coleção previamente ordenada.

---

## Persistência em Arquivos CSV

O sistema realiza a leitura dos arquivos ao iniciar e salva automaticamente qualquer alteração válida nos arquivos `.csv` localizados na pasta `data/`.

### Formato e Contrato dos Arquivos CSV:
1. **`data/clientes.csv`**: `codigo,nome`
2. **`data/produtos.csv`**: `codigo,nome,preco,quantidade`
3. **`data/vendas.csv`**: `codigo,codigo_cliente,itens,valor_total`
   - *Estrutura do campo `itens`*: `codigo_produto:quantidade:preco_unitario` (múltiplos itens separados por `|`). Exemplo: `2:1:18.9|4:3:1.2`.

---

## Estrutura do Projeto

```text
estoque-estrutura-dados/
├── main.py                    # Menu principal e fluxo do terminal
├── models/                    # Classes de domínio (Cliente, Produto, Venda)
│   ├── cliente.py
│   ├── produto.py
│   └── venda.py
├── estruturas/                # Estruturas de dados próprias
│   ├── nodo.py                # Nodo simples (LSE, Fila, Pilha)
│   ├── dnodo.py               # Nodo duplo (LDE)
│   ├── lse.py                 # Lista Simplesmente Encadeada
│   ├── lde.py                 # Lista Duplamente Encadeada
│   ├── fila.py                # Fila (FIFO)
│   └── pilha.py               # Pilha (LIFO)
├── algoritmos/                # Algoritmos manuais
│   ├── ordenacao.py           # Insertion Sort
│   └── busca_binaria.py       # Busca Binária
├── services/                  # Regras de negócio e persistência
│   ├── estoque_service.py     # Lógica central do sistema
│   └── persistencia_service.py# Leitura e escrita dos CSVs
└── data/                      # Arquivos de banco de dados
    ├── clientes.csv
    ├── produtos.csv
    └── vendas.csv

```

---

## Como Executar o Projeto

### Pré-requisitos

* Python 3.8 ou superior instalado.

### Passo a Passo

1. Navegue até a pasta do projeto:

```bash
cd estoque-estrutura-dados

```

2. Execute o programa:

```bash
python main.py
# ou
python3 main.py

```

---

## Opções do Menu Terminal

```text
==================================================
           SISTEMA DE CONTROLE DE ESTOQUE
==================================================
1  - Cadastrar cliente
2  - Listar clientes
3  - Buscar cliente
4  - Remover cliente
5  - Cadastrar produto
6  - Listar produtos
7  - Buscar produto
8  - Atualizar estoque
9  - Remover produto
10 - Listar produtos em ordem inversa
11 - Listar produtos ordenados por ID
12 - Buscar produto por ID usando Busca Binaria
13 - Realizar venda
14 - Visualizar fila de vendas
15 - Visualizar primeira venda da fila
16 - Exibir valor total do estoque
17 - Exibir valor total das vendas
18 - Exibir clientes e valores totais gastos
19 - Exibir cliente que mais gastou
20 - Exibir produto mais vendido
21 - Desfazer ultima operacao
0  - Sair
==================================================

```
