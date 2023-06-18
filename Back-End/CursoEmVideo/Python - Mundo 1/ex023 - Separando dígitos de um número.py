# Faça um programa que leia um númeor de 0 a 9999 e mostre n atela cada um dos dígitos separados

while True:
    num = int(input('Digite um número: '))
    if num >= 0 and num <= 9999: break

print(f'Unidade: {num//1%10}')
print(f'Dezena: {num//10%10}')
print(f'Centena: {num//100%10}')
print(f'Milhar: {num//1000%10}')
