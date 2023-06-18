# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
# calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida

alt = float(input("Qual a sua altura (metros): "))
peso = float(input("Qual a seu peso (kilogramas): "))
imc = peso/(alt*alt)

if imc < 18.5: print(f"Você está abaixo do peso ideal! Seu IMC atual é {imc:.2f}.")
elif imc < 25: print(f"Você está com peso ideal! Seu IMC atual é {imc:.2f}.")
elif imc < 30: print(f"Você está com sobrepeso! Seu IMC atual é {imc:.2f}.")
elif imc < 40: print(f"Você está com obesidade! Seu IMC atual é {imc:.2f}.")
else: print(f"Você está com obesidade mórbida! Seu IMC atual é {imc:.2f}.")