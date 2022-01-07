# Faça um programa que leia algo pelo teclado e mostre na tela
# o seu tipo primitivo e todas as informações possíveis sobre ele

a = input('Digite algo: ')

print('Tipo: {} | Númerico: {} | Alfabético: {} | Alfanumérico: {}'.format(type(a), a.isnumeric(), a.isalpha(), a.isalnum()))
print('Está em maiúscula: {} | Está em minúscula: {} | Está capitalizada: {}'.format(a.isupper(), a.islower(), a.istitle()))
