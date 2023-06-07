# Crie um programa que receba uma medida em métros e converta para centimetros e milimetros

metros = float(input('Digite o valor em metros: '))

km = metros / 1000
hm = metros / 100
dam = metros / 10
dm = metros * 10
cm = metros * 100
mm = metros * 1000

print('O valor inserido foi {}M.'.format(metros))
print('''Tabela de conversão
KM: {}
HM: {}
DAM: {}
DM: {}
CM: {}
MM: {}'''.format(km, hm, dam, dm, cm, mm))