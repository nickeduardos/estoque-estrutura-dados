from services.estoque_service import EstoqueService
import os

def ler_inteiro(mensagem):
    valor = input(mensagem)
    return int(valor)

def ler_float(mensagem):
    valor = input(mensagem).replace(",", ".")
    return float(valor)

def pausar():
    input("\nPressione ENTER para continuar...")

def imprimir_registros(registros, mensagem_vazia):
    if len(registros) == 0:
        print(mensagem_vazia)
        return

    for registro in registros:
        print(registro)

def mostrar_menu():
    print("\n==============================")
    print("SISTEMA DE ESTOQUE E VENDAS")
    print("==============================")
    print("1 - Cadastrar cliente")
    print("2 - Listar clientes")
    print("3 - Buscar cliente")
    print("4 - Remover cliente")
    print("5 - Cadastrar produto")
    print("6 - Listar produtos")
    print("7 - Buscar produto")
    print("8 - Atualizar estoque")
    print("9 - Remover produto")
    print("10 - Listar produtos em ordem inversa")
    print("11 - Listar produtos ordenados por ID")
    print("12 - Buscar produto por ID usando Busca Binaria")
    print("13 - Realizar venda simples de exemplo")
    print("14 - Visualizar fila de vendas")
    print("15 - Visualizar primeira venda da fila")
    print("16 - Exibir valor total do estoque")
    print("17 - Exibir valor total das vendas")
    print("18 - Exibir clientes e valores totais gastos")
    print("19 - Exibir cliente que mais gastou")
    print("20 - Exibir produto mais vendido")
    print("21 - Desfazer ultima operacao")
    print("0 - Sair")


def executar_opcao(opcao, service):
    if opcao == 1:
        nome = input("Informe o nome do cliente: ")
        service.cadastrar_cliente(nome)

    elif opcao == 2:
        service.listar_clientes()

    elif opcao == 3:
        print()
        print("=======BUSCAR CLIENTE=======")
        service.buscar_cliente(ler_inteiro("Informe o código do cliente: "))

    elif opcao == 4:
        service.remover_cliente(ler_inteiro("Informe o código do cliente a ser removido: "))
        
    elif opcao == 5:
        NomeProduto = input ("Informe o nome do produto que deseja cadastrar: ")
        print()
        Preco = float (input ("Digite o valor do produto: "))
        print()
        Quantidade = int (input ("Digite a quantidade do produto em estoque: "))

        service.cadastrar_produto(NomeProduto, Preco, Quantidade)

    elif opcao == 6:
        service.listar_produtos()

    elif opcao == 7:
        pass

    elif opcao == 8:
        pass

    elif opcao == 9:
        pass

    elif opcao == 10:
        pass

    elif opcao == 11:
        pass

    elif opcao == 12:
        pass

    elif opcao == 13:
        pass

    elif opcao == 14:
        pass

    elif opcao == 15:
        pass

    elif opcao == 16:
        pass

    elif opcao == 17:
        pass

    elif opcao == 18:
        pass

    elif opcao == 19:
        pass

    elif opcao == 20:
        pass

    elif opcao == 21:
        pass

    else:
        print("Opcao invalida. Tente novamente.")

def main():
    service = EstoqueService()

    os.system("cls")

    while True:
        mostrar_menu()

        print()

        try:
            opcao = ler_inteiro("Escolha uma opcao: ")

            if opcao == 0:
                print("Sistema encerrado.")
                break


            executar_opcao(opcao, service)

        except ValueError as erro:
            print(f"Erro: {erro}")
        except IndexError as erro:
            print(f"Erro: {erro}")
        except NotImplementedError as erro:
            print(f"Funcionalidade para completar: {erro}")

        pausar()

if __name__ == "__main__":
    main()
