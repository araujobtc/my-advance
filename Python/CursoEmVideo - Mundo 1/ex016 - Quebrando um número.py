# Crie um programa que leia um número Real qualquer pelo teclado e mosre na tela a sua porção inteira.
# Ex: Entrada: 6.127 Saída: O núero 6,127 tem a parte inteira 6.

from math import trunc

num = float(input('Digite um número: '))
print(f'O número: {num} tem a parte inteira: {trunc(num)}')     #ou int()