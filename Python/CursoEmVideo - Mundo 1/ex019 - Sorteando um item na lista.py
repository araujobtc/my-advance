# Um professor quer sortear um dos seus quatro alunos para apagar um quadro.
# Faça um programa ue ajude ele, lendoo nome deles e escrevendo o nome do escolhido.

from random import choice    #randint

nomes = []
for i in range(4): 
    nomes.append(input('nome: '))

# escolhido = nomes[randint(0, 3)]
escolhido = choice(nomes)


print(f'O escolhido é {escolhido}')
