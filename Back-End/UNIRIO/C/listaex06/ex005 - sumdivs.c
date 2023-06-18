/*  
Implemente a função

    int soma_divisores(int n)

que retorna a soma dos divisores próprios de n. Dica: divisores próprios são os divisores de um
número sem contar com ele mesmo. Os divisores próprios de 6 são 1, 2 e 3.
*/

#include <stdio.h>

int soma_divisores(int n){
    int soma=0;

    for(int i = n-1; i>0; i--)
        if ((n%i) == 0)
            soma += i;

    return soma;
}

int main(){
    int n;
    printf("\nInsira um número inteiro: ");
    scanf("%d", &n);
    printf("\nA soma do divisores próprios de %d, é %d\n", n, soma_divisores(n));

    return 0;
}