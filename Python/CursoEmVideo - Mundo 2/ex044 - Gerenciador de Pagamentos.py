# Elabore um programa que calcule o valor a ser pago por um produto, 
# considerando o seu preço normal e condição de pagamento:
# - À vista dinheiro/cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

preco = float(input("Preço do produto/serviço: "))
pag = int(input("""
    (1) Dinheiro/Cheque
    (2) 1x no Cartão
    (3) 2x no Cartão
    (4) 3x ou mais no Cartão
    """))

if pag == 1: preco -= preco * .1 
if pag == 2: preco -= preco * .05 
if pag == 4: preco += preco * .2 

print(f"O preço final do produto/serviço será {preco:.2f}")