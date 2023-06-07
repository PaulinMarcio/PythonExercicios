# Faça um programa que receba um número e retorne o dobro, o triplo e sua raiz quadrada.

num = int(input('Digite um valor: '))

print('O valor recebido foi {}. Dobro: {}, Triplo: {}, Raiz Quadrada: {:.2f}'.format(num, num*2, num*3, num**(1/2)))