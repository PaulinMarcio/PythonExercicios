# Faça um programa que calcule a média aritmética de um valor

nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
media = (nota1 + nota2) / 2

print('A primeira nota foi {}, a segunda nota foi {}.'.format(nota1, nota2))
print('A média do aluno foi de {:.2f}'.format(media))