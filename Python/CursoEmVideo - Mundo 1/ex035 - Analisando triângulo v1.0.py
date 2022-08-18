# Desenvolva um programa que leia o comprimento de três reas e diga ao usuário se elas podem ou não formar um triângulo.

c1 = int(input("Comprimeto 1: "))
c2 = int(input("Comprimeto 2: "))
c3 = int(input("Comprimeto 3: "))

if c1 < (c2 + c3) and c2 < (c1 + c3) and c3 < (c1 + c2): print("As retas podem formar um triângulo")
else: print("As retas não podem formar um triângulo")
