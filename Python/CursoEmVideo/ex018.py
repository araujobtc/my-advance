# Faça um programa que leia um âmgulo qualquer e mostre na tela o
# valor de seno, cosseno e tangente desse ângulo

from math import radians, cos, sin, tan

ang = float(input('angulo: '))
angulo = radians(ang)
seno = sin(angulo)
cosseno = cos(angulo)
tangente = tan(angulo)

print(f'seno: {seno :.3f}')
print(f'cosseno: {cosseno :.3f}')
print(f'tangente: {tangente :.3f}')