# Crie um programa que leia o nome de uma pessoa e diga se ela tem 'silva' no nome.

nome = str(input('Nome completo: ')).strip().title()

silva = nome.find('Silva')  # 'Silva' in nome

if silva == -1: print(f'O nome {nome} não tem "Silva" no nome')     #silva == False
else: print(f'O nome {nome} tem "Silva" no nome')

print()
