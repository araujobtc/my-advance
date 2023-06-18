# Escreva um programa que leia dois númeors inteiros e compare-os,
# mostrando na tela uma mensagem:
# - O primero valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais.

n1 = int(input("Insira um número inteiro: "))
n2 = int(input("Insira outro número inteiro: "))

if n1 > n2 : print(f"O primero valor é maior! {n1} é maior que {n2}")
elif n1 < n2 : print(f"O segundo valor é maior! {n2} é maior que {n1}")
else: print("Os dois números são iguais!")