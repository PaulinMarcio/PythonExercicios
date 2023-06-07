while True:
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))
    print('[1] - Adição')
    print('[2] - Subtração')
    print('[3] - Divisão')
    print('[4] - Multiplicação')
    op = int(input('Digite qual operação você quer fazer: '))

    match op:
        case 1:
            res = num1 + num2
            print(f'O resultado de {num1} + {num2} é {res}')

        case 2:
            res = num1 - num2
            print(f'O resultado de {num1} - {num2} é {res}')
            
        case 3:
            res = num1 / num2
            print(f'O resultado de {num1} / {num2} é {res}')
            
        case 4:
            res = num1 * num2
            print(f'O resultado de {num1} * {num2} é {res}')
            
        case _:
            print('Digite uma opção válida.')
            

    sair = input('Deseja sair? [s]im - [n]ão: ').lower().startswith('s')
    if sair == True:
        break
