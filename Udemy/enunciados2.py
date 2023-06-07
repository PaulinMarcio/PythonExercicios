"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação aprovada. Ex:
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = input('Digite a hora atual: ')

try:
    hora_int = int(hora)
    if hora_int <= 11:
        print('Bom dia')
    elif hora_int <= 17:
        print('Boa tarde')
    elif hora_int <= 23:
        print ('Boa noite')
    else:
        print('Insira uma hora válida')
except:
    print('Digite a hora em números inteiros')