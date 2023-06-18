# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos
# dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

nomes = []
for i in range(4): 
    nomes.append(input('nome: '))

shuffle(nomes)

print(f'Ordem da apresentação: {nomes[0]}, {nomes[1]}, {nomes[2]}, {nomes[3]}')