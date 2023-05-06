# Refaça o ex035 dos triângulos, acrescentando o recurso de mostrar
# que tipo de riânglo será formado:
# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes

c1 = int(input("Comprimeto 1: "))
c2 = int(input("Comprimeto 2: "))
c3 = int(input("Comprimeto 3: "))

if c1 < (c2 + c3) and c2 < (c1 + c3) and c3 < (c1 + c2): 
    if c1 == c2 and c2 == c3 and c1 == c3: print("As retas podem formar um triângulo Equilátero")
    elif c1 == c2 or c2 == c3 or c1 == c3: print("As retas podem formar um triângulo Isósceles")
    else: print("As retas podem formar um triângulo Escaleno")
else: print("As retas não podem formar um triângulo")