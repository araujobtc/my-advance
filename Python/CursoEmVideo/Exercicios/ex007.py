# Desenvolva um programa que leia as duas noras de um aluno,
# calcule e mostre sua média.

n1 = float(input('Nota 1: (ex.: 8.5) '))
n2 = float(input('Nota 1: (ex.: 7.9) '))

m = (n1 + n2)/2

print('nota1 | nota2 | média')
print('  {:.1f}  |  {:.1f}  |  {:.1f}  '.format(n1, n2, m))

