# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint

print("=-=-" * 10)
print("JOGO DA ADIVINHAÇÃO")
print("=-=-" * 10)
print('Tente adivinha o número, de 0 a 5, que a máquina esta "pensando"\n')

if randint(0, 5) == int(input("Escreva um numero: ")) : print("Parabénsss, você acertou!\nVocê venceu.")
else: print(f"Infelizmente você errou!\nO computador venceu")
print()