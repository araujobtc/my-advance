# Escreva um programa que pergunte a quantidade de Km percorridos por
# um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Quilometragem: '))
dias = int(input('Dias de aluguel: '))
preco = (60*dias) + (0.15*km)

print('Alugando um carro por {} dias e tendo {} de quilometragem, o preço a ser pago é R${:.2f}'.format(dias, km, preco))
