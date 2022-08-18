# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de
# até 200Km, e R$0,45 para viagens mais longas.

km = float(input("Distância da viagem: "))
# passagem = km * 0.45 if km > 200 else km * 0.5
if km > 200: print(f"O preço da passagem é R${(0.45*km):.2f}")
else: print(f"O preço da passagem é R${(0.5*km):.2f}")