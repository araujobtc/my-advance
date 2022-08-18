# Faça um programa que leia um ano qualquer e mostre se ele é bissexto

from datetime import date


ano = int(input("Insira um ano, ou 0 para o anoo atual, para analisar: "))

if ano == 0: ano = date.today().year

if ano % 100 == 0:
    if ano % 400 == 0: print(f"{ano} é um ano bissexto")
    else: print(f"{ano} não é um ano bissexto")
elif ano % 4 == 0: print(f"{ano} é um ano bissexto")
else: print(f"{ano} não é um ano bissexto")