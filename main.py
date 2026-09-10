from services.estoque_service import EstoqueService
import os

def limpar_tela():
    os.system("cls")

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
        rodando = True
        while rodando:

            print ()
            nome = input("Informe o nome do cliente ou [0] para RETORNAR AO MENU: ")

            if nome == "0":
                print ()

                certeza = True
                while certeza:
                    certeza = int (input ('''VOLTAR PARA O MENU?
[1] SIM
[2] NÃO
'''))
                    if certeza == 1:
                        rodando = False
                        certeza = False

                    elif certeza == 2:
                        input ("Pressione ENTER para VOLTAR")
                        certeza = False
                        rodando = True

                    else:
                        print ()
                        input ("Erro! CARACTERE INVALIDO. Pressione ENTER para retornar.")
                        certeza = True
                        rodando = True

            else:
                if len(nome) == 0:
                    print ()
                    print ("Erro! O nome não pode estar vazio.")
                    print ()
                    input ("Pressione ENTER para tentar novamente.")
                    print ()

                else:
                    service.cadastrar_cliente(nome)
                    break

    elif opcao == 2:
        service.listar_clientes()

    elif opcao == 3:
        print()
        print("=======BUSCAR CLIENTE=======")
        service.buscar_cliente(ler_inteiro("Informe o código do cliente: "))

    elif opcao == 4:
        rodando = True
        while rodando:

            menu = input ("Informe o código do cliente a ser removido ou [0] para VOLTAR AO MENU: ")
            
            if menu == "0":
                print ()

                certeza = True
                while certeza:

                    certeza = int (input ('''VOLTAR PARA O MENU?
[1] SIM
[2] NÃO
'''))
                    if certeza == 1:
                        rodando = False
                        certeza = False

                    elif certeza == 2:
                        input ("Pressione ENTER para VOLTAR")
                        certeza = False
                        rodando = True

                    else:
                        print ()
                        input ("Erro! CARACTERE INVALIDO. Pressione ENTER para retornar.")
                        certeza = True
                        rodando = True

            else:
                menu = int(menu)
                service.remover_cliente(menu)
                break
        
    elif opcao == 5:
        rodando = True
        while rodando:
            nome = input ("Informe o nome do produto que deseja cadastrar ou [0] para RETORNAR AO MENU: ")

            if nome == "0":
                print ()

                certeza = True
                while certeza:

                    certeza = int (input ('''VOLTAR PARA O MENU?
[1] SIM
[2] NÃO
'''))
                    if certeza == 1:
                        rodando = False
                        certeza = False

                    elif certeza == 2:
                        input ("Pressione ENTER para VOLTAR")
                        certeza = False
                        rodando = True

                    else:
                        print ()
                        input ("Erro! CARACTERE INVALIDO. Pressione ENTER para retornar.")
                        certeza = True
                        rodando = True
                                    
            else:
                print()
                preco = input ("Digite o valor do produto: ")
                print()
                quantidade = input ("Digite a quantidade do produto em estoque: ")

                if len(preco) == 0 or len(quantidade) == 0:
                    print ()
                    print ("Erro! os campos devem ser preenchidos!")
                    input ("Pressione ENTER para retornar")
                    rodando = True
                
                else:
                    preco = float (preco)
                    quantidade = int (quantidade)
                    service.cadastrar_produto(nome, preco, quantidade)
                    break

    elif opcao == 6:
        service.listar_produtos()

    elif opcao == 7:
        print()
        print("=======BUSCAR PRODUTO=======")
        service.buscar_produto(ler_inteiro("Digite o Id do produto que deseja buscar: "))

    elif opcao == 8:
        print()
        print("=======ATUALIZAR QUANTIDADE EM ESTOQUE=======")

        service.listar_produtos()
        
        print()

        rodando = True
        while rodando:
            codigo = int (input ("Digite o código do produto que deseja atualizar ou [0] Para RETORNAR AO MENU: "))
            if codigo == 0:
                print ()

                certeza = True
                while certeza:

                    certeza = int (input ('''VOLTAR PARA O MENU?
[1] SIM
[2] NÃO
'''))
                    if certeza == 1:
                        rodando = False
                        certeza = False

                    elif certeza == 2:
                        input ("Pressione ENTER para VOLTAR")
                        certeza = False
                        rodando = True

                    else:
                        print ()
                        input ("Erro! CARACTERE INVALIDO. Pressione ENTER para retornar.")
                        certeza = True
                        rodando = True
                                            
            else:
                codigo = int (codigo)
                print()
                NovaQuantidade = ler_inteiro("Digite a nova quantidade do produto: ")
                
                retorno = service.atualizar_estoque(codigo, NovaQuantidade)

                if retorno == None:
                    rodando = True
                
                elif retorno == "certo":
                    print()
                    
                    print(f"Produto [{codigo}] Atualizado para {NovaQuantidade} Unidades em estoque")
                    break

    elif opcao == 9:
        rodando = True
        while rodando:
            codigo = input("Informe o código do produto a ser removido ou [0] para RETORNAR AO MENU: ")
            if codigo == "0":
                print ()

                certeza = True
                while certeza:

                    certeza = int (input ('''VOLTAR PARA O MENU?
[1] SIM
[2] NÃO
'''))
                    if certeza == 1:
                        rodando = False
                        certeza = False

                    elif certeza == 2:
                        input ("Pressione ENTER para VOLTAR")
                        certeza = False
                        rodando = True

                    else:
                        print ()
                        input ("Erro! CARACTERE INVALIDO. Pressione ENTER para retornar.")
                        certeza = True
                        rodando = True
                                                
            else:
                if len(codigo) == 0:
                    print ()
                    print ("Erro! O campo de digito não pode estar vazio.")
                    print ()
                    input ("Pressione ENTER para tentar novamente.")
                    print ()

                else:
                    codigo = int (codigo)
                    service.remover_produto(codigo)
                    break

    elif opcao == 10:
        service.listar_produtos_inverso()
        
    elif opcao == 11:
        service.listar_produtos_ordenados_por_id()

    elif opcao == 12:
        print()
        print("=======BUSCAR PRODUTO COM BUSCA BINARIA=======")
        service.buscar_produto_binario(ler_inteiro("Digite o Id do produto que deseja buscar: "))
        
    elif opcao == 13:
        service.realizar_venda_exemplo(ler_inteiro("Informe o código do cliente: "), ler_inteiro("Informe o código do produto: "), ler_inteiro("Informe a quantidade: "))
        

    elif opcao == 14:
        service.listar_vendas()
        

    elif opcao == 15:
        service.primeira_venda()
        

    elif opcao == 16:
        service.valor_total_estoque()
        

    elif opcao == 17:
        service.valor_total_vendas()
        

    elif opcao == 18:
        service.clientes_e_valores_totais_gastos()

    elif opcao == 19:
        service.cliente_que_mais_gastou()
        

    elif opcao == 20:
        service.produto_mais_vendido()

    elif opcao == 21:
        print ()
        certeza = input ('''Você deseja DESFAZER A ULTIMA OPERAÇÃO?: 
[1] -> SIM
[2] -> NÃO, RETORNAR AO MENU
''')
        certeza = int (certeza)
        if certeza == 1:
            service.desfazer_ultima_operacao()

        elif certeza == 2:
            return

        else:
            print ("Erro! OPÇÃO INVÁLIDA, Processo Cancelado!")

    else:
        print("Opcao invalida. Tente novamente.")

def main():
    service = EstoqueService()

    limpar_tela()

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
