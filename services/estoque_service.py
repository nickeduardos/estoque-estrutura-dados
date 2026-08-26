import os

from estruturas.fila import Fila
from estruturas.lde import LDE
from estruturas.lse import LSE
from services.persistencia_service import PersistenciaService
from models.cliente import Cliente
from models.produto import Produto

class EstoqueService:
    def __init__(self):
        pasta_raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        pasta_data = os.path.join(pasta_raiz, "data")

        self.clientes = LSE()
        self.produtos = LDE()
        self.vendas = Fila()
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
        return cliente


    def listar_clientes(self):
        print()
        print("=======LISTA DE CLIENTES=======")
        for cliente in self.clientes.listar():
            print (f"[{cliente.codigo}] - {cliente.nome}")

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
            print(f"Cliente removido -> [{removerCliente.codigo}] - {removerCliente.nome}")
            self.salvar_clientes()
        else:
            print("Cliente não encontrado.")

    def cadastrar_produto(self, nome, preco, quantidade):
        Codigo = self.gerar_proximo_codigo_produto()
        NovoProduto = Produto(Codigo, nome, preco, quantidade)
        print ()
        print (f"Produto cadastrado! {NovoProduto}")
        self.produtos.inserir_fim(NovoProduto)
        self.salvar_produtos()
        return NovoProduto

    def listar_produtos(self):
        print()
        print("=======LISTA DE PRODUTOS=======")
        for produto in self.produtos.listar():
            print (f"Id [{produto.codigo}] - {produto.nome} | {produto.quantidade} unidades em estoque.")

    def listar_produtos_inverso(self):
        pass

    def listar_produtos_ordenados_por_id(self):
        pass

    def buscar_produto(self, codigo):
        BuscarProduto = self.produtos.buscar(codigo)
        if BuscarProduto is not None:
            print ()
            print (f"[{BuscarProduto.codigo}] - {BuscarProduto.nome}")
        else:
            print ()
            print ("Erro! Produto inexistente")

    def buscar_produto_binario(self, codigo):
        pass

    def atualizar_estoque(self, codigo, nova_quantidade):
        pass

    def remover_produto(self, codigo):
        pass

    def realizar_venda_exemplo(self, codigo_cliente, codigo_produto, quantidade):
        pass

    def listar_vendas(self):
        pass

    def primeira_venda(self):
        pass

    def valor_total_estoque(self):
        pass

    def valor_total_vendas(self):
        pass

    def clientes_e_valores_totais_gastos(self):
        pass

    def cliente_que_mais_gastou(self):
        pass

    def produto_mais_vendido(self):
        pass

    def desfazer_ultima_operacao(self):
        pass

    def salvar_clientes(self):
        self.persistencia.salvar_clientes(self.clientes.listar())

    def salvar_produtos(self):
        self.persistencia.salvar_produtos(self.produtos.listar())

    def salvar_vendas(self):
        self.persistencia.salvar_vendas(self.vendas.listar())
