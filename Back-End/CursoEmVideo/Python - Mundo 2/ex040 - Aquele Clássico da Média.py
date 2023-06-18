# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acodo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre de 5.0 e 6.9: RECUPERAÇÃO
# - Média igual ou acima de 7.0: APROVADO

media = (float(input("Nota 1: ")) + float(input("Nota 2: "))) / 2

if media < 5: print(f"REPROVADO! O aluno tirou média {media:.2f}.")
elif media < 6.9: print(f"RECUPERAÇÃO! O aluno tirou média {media:.2f}.")
else: print(f"APROVADO! O aluno tirou média {media:.2f}.")