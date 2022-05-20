# Faça um programa que leia o coprimento do cateto oposto e do cateto 
# adjacemte de m triângulo retângulo. Calcule e mostre o comprimento da hipotenusa

from math import hypot   # pow, sqrt

ca = float(input('cateto adjacente: '))
co = float(input('cateto oposto: '))
# h = sqrt(pow(ca,2)+pow(co,2))
h = hypot(co, ca)

print(f'hipotenusa: {h}')