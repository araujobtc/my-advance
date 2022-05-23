# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome comm todas a letras maiúsculas
# O nome com odas minúsculas
# Quantas letras ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome

nome = str(input('Nome completo: ')).strip()

print(f'Todas maiúsculas: {nome.upper()}')
print(f'Todas minúsculas: {nome.lower()}')
print(f'Quantidade de letras do nome completo: {len(nome)-nome.count(" ")}')
print(f'Quantidade de letras do primeiro nome: {len((nome.split())[0])}')
