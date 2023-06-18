#include <stdio.h>

int main() {
    int n, i;
    double aux, x, j, arctan = 0;
    
    do{
        scanf("%lf", &x);
        if(x>=1.0 || x<=-1.0)
            printf("O valor absoluto de x deve ser menor que 1. Informe novamente.\n");
    }while(x>=1.0 || x<=-1.0);
    do{
        scanf("%d", &n);
        if(n<0)
            printf("O valor de n deve ser maior ou igual a 0. Informe novamente.\n");
    }while(n<0);
    
    for(i=0; i<=n; i++){
        int k =(2*i)+1;
        aux = x;
        
        for(j = k; j>1; j--)
            aux *= x;
            
        if (i == 0)
            arctan = x;
        else if (i%2 == 0)
            arctan += (1.0/k)*aux;
        else
            arctan += (-1.0/k)*aux;
    }
    printf("%.10lf\n", arctan);
    return 0;
}