# Faça um algoritmo que leia o sálrio de um funcionário e mostre seu 
# novo sálario com 15% de aumento

salario = float(input('Sálario atual: '))
aumento = salario + (salario*0.15)

print('Sálario atual | Sálario com aumento')
print(' R${}      |    R${}      '.format(salario, aumento))
