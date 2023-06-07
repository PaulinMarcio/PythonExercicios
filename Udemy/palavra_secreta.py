'''
Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar uma letra.
- Quando o usuário digitar uma letra, você vai conferir se a letra está na palavra secreta.
    - Se a letra estiver na palavra secreta, exiba a letra
    - Se a letra não estiver na palavra secreta, exiba *
- Faça a contagem de tentativas do usuário.
'''
import os

secreta = 'python'
tentativas = 0
usuario = ''

while usuario != secreta:
    
    letra = input('Digite uma letra: ')
    if len(letra) > 1:
        print('Insira uma letra de cada vez.')
        tentativas += 1
        continue

    if letra in secreta:
        usuario += letra

    formado = ''
    for letra_secreta in secreta:
        if letra_secreta in usuario:
            formado += letra_secreta
        else:
            formado += '*'
    tentativas += 1
    print(formado)

print(f'Parabéns! A palavra era {secreta}!')
print(f'Numero de tentativas: {tentativas}')

os.system('clear')
    



    