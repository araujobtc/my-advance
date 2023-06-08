/*  
Implemente a função

    int reverso(int n)

que recebe um valor inteiro n e retorna o mesmo número com seus dígitos invertidos. Por exemplo,
se n = 7631, a função deve retornar 1367.
*/

#include <stdio.h>
#include <math.h>

int reverso(int n){
    int qtd = 0, aux = n, rev = 0;

    while(aux!=0){
        aux /= 10;
        qtd++;
    }

    for(qtd; qtd>0; qtd--){
        rev += (pow(10, qtd) * (n%10))/10;
        n /= 10;
    }

    return rev;
}

int main(){
    int n;

    printf("\nInsira um número inteiro: ");
    scanf("%d", &n);

    printf("\nO reverso do número %d é %d", n, reverso(n));

    return 0;
}