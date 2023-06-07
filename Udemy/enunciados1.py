"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se esse número é par ou ímpar. Se o número não for inteiro,
informe o usuário.
"""
numero = input('Insira um número inteiro: ')

try:
    numero_int = int(numero)
    numero_int = numero_int % 2

    if numero_int == 0:
        print('O número é par')
    else:
        print('O número é ímpar')
except:
    print('insira um número inteiro')