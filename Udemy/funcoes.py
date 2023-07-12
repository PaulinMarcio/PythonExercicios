#Crie funções que dupliquem, tripliquem e quadripliquem o número recebido

def duplicar(num):
    return num * 2

def triplicar(num):
    return num * 3

def quadruplicar(num):
    return num * 4

print(duplicar(3))
print(triplicar(3))
print(quadruplicar(3))

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplica = criar_multiplicador(2)
triplica = criar_multiplicador(3)
quadruplica = criar_multiplicador(4)

print(duplica(3))
print(triplica(3))
print(quadruplica(3))