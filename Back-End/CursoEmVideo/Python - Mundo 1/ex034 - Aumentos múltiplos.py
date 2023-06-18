# Escreva um programa que pergunta o salário de um funcionário e calcle o valor do seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%.
# Para salários inferiores ou iguais, o aumento é de 15%.

sal = float(input("Salário: "))

if sal > 1250: print(f"Com o aumento de 10%, o salário será de R${(sal*1.10):.2f}. Um acréscimo de R${((sal*1.10) - sal):.2f}")
else: print(f"Com o aumento de 15%, o salário será de R${(sal*1.15):.2f}. Um acréscimo de R${((sal*1.15) - sal):.2f}")