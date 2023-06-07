frase = 'O Python é uma linguagem de programação multiparadigma. Python foi criado por Guido van Rossum.'.lower()

i = 0
qtd = 0
letra = ''
while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    quantas_vezes = frase.count(letra_atual)
    if qtd < quantas_vezes:
        qtd = quantas_vezes
        letra = letra_atual

    i += 1

print(f'A letra que apareceu mais vezes foi {letra}, aparecendo {qtd} vezes')