# Exiba os indices da lista
# Ex: 0 A, 1 B, 2 C, 3 D
#
lista = ['A', 'B', 'C', 'D']
'''num = 0

for indice in lista:
    print(num, indice)
    num += 1
'''

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice])