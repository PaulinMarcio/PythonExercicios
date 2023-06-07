# Faça um programa que leia algo na tela e retorne o tipo primitivo e todas as informações possíveis sobre ela

palavra = input('Digite uma palavra: ')

print('O tipo primitivo dessa palavra é:', type(palavra))
print('Tem espaços?', palavra.isspace())
print('É um número?', palavra.isnumeric())
print('É alfabético?', palavra.isalpha())
print('É alfanumérico?', palavra.isalnum())
print('Está em maíusculas?', palavra.isupper())
print('Está em minúsculas?', palavra.islower())
print('Esta capitalizado?', palavra.istitle())