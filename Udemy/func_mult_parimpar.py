def multi(*args):
    total = 1
    for num in args:
        total *= num
    return total

def parImpar(num):
    restante = num % 2
    return 'Par' if restante == 0 else 'Impar'

print(multi(3,5,6,4,3,5,6))

print(parImpar(3))

print(parImpar(4))