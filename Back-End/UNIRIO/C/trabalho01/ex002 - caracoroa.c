#include <stdio.h>

int main(){
    int n, r, maria=0, joao=0;
     
    do{ 
        printf("\n");
        scanf("%d", &n); // le numero de jogadas
        fflush(stdin);
        if (n < 0 || n > 10000)
            printf("valor inválido insira novamente\n");
        else if (n == 0)
            return 0;
        else{
            for(int i=0; i<n; i++){
                scanf("%d", &r);
                if(i+1 == n)
                    fflush(stdin);

                if(r == 0){
                    maria++;
                }
                else if (r == 1){
                    joao++;
                }
                else{
                    printf("\nUm valor inválido foi inserido.\n");
                    joao = 0;
                    maria = 0;
                    break;
                }
            }
            if (joao!=0 || maria!=0)
                printf("Maria venceu %d vez(es) e Joao venceu %d vez(es)", maria, joao);
        }
        joao = 0;
        maria = 0;
    }while(n < 1 || n >10000 || n !=0);
}