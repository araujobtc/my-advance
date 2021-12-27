# Escreva um programa que leia um valor em metros e o exiba
# convertido em centímetros e milímetros.

metros = float(input('Digite um valor(m): '))
cent = metros*100
mili = metros*1000

print('Metros: {:.2f} | Centímetros: {:.2f} | Milímetros: {:.2f}'.format(metros, cent, mili))
