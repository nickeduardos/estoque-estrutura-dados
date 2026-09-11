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
    limpar_tela()
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
            limpar_tela()
            print ("=======CADASTRAR CLIENTE=======")
            nome = input ("Informe o nome do cliente ou [0] para RETORNAR AO MENU: ")

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
        limpar_tela()
        print ("=======LISTA DE CLIENTES=======")
        print()
        service.listar_clientes()


    elif opcao == 3:
        limpar_tela()
        print ("=======BUSCAR CLIENTE=======")
        service.buscar_cliente(ler_inteiro("Informe o código do cliente: "))


    elif opcao == 4:
        rodando = True
        while rodando:
            limpar_tela()
            print ("=======REMOVER CLIENTE=======")
            print ()
            service.listar_clientes()
            menu = input ("Informe o ID do cliente a ser removido ou [0] para VOLTAR AO MENU: ")
            
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

            limpar_tela()

            print ("=======CADASTRAR PRODUTO=======")

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

                produto_existente = service.buscar_produto_por_nome(nome)

                if produto_existente is not None:

                    quantidade = input(f"Produto [{produto_existente.nome}] disponível em estoque. Informe a quantidade a ser adicionada: ")

                    if len(quantidade) == 0:

                        print()

                        print("Erro! os campos devem ser preenchidos.")

                        input("Pressione ENTER para retornar")

                        rodando = True

                    else:

                        quantidade = int(quantidade)

                        service.cadastrar_produto(
                            nome,
                            quantidade=quantidade
                        )

                        break

                else:

                    preco = input("Digite o preço do produto R$: ")

                    quantidade = input("Digite a quantidade do produto: ")

                    if len(preco) == 0 or len(quantidade) == 0:

                        print ()

                        print ("Erro! os campos devem ser preenchidos.")

                        input ("Pressione ENTER para retornar")

                        rodando = True

                    else:

                        preco = float(preco)

                        quantidade = int(quantidade)

                        service.cadastrar_produto(nome, preco, quantidade)

                        break


    elif opcao == 6:
        limpar_tela()
        print ("=======LISTA DE PRODUTOS=======")
        print()
        service.listar_produtos()


    elif opcao == 7:
        limpar_tela()
        print("=======BUSCAR PRODUTO=======")
        service.buscar_produto(ler_inteiro("Digite o Id do produto que deseja buscar: "))


    elif opcao == 8:
        rodando = True
        while rodando:
            limpar_tela()
            print ("=======ATUALIZAR QUANTIDADE EM ESTOQUE=======")
            print ()
    
            service.listar_produtos()
            
            print ()
            
            codigo = int (input ("Digite o ID do produto que deseja atualizar ou [0] Para RETORNAR AO MENU: "))
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
                NovaQuantidade = ler_inteiro("Digite a nova quantidade do produto: ")
                if NovaQuantidade < 0:
                    print ()
                    print ("Erro! O produto não deve ter quantidade menor que zero.")
                    input ("Pressione ENTER para RETORNAR. ")
                    continue

                else:
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
            limpar_tela()
            print ("=======REMOVER PRODUTO=======")
            print ()
    
            service.listar_produtos()
            
            print ()
    
            codigo = input("Informe o ID do produto a ser removido ou [0] para RETORNAR AO MENU: ")
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
        limpar_tela()
        print ("=======LISTA DE PRODUTOS INVERSA=======")   
        print()
        service.listar_produtos_inverso()

        
    elif opcao == 11:
        limpar_tela()
        print ("=======LISTA DE PRODUTOS ORDENADOS POR ID=======")
        print()
        service.listar_produtos_ordenados_por_id()


    elif opcao == 12:
        limpar_tela()
        print("=======BUSCAR PRODUTO COM BUSCA BINARIA=======")
        print()
        service.buscar_produto_binario(ler_inteiro("Digite o ID do produto que deseja buscar: "))

        
    elif opcao == 13:
        rodando = True
        while rodando:
            limpar_tela()
            print ("=======LISTA DE CLIENTES=======")
            print()
            service.listar_clientes()
            print ()
            print ("=======REALIZAR VENDA=======")
            print()

            codigo_cliente = ler_inteiro("Digite o ID do cliente ou [0] para RETORNAR AO MENU: ")
            if codigo_cliente == 0:
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
                itens = []
                primeiro_produto = True

                while True:

                    if primeiro_produto:
                        codigo_produto = ler_inteiro("Digite o código do produto a ser adicionado ao carrinho: ")

                    else:
                        codigo_produto = ler_inteiro("Infome o ID do próximo produto a ser adicionado "
                                                     "OU DIGITE 0 PARA FINALIZAR A COMPRA: ")
                    if codigo_produto == 0:
                        break
                    produto = service.produtos.buscar(codigo_produto) 

                    if produto is None:
                        print()
                        print(f"Produto com código [{codigo_produto}] não encontrado.")
                        input("Pressione ENTER para tentar novamente.")
                        continue

                    quantidade = ler_inteiro("Digite a quantidade do produto: ")

                    if service.verificar_item_venda(codigo_produto, quantidade):
                
                        itens.append({"codigo_produto": codigo_produto,
                                "quantidade": quantidade})

                        primeiro_produto = False

                        limpar_tela()

                        print()
                        print(f"Produto [{codigo_produto}] - {produto.nome} adicionado ao carrinho.")
                        print(f"Quantidade: {quantidade}")

                        print()
                        print("======= CARRINHO ATUAL =======")
                        print()
                        valor_total_carrinho=0

                        for item in itens:
                            produto_carrinho = service.produtos.buscar(item["codigo_produto"])
                            subtotal =produto_carrinho.preco * item["quantidade"]
                            valor_total_carrinho += subtotal

                            print (f"Produto [{produto_carrinho.codigo}] - "
                                   f"{produto_carrinho.nome} - "
                                   f"Qtde: {item['quantidade']} - "
                                   f"R${subtotal:.2f}")
                            
                        print()
                        print(f"Valor total do carrinho R${valor_total_carrinho:.2f}")
                        print()
                        print("        ==============        ")

                        
                        

                if len(itens) == 0:
                    print("Nenhum item adicionado à venda.")

                else:
                    service.realizar_venda_exemplo(codigo_cliente, itens)
                    break

                    
    elif opcao == 14:
        limpar_tela()
        print ("=======LISTA DE VENDAS=======")
        print()
        service.listar_vendas()
        

    elif opcao == 15:
        limpar_tela()
        service.primeira_venda()
        

    elif opcao == 16:
        limpar_tela()
        service.valor_total_estoque()
        

    elif opcao == 17:
        limpar_tela()
        service.valor_total_vendas()
        

    elif opcao == 18:
        limpar_tela()
        service.clientes_e_valores_totais_gastos()


    elif opcao == 19:
        limpar_tela()
        service.cliente_que_mais_gastou()
        

    elif opcao == 20:
        limpar_tela()
        service.produto_mais_vendido()


    elif opcao == 21:
        limpar_tela()
        print ("=======DESFAZER ULTIMA OPERAÇÃO=======")
        print ()
        certeza = input ('''Você deseja DESFAZER A ULTIMA OPERAÇÃO?: 
[1] -> SIM
[2] -> NÃO, RETORNAR AO MENU
''')
        certeza = int (certeza)
        if certeza == 1:
            service.desfazer_ultima_operacao()

        elif certeza == 2:
            print ()
            print ("Retornando para o menu principal...")
            return

        else:
            print ("Erro! OPÇÃO INVÁLIDA, Processo Cancelado!")


    else:
        print("Opcao invalida. Tente novamente.")

def main():
    service = EstoqueService()

    limpar_tela()

    rodando = True
    while rodando:
        mostrar_menu()

        print()

        try:
            opcao = ler_inteiro("Escolha uma opcao: ")

            if opcao == 0:
                certeza = True
                while certeza:
                    print ()
                    certeza = int (input ('''Você realmente deseja encerrar o programa?
[1] SIM
[2] NÃO
'''))
                    if certeza == 1:
                        print("Sistema encerrado.")
                        rodando = False
                        certeza = False
                        
                    elif certeza == 2:
                        print ()
                        print ("Retornando ao menu principal...")
                        certeza = False
                        rodando = True

                    else:
                        print ()
                        input ("Erro! CARACTERE INVALIDO. Pressione ENTER para retornar.")
                        certeza = True
                        rodando = True

            else:
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
