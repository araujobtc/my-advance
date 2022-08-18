# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'santo'.

cidade = str(input('Nome da cidade: ')).strip().title()

primeiro = cidade.find('Santo')

if primeiro == 0: print(f'A cidade {cidade} tem "Santo" no inicio do nome')
else: print(f'A cidade {cidade} não tem "Santo" no inicio do nome')
