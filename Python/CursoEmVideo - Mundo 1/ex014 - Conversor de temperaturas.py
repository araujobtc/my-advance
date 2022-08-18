# Escreva um programa que converta uma temperatura digitada
# em °C e converta para °F.

tempc = float(input('Temperatura (°C): '))
tempf = (tempc * (9/5)) + 32

print('Convertendo...')
print('Temperatura (°F): {}'.format(tempf))
