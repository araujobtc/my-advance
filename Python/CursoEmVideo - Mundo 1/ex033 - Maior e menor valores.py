# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num1 = int(input("Primeiro numero: "))
num2 = int(input("Segundo numero: "))
num3 = int(input("Terceiro numero: "))

menor = num1

if num1 > num2 and num1 > num3:
    print(f"{num1} é o maior número")
    if num2 > num3: print(f"{num2} é o menor número")
    else: print(f"{num2} é o menor número")
elif num3 > num2 and num3 > num1:
    print(f"{num3} é o maior número")
    if num2 > num1: print(f"{num1} é o menor número")
    else: print(f"{num2} é o menor número")
else:
    print(f"{num2} é o maior número")
    if num1 > num3: print(f"{num3} é o menor número")
    else: print(f"{num1} é o menor número")
