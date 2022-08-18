# Faça um programa que leia um frase e pelo teclado e mostre;
# Quantas vezes aparece a letra 'a'
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a última

frase = str(input('Digite uma frase: ')).strip().lower()

qnt = frase.count("a")

if qnt > 0:
    print(f'Tem {qnt} "a" na frase: "{frase}"')
    print(f'O primeiro "a" aparece na posição {frase.find("a")+1}')
    print(f'O último "a" aparece na posição {frase.rfind("a")+1}')
else: print(f'Nao há "a" na frase')
