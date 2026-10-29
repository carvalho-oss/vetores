import os
os.system('cls')

lista_series = []

while True:
    os.system('cls')

    print('''
    ==== sineFLIX ===
    1- CADASTRAR SERIE
    2- LISTA_SERIES
    0- SAIR DO APP
    ''')
        
    opcao = int(input('Digite a opção desejada: '))

    match opcao:
        case 1:
            print('\n=== CADASTRO DE PRODUTOS ===')
                # strip() retira os espaços vazios no final.
                #upper() todas as letras maiúsculas.
            nome = input('Digite o nome da serie produto: ')
            if nome == " ":
                print('O nome não pode ficar vazio.')
            elif nome in lista_series:
                print(f'{nome} já está cadastrado.')
                
            else:
            #.append(nome)adiciona o nome da serie .
                lista_series.append(nome)
                print('Produto cadastradada com sucesso!')
                input('\nPressione uma tecla para continuar...')
        case 2:
            print('\n=== LISTANDO SERIES ====')
            if len(lista_series) ==  0:
                print('lista vazia')
            else:
                for i, lista_series in enumerate(lista_series):
                    print(f'{i+1}. {serie}')

        case 0:
            print('FIM DO PROGRAMA.')
            break
            input("Pressione para continuar...")
            
        case _:
            print('Opção inválida!"')
            input(' Pressione a tecla para continuar...')
            
