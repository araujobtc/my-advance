# Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.

num = int(input("Insira um número: "))

if (num%2) != 0: print(f"{num} é um número ímpar")
else: print(f"{num} é um número par")