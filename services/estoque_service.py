import os

from estruturas.fila import Fila
from estruturas.lde import LDE
from estruturas.lse import LSE
from estruturas.pilha import Pilha
from services.persistencia_service import PersistenciaService
from models.cliente import Cliente
from models.produto import Produto
from algoritmos.ordenacao import ordenar_produtos_por_id
from algoritmos.busca_binaria import buscar_produto_por_id
from models.venda import Venda

class EstoqueService:
    def __init__(self):
        pasta_raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        pasta_data = os.path.join(pasta_raiz, "data")

        self.clientes = LSE()
        self.produtos = LDE()
        self.vendas = Fila()
        self.operacoes = Pilha()
        self.persistencia = PersistenciaService(pasta_data)

        self.carregar_dados()

    def carregar_dados(self):
        for cliente in self.persistencia.carregar_clientes():
            if self.clientes.buscar(cliente.codigo) is None:
                self.clientes.inserir_fim(cliente)

        for produto in self.persistencia.carregar_produtos():
            if self.produtos.buscar(produto.codigo) is None:
                self.produtos.inserir_fim(produto)

        for venda in self.persistencia.carregar_vendas():
            self.vendas.enqueue(venda)

    def gerar_proximo_codigo_cliente(self):
        return self._gerar_proximo_codigo(self.clientes.listar())

    def gerar_proximo_codigo_produto(self):
        return self._gerar_proximo_codigo(self.produtos.listar())

    def gerar_proximo_codigo_venda(self):
        return self._gerar_proximo_codigo(self.vendas.listar())

    def _gerar_proximo_codigo(self, registros):
        maior_codigo = 0

        for registro in registros:
            if registro.codigo > maior_codigo:
                maior_codigo = registro.codigo

        return maior_codigo + 1

    def cadastrar_cliente(self, nome):
        codigo=self.gerar_proximo_codigo_cliente()
        cliente=Cliente(codigo, nome)
        self.clientes.inserir_fim(cliente)
        self.salvar_clientes()
        print()
        print("Cliente Cadastrado!")
        self.operacoes.push({
                    "acao" : "cadastrar_cliente",
                    "codigo" : codigo,
                    "nome" : nome
                })
        return cliente


    def listar_clientes(self):
        clientes=self.clientes.listar()

        if len(clientes) == 0:
            print("Nenhum cliente cadastrado até o momento.")
            return

        for cliente in clientes:
            print(f"ID [{cliente.codigo}] - {cliente.nome}")

    def buscar_cliente(self, codigo):
        buscarCliente = self.clientes.buscar(codigo)
        if buscarCliente is not None:
            print()
            print(f"[{buscarCliente.codigo}] - {buscarCliente.nome}")
        else:
            print("Cliente não encontrado.")

    def remover_cliente(self, codigo):
        removerCliente = self.clientes.remover(codigo)
        if removerCliente is not None:
            self.salvar_clientes()
            print(f"Cliente removido -> [{removerCliente.codigo}] - {removerCliente.nome}")
            self.operacoes.push({
                "acao" : "remover_cliente",
                "nome" : removerCliente.nome
            })
            return removerCliente
        else:
            print("Cliente não encontrado.")

    def cadastrar_produto(self, nome, preco = None, quantidade = None):
        produto_existente = self.buscar_produto_por_nome(nome)
        if produto_existente is not None:
            quantidade_adicionada = quantidade
            produto_existente.quantidade += quantidade_adicionada

            self.operacoes.push({

                "acao" : "atualizar_estoque",
                "codigo" : produto_existente.codigo,
                "quantidade" : produto_existente.quantidade - quantidade

            })

            self.salvar_produtos()

            print()
            print(f"Produto informado ({produto_existente.nome}) já cadastrado. A quantidade em estoque foi atualizada para {produto_existente.quantidade} unidades.")

            print(f"Estoque atual de {produto_existente.nome}: {produto_existente.quantidade} unidades.")

            return produto_existente

        Codigo=self.gerar_proximo_codigo_produto()

        NovoProduto= Produto(Codigo, nome, preco, quantidade)

        print()
        print("Produto Cadastrado! {NovoProduto}")

        self.produtos.inserir_fim(NovoProduto)
        self.salvar_produtos()

        self.operacoes.push({

            "acao": "cadastrar_produto",
            "codigo": Codigo,
        })
        return NovoProduto

    def listar_produtos(self):
        produtos=self.produtos.listar()

        if len(produtos) == 0:
            print("Nenhum produto cadastrado até o momento.")
            return

        for produto in produtos:
            print(f"ID [{produto.codigo}] - {produto.nome} | R$ {produto.preco} | {produto.quantidade} unidades em estoque")

    def listar_produtos_inverso(self):
        produtos=self.produtos.listar_inverso()

        if len(produtos) == 0:
            print("Nenhum produto cadastrado até o momento.")
            return
        
        for produto in self.produtos.listar_inverso():
            print (f"ID [{produto.codigo}] - {produto.nome} | {produto.quantidade} unidades em estoque.")
        

    def listar_produtos_ordenados_por_id(self):
        ProdutosOrdenados = ordenar_produtos_por_id(self.produtos.listar())

        if len(ProdutosOrdenados) == 0:
            print("Nenhum produto cadastrado até o momento.")
            return
        
        for produto in ProdutosOrdenados:
            print (f"[{produto.codigo}] -> {produto.nome} | R$ {produto.preco} | {produto.quantidade} unidades em estoque")

    def buscar_produto(self, codigo):
        BuscarProduto = self.produtos.buscar(codigo)
        if BuscarProduto is not None:
            print ()
            print (f"[{BuscarProduto.codigo}] - {BuscarProduto.nome}")
        else:
            print ()
            print ("Erro! Você precisa digitar o Id do produto.")

    def buscar_produto_binario(self, codigo):
        BuscarProduto = buscar_produto_por_id(self.produtos.listar(), codigo)

        if BuscarProduto not in self.produtos.listar():
            print ()
            print ("Erro! Id não cadastrado em nenhum produto.")

        else:
            print()
            print("Produto Encontrado!")
            print (f"[{BuscarProduto.codigo}] - {BuscarProduto.nome}")

    def atualizar_estoque(self, codigo, nova_quantidade):    
        ProdutoBuscado = self.produtos.buscar(codigo)
        Validacao = buscar_produto_por_id (self.produtos.listar(), codigo)

        if Validacao not in self.produtos.listar():
            print ()
            print ("Erro! Não existe nenhum produto cadastrado nesse Id.")
            print ()
            return None

        else:
            QuantidadeAnterior = ProdutoBuscado.quantidade
            ProdutoBuscado.quantidade = nova_quantidade
            self.operacoes.push({
                "acao" : "atualizar_estoque",
                "codigo" : codigo,
                "quantidade" : QuantidadeAnterior
            })
            self.salvar_produtos()
            return "certo"
        
    
    def remover_produto(self, codigo):
        produto_removido = self.produtos.remover(codigo)
        if produto_removido is not None:
            print(f"Produto removido -> [{produto_removido.codigo}] - {produto_removido.nome}")
            
            if produto_removido.quantidade == 0:
                produto_removido.quantidade += 1
                self.operacoes.push({
                                "acao" : "remover_produto",
                                "nome" : produto_removido.nome,
                                "preco" : produto_removido.preco,
                                "quantidade" : produto_removido.quantidade
                            })
                self.salvar_produtos()
                return produto_removido
            
            else:
                self.operacoes.push({
                                "acao" : "remover_produto",
                                "nome" : produto_removido.nome,
                                "preco" : produto_removido.preco,
                                "quantidade" : produto_removido.quantidade
                            })
                self.salvar_produtos()
                return produto_removido

        else:
            print("Produto não encontrado.")

    def realizar_venda_exemplo(self, codigo_cliente, itens):
            
        cliente = self.clientes.buscar(codigo_cliente)

        if cliente is None:
            print("Cliente não encontrado.")
            return None

        itens_venda = []

        for item in itens:
            codigo_produto = item["codigo_produto"]
            quantidade = item["quantidade"]

            produto = self.produtos.buscar(codigo_produto)

            if produto is None:
                print(
                    f"Produto de código {codigo_produto} "
                    f"não encontrado."
                )
                return None

            if quantidade <= 0:
                print(
                    f"Insira uma quantidade válida "
                    f"para o produto {produto.nome}."
                )
                return None

            if quantidade > produto.quantidade:
                print(
                    f"Quantidade em estoque insuficiente para o produto "
                    f"{codigo_produto}. "
                    f"Quantidade em estoque: "
                    f"{produto.quantidade}."
                )
                return None

            for item_existente in itens_venda:
                if item_existente["codigo_produto"] == codigo_produto:
                    print(
                        f"Erro! O produto de código "
                        f"{codigo_produto} já foi "
                        f"adicionado a venda."
                    )
                    return None

            itens_venda.append({
                "codigo_produto": produto.codigo,
                "quantidade": quantidade,
                "preco_unitario": produto.preco
            })

        if len(itens_venda) == 0:
            print("Nenhum item adicionado a venda.")
            return None

        CodigoVenda = self.gerar_proximo_codigo_venda()

        venda = Venda(
            CodigoVenda,
            cliente.codigo,
            itens_venda
        )

        for item in itens_venda:
            produto = self.produtos.buscar(
                item["codigo_produto"]
            )

            produto.quantidade -= item["quantidade"]

        self.vendas.enqueue(venda)

        self.operacoes.push({
            "acao": "realizar_venda_exemplo",
            "codigo_venda": CodigoVenda,
            "codigo_cliente": cliente.codigo,
            "itens": itens_venda
        })

        self.salvar_produtos()
        self.salvar_vendas()

        print(
            f"Venda realizada com sucesso! "
            f"Código da venda: {CodigoVenda}"
        )

        return venda
            

    def listar_vendas(self):
        vendas=self.vendas.listar()

        if len(vendas) == 0:
            print("Nenhuma venda registrada até o momento.")
            return

        for venda in vendas:
            print(f"Venda {venda.codigo} - Cliente [{venda.codigo_cliente}] | Total R$ {venda.valor_total:.2f}")
        

    def primeira_venda(self):
        if self.vendas.is_empty():
            print("=======PRIMEIRA VENDA REGISTRADA=======")
            print()
            print("Não há vendas registradas.")
            return None
        primeira_venda = self.vendas.front()
        print("=======PRIMEIRA VENDA REGISTRADA=======")
        print()
        print(f"venda {primeira_venda.codigo} - Cliente [{primeira_venda.codigo_cliente}] | Total R$ {primeira_venda.valor_total:.2f}")

        return primeira_venda
        

    def valor_total_estoque(self):
        total=0

        for produto in self.produtos.listar():
            total += produto.preco * produto.quantidade

        print("=======VALOR TOTAL EM ESTOQUE=======")
        print()
        print(f"Valor total em estoque: R$ {total:.2f}")

        return total

    def valor_total_vendas(self):
        total=0

        for venda in self.vendas.listar():
            total += venda.valor_total

        print("=======VALOR TOTAL DAS VENDAS=======")
        print()
        print(f"Valor total das vendas: R$ {total:.2f}")

        return total

    def clientes_e_valores_totais_gastos(self):
        clientes=self.clientes.listar()
        print ("=======CLIENTES E VALORES TOTAIS GASTOS=======")
        print ()

        if len(clientes) == 0:
            print("Nenhum cliente cadastrado ou nenhuma venda registrada até o momento.")
            return

        for cliente in self.clientes.listar():
            total=0

            for venda in self.vendas.listar():
                if venda.codigo_cliente == cliente.codigo:
                    total += venda.valor_total

                    print(f"ID [{cliente.codigo}] - {cliente.nome} | Total gasto: R$ {total:.2f}")

    def cliente_que_mais_gastou(self):
        maiorGasto = 0
        clienteMaisGastou = None

        for cliente in self.clientes.listar():
            total=0

            for venda in self.vendas.listar():
                if venda.codigo_cliente == cliente.codigo:
                    total += venda.valor_total
            if total > maiorGasto:
                maiorGasto = total
                clienteMaisGastou = cliente

        if clienteMaisGastou is None:
            print("=======CLIENTE QUE MAIS GASTOU=======")
            print()
            print("Nenhum registro de compra encontrado.")
            return None

        print("=======CLIENTE QUE MAIS GASTOU=======")  
        print()
        print(f"ID [{clienteMaisGastou.codigo}] - {clienteMaisGastou.nome} | Total gasto: R$ {maiorGasto:.2f}")

        return clienteMaisGastou
        

    def produto_mais_vendido(self):
        TotaisVendidos = {}


        for venda in self.vendas.listar():
            for item in venda.itens:
                codigo = item ["codigo_produto"]
                quantidade = item ["quantidade"]

                if codigo in TotaisVendidos:
                    TotaisVendidos[codigo] += quantidade

                else:
                    TotaisVendidos[codigo] = quantidade

        if not TotaisVendidos:
            print ("=======PRODUTO MAIS VENDIDO=======")
            print ()
            print ("Nenhuma venda registrada.")
            return None

        CodigoMaisVendido = None
        MaiorQuantidade = 0

        for codigo, quantidade in TotaisVendidos.items():
            if quantidade > MaiorQuantidade:
                MaiorQuantidade = quantidade
                CodigoMaisVendido = codigo

        ProdutoBuscar = self.produtos.buscar(CodigoMaisVendido)

        print ("=======PRODUTO MAIS VENDIDO=======")
        print()

        if ProdutoBuscar is not None:
            print (f"ID [{ProdutoBuscar.codigo}] - {ProdutoBuscar.nome} | Total Vendido: {MaiorQuantidade} Unidades")

        else:
            print (f"Codigo do produto: {CodigoMaisVendido} | Total Vendido: {MaiorQuantidade} unidades (Produto não encontrado no estoque)")
            
        return ProdutoBuscar

    def desfazer_ultima_operacao(self):
        if self.operacoes.is_empty():
            print("Não há operações recentes para desfazer")
            return None

        UltimaOperação = self.operacoes.pop()


        print ()
        print ("=======DESFAZENDO OPERAÇÃO=======")
        
        if UltimaOperação["acao"] == "cadastrar_cliente":
            print ()
            self.remover_cliente(UltimaOperação["codigo"])
            print ("Ação Desfeita: O ultimo cliente CADASTRADO foi REMOVIDO.")

        elif UltimaOperação["acao"] == "remover_cliente":
            print ()
            self.cadastrar_cliente(UltimaOperação["nome"])
            print ("Ação Desfeita -> O ultimo cliente REMOVIDO  do sistema foi CADASTRADO novamente.")

        elif UltimaOperação["acao"] == "cadastrar_produto":
            self.remover_produto(UltimaOperação["codigo"])
            print ("Ação Desfeita -> O ultimo produto CADASTRADO foi REMOVIDO")

        elif UltimaOperação["acao"] == "remover_produto":
            nome = UltimaOperação["nome"]
            preco = UltimaOperação["preco"]
            quantidade = UltimaOperação["quantidade"]
            print ()
            self.cadastrar_produto(nome, preco, quantidade)
            print ("Ação Desfeita -> O ultimo Produto REMOVIDO foi CADASTRADO novamente.")  

        elif UltimaOperação["acao"] == "atualizar_estoque":
            codigo = UltimaOperação["codigo"]
            quantidade = UltimaOperação["quantidade"]
            produto = self.produtos.buscar(codigo)

            if produto is not None:
                quantidade_atual = produto.quantidade
                produto.quantidade = quantidade

                self.operacoes.push({

                    "acao": "atualizar_estoque",
                    "codigo": codigo,
                    "quantidade": quantidade_atual

                })

                self.salvar_produtos()

            print()
            print ("Ação Desfeita -> foi RETORNADA a quantidade ANTERIOR do ultimo produto que teve a sua quantidade atualizada.")

        elif UltimaOperação["acao"] == "realizar_venda_exemplo":
            for item in UltimaOperação["itens"]:
                produto= self.produtos.buscar(item["codigo_produto"])

                if produto is not None:
                    produto.quantidade += item["quantidade"]

            VendasAtualizadas = Fila()

            for venda in self.vendas.listar():
                if venda.codigo != UltimaOperação["codigo_venda"]:
                    VendasAtualizadas.enqueue(venda)

            self.vendas = VendasAtualizadas

            self.salvar_produtos()
            self.salvar_vendas()

            self.operacoes.push({
                "acao": "remover_venda",
                "codigo_venda": UltimaOperação["codigo_venda"],
                "cliente_codigo": UltimaOperação["codigo_cliente"],
                "itens": UltimaOperação["itens"]
            })
            print ("Ação Desfeita -> A ultima venda realizada foi REMOVIDA do sistema e o estoque dos produtos foi RESTAURADO.")

        elif UltimaOperação["acao"] == "remover_venda":
            codigo_venda = UltimaOperação["codigo_venda"]
            cliente_codigo = UltimaOperação["cliente_codigo"]
            itens = UltimaOperação["itens"]

            venda = Venda(codigo_venda, cliente_codigo, itens)

            self.vendas.enqueue(venda)

            for item in itens:
                produto = self.produtos.buscar(item["codigo_produto"])

                if produto is not None:
                    produto.quantidade -= item["quantidade"]

            self.salvar_produtos()
            self.salvar_vendas()

            self.operacoes.push({
                "acao": "realizar_venda_exemplo",
                "codigo_venda": codigo_venda,
                "codigo_cliente": cliente_codigo,
                "itens": itens
            })

            print()

            print("Ação Desfeita -> A ultima venda removida foi RESTAURADA no sistema e o estoque dos produtos foi ATUALIZADO.")
           

    def salvar_clientes(self):
        self.persistencia.salvar_clientes(self.clientes.listar())

    def salvar_produtos(self):
        self.persistencia.salvar_produtos(self.produtos.listar())

    def salvar_vendas(self):
        self.persistencia.salvar_vendas(self.vendas.listar())


    def verificar_item_venda(self,codigo_produto,quantidade):
        produto = self.produtos.buscar(codigo_produto)

        if produto is None:
            print(f"Erro!!! Produto de código {codigo_produto} não cadastrado.")
            return False

        if quantidade <=0:
            print(f"Erro!!! Insira uma quantidade válida para o produto {produto.nome}.")
            return False

        if quantidade > produto.quantidade:
            print(f"Erro!!! Quantidade em estoque insuficiente para o produto {codigo_produto}. Quantidade em estoque: {produto.quantidade}.")
            return False

        return True

    def buscar_produto_por_nome(self,nome):
        for produto in self.produtos.listar():
            if produto.nome.strip().lower() == nome.strip().lower():
                return produto
        return None

    def alfabeto(self):
        alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        return alfabeto