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

cpf_mult_primeiro = [10, 9, 8, 7, 6, 5, 4, 3, 2] # números para a multiplicação
cpf_mult_segundo = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2] # números para a multiplicação
cpf = input('insira o seu cpf: ') # cpf do usuário
cpf_res_primeiro = 0 # resultado primeiro número
cpf_res_segundo = 0 # resultado segundo número

cpf_num = cpf # não mexe no cpf original
cpf_num = cpf_num.split() # separa eles

for num in range(len(cpf_num)):
    cpf_num[num] = int(cpf_num[num])


for num in range(len(cpf_mult_primeiro)):
    cpf_num[num] = int(cpf_num[num]) # transforma de string para int
    cpf_mult_res = cpf_mult_primeiro[num] * cpf_num[num] # multiplicação de cada número
    cpf_res_primeiro += cpf_mult_res # soma dos resultados das multiplicações


cpf_res_primeiro = (cpf_res_primeiro * 10) % 11 # resultado multiplicado por 10 e tirado o resto da divisão por 11

cpf_res_primeiro = 0 if cpf_res_primeiro > 9 else cpf_res_primeiro # se o resultado for maior que 9, transformar em zero

print(cpf_res_primeiro) # primeiro digito do cpf

for num in range(len(cpf_mult_segundo)):
    cpf_num[num] = int(cpf_num[num]) # transforma de string para int
    cpf_mult_res = cpf_mult_segundo[num] * cpf_num[num] # multiplicação de cada número
    cpf_res_segundo += cpf_mult_res # soma dos resultados das multiplicações

cpf_res_segundo = (cpf_res_segundo * 10) % 11 # resultado multiplicado por 10 e tirado o resto da divisão por 11

cpf_res_segundo = 0 if cpf_res_segundo > 9 else cpf_res_segundo # se o resultado for maior que 9, transformar em zero
print(cpf_res_segundo)

print(cpf_num)
