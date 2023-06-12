"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

cpf_mult = [10, 9, 8, 7, 6, 5, 4, 3, 2]
cpf_num = [7, 4, 6, 8, 2, 4, 8, 9, 0]
cpf_res = 0

for num in range(len(cpf_mult)):
    cpf_mult_res = cpf_mult[num] * cpf_num[num]
    cpf_res += cpf_mult_res
    print(f'{cpf_mult[num]} * {cpf_num[num]} = {cpf_mult_res}')

cpf_res = cpf_res * 10
cpf_res = cpf_res % 11

cpf_res = 0 if cpf_res > 9 else cpf_res