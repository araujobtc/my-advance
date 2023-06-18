# Faça um programa que leia o ano e nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao seviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

nasc = int(input("Ano de nascimento: "))
idade = date.today().year - nasc

if idade < 18: print(f"Você deverá se alistar daqui a {18-idade} ano(s)")
elif idade == 18: print("Você deve se alistar este ano!") 
else: print(f"Você deve se alistar! Já passou {idade-18} ano(s) do prazo.")