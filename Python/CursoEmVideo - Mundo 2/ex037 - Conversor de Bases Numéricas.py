# Escreva um programa que leia um número inteiro qualquer e peça para o
# usuário escolher qual será a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal

num = int(input("Insira um número: "))
base = int(input("(1) Binário (2) Octal (3) Hexadecimal \n"))

if base == 1: print(f"O número {num} em binário é {bin(num)[2:]}")
elif base == 2: print(f"O número {num} em octal é {oct(num)[2:]}")
elif base == 3: print(f"O número {num} em hexadecimal é {hex(num)[2:]}")
else: print("Opção inválida. Tente novamente!")