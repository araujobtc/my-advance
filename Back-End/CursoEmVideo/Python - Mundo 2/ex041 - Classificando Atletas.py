# A Confederação Nacional de Natação precisa de um programa que leia o ano de 
# nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 20 anos: SÊNIOR
# Acima: MASTER

from datetime import date

nasc = int(input("Ano de nascimento: "))
idade = date.today().year - nasc

if idade <= 9: print(f"Atleta da categoria MIRIM")
elif idade <= 14: print(f"Atleta da categoria INFANTIL")
elif idade <= 19: print(f"Atleta da categoria JUNIOR")
elif idade <= 20: print(f"Atleta da categoria SÊNIOR")
else: print(f"Atleta da categoria MASTER")