# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

v = int(input("Velocidade do carro: "))

if v > 80:
    print("O carro foi multado por excesso de velocidade!")
    print(f"O valor da multa é de R${((v-80)*7):.2f}")