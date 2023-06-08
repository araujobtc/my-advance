/* 
Implemente a função

    int conta_digitos(int n, int d)

que recebe um valor inteiro n e retorna quantas vezes o dígito d (0 a 9) aparece no número n. Por
exemplo, se n = 6764963 e d = 6 a função deve retornar 3.
*/

#include <stdio.h>

int conta_digitos(int n, int d){
    int qtd = 0;

    if (n == 0 && d == 0)
        return 1;

    while(n!=0){
        if ((n%10) == d)
            qtd++;
        n /= 10;
    }

    return qtd;
}

int main(){
    int n, d;

    printf("\nInsira um valor inteiro: ");
    scanf("%d", &n);
    printf("\nQual digito você quer verificar: ");
    scanf("%d", &d);
    
    printf("\nO número %d tem %d digitos \"%d\".", n, conta_digitos(n, d), d);  

    return 0;
}