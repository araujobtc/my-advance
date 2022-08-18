# Fça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Nome completo: ')).strip().title()

print(f'Primeiro nome: {nome.split()[0]}')
print(f'Último nome: {nome.split()[-1]}')
