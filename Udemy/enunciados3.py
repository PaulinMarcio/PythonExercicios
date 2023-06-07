"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos
escreva 'Seu nome é curto'; Se tiver entre 5 e 6 letras, escreva 'Seu nome é normal'; Maior que 6 escreva 'Seu nome é muito grande'.
"""

nome = input('Insira seu nome: ')
length = len(nome)

if length <= 4:
    print('Seu nome é curto')
elif length == 5 or length == 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')