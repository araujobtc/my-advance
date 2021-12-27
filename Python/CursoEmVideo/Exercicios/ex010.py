# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e
# mostre quantos Dólares ele pode comprar.

reais = float(input('Quantos reais (R$) você tem? '))

print('US$1.00 = R$ 5,67 | 26/12/2021')

conv = reais/5.67

print('Você pode comprar US${:.2f} com R${}'.format(conv, reais))
