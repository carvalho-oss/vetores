import os

#lista de produtos.
lista_produtos = []

while True:
    os.system('cls')
    #limpar o terminal.
    os.system("cls")
    print('''
==== MERCADINHO ===
1- CADASTRO DE PRODUTOS
2- LISTA_PRODUTOS
0- SAIR
''')
    
    opcao = int(input('Digite a opção desejada: '))

    match opcao:
        case 1:
            print('\n=== CADASTRO DE PRODUTOS ===')
            # strip() retira os espaços vazios no final.
            #upper() todas as letras maiúsculas.
            nome = input('Digite o nome do novo produto: ')
            
            
            if nome == " ":
                print('O nome não pode ficar vazio.')
            elif nome in lista_produtos:
                print(f'{nome} já está cadastrado.')

            else:
                #.append(nome)adiciona o nome do produto na lista.
                lista_produtos.append(nome)
                print('Produto cadastrado com sucesso!')
                input('\nPressione uma tecla para continuar...')

        case 2:
            print('\n=== PRODUTOS NO ESTOQUE ===')
            if len(lista_produtos) == 0:
                print('O estoque está vazio.')
            else:
                for i, produto in enumerate(lista_produtos):
                    print(f'{i+1}. {produto}')

                # len(lista_produtos) mostra a quantidade de produtos na lista.
                print(f'Total de produtos: {len(lista_produtos)}')

        case 0:
            print('FIM DO PROGRAMA.')
            break
            input("Pressione para continuar...")
            
        case _:
            print('Opção inválida!"')
            input(' Pressione a tecla para continuar...')

