# Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos
# ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário
# ou então o empréstimo será negado.

pcasa = float(input("Qual o preço da casa? "))
salario = float(input("Qual o seu salário? "))
tempo = int(input("Quitação em quantos anos? "))

if pcasa/(tempo*12) <= (salario * 0.3): print(f"Empréstimo aceito!")
else: print("Empréstimo negado!")