# Faça um algoritmo que leia o preço de um produto e mostre seu 
# novo preço com 5% de desconto

preco = float(input('Preço do produto: '))
desc = preco - (preco*0.05)

print('O produto tem o preço de R${}, mas com o desconto de 5% vai custar R${:.2f}'.format(preco, desc))
