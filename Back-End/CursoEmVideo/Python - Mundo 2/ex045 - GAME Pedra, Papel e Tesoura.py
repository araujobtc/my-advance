# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint

maojog = int(input("""
    (1) Tesoura
    (2) Pedra
    (3) Papel\n
Você: """))

maobot = randint(1, 4);
print(f"Bot: {maobot}\n")

if maojog in (1, 2, 3):
    if maobot == maojog: print("EMPATE!") 
    elif maobot == 1 and maojog == 2: print("VOCÊ GANHOU!") 
    elif maobot == 2 and maojog == 3: print("VOCÊ GANHOU!") 
    elif maobot == 3 and maojog == 1: print("VOCÊ GANHOU!")
    else: print("VOCÊ PERDEU! TENTE DE NOVO.") 
else: print("Opção Inválida! Tente novamente.")