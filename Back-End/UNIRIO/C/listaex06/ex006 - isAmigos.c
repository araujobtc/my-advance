/*  
Implemente a função

    bool amigos(int x, int y)

que retorna true ou false indicando se os números x e y são amigos ou não. x e y serão amigos se a
soma dos divisores próprios de x for igual a y e se a soma dos divisores próprios de y for igual a x.

Dica 1: divisores próprios são os divisores de um número sem contar com ele mesmo. Os divisores próprios de 6 são 1, 2 e 3.
Dica 2: use a função implementada no exercício anterior (sumdivs.c).
Dica 3: 1184 e 1210 são amigos.
*/

#include <stdio.h>
#include <stdbool.h>

int soma_divisores(int n){
    int soma=0;

    for(int i = n-1; i>0; i--)
        if ((n%i) == 0)
            soma += i;

    return soma;
}

bool amigos(int x, int y){
    if (soma_divisores(x) == y && soma_divisores(y) == x)
        return 1;
    return 0;
}

int main(){
    int x, y;
    printf("\nInsira dois números inteiros:\n");
    printf("num 1: ");
    scanf("%d", &x);
    printf("num 2: ");
    scanf("%d", &y);
    printf("\n%d e %d %s\n", x, y, amigos(x, y)? "são amigos" : "não são amigos");

    return 0;
}
