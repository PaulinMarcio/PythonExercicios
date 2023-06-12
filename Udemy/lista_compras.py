# Faça uma lista de compras com listas. O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista.
# Não permita que o programe quebre com erros de índices inexistentes.
import os

lista_compras = []
menu = ''
while True:
    print('Escolha uma opção')
    menu = input('[I]nserir [A]pagar [L]istar [S]air: ').upper()

    match menu:
        case 'I':
            os.system('cls')
            item = input('Digite o item: ')
            try:
                lista_compras.append(item)
            except Exception:
                    print('Erro desconhecido.')
                    print(Exception)
        case 'A':
            os.system('cls')
            if len(lista_compras) > 0:
                for produto in enumerate(lista_compras):
                    print(produto)
                item_str = input('Digite qual index você quer remover: ')
                try:
                    item = int(item_str)
                    del lista_compras[item]
                except IndexError:
                    print('Item inválido')
                except TypeError:
                    print('Por favor, insira somente números.')          
                except Exception:
                    print('Erro desconhecido.')
                    print(Exception)      
                
            else:
                print('Não há nada para apagar.')

        case 'L':
            os.system('cls')
            if len(lista_compras) > 0:
                for produto in enumerate(lista_compras):
                    print(produto)
            else:
                print('Não há nada para mostrar.')

        case 'S':
            break

        case _:
            os.system('cls')
            print('Digite uma opção válida.')