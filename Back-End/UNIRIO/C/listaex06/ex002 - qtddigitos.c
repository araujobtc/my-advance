/* 
Implemente a função

    int digitos(int n)

que recebe um valor inteiro n e retorna o número de dígitos de n. Por exemplo, se n = 4875, a
função deve retornar 4.
*/

#include <stdio.h>

int digitos(int n){
    int qtd = 0;

    if (n == 0)
        return 1;

    while(n!=0){
        n /= 10;
        qtd++;
    }

    return qtd;
}

int main(){
    int n;

    printf("\nInsira um valor inteiro: ");
    scanf("%d", &n);
    
    printf("\n%d tem %d digitos.", n, digitos(n));  

    return 0;
}