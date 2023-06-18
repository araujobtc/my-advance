/* 
Implemente a função

    void segundo_grau(float a, float b, float c)

que recebe os valores a, b e c de uma equação do segundo grau (ax2 + bx + c = 0) e imprime as
duas raízes da equação. Se não for possível calcular as duas raízes, então a função deve imprimir
“Não há raízes”.
*/

#include <stdio.h>
#include <math.h>

void segundo_grau(float a, float b, float c){
    float delta = pow(b, 2) - (4 * a * c);

    printf("\n Delta: %f", delta);
    if (delta < 0)
        printf("\nNão há raízes.");
    else if (delta == 0){
        float x = -b/(2 * a);  
        printf("\nA raíz da função (%.2f)x² + (%.2f)x + (%.2f) é %.2f", a, b, c, x); 
    }
    else{
        float x1, x2;
        
        x1 = (-b + sqrt(delta))/(2 * a); 
        x2 = (-b - sqrt(delta))/(2 * a);
        printf("\nAs raízes da função (%.2f)x² + (%.2f)x + (%.2f) são %.2f e %.2f", a, b, c, x1, x2); 
    }
}

int main(){
    float a, b, c;

    printf("Indique os valores a, b e c da função.");
    printf("\na:");
    scanf("%f", &a);
    printf("\nb:");
    scanf("%f", &b);
    printf("\nc:");
    scanf("%f", &c);

    segundo_grau(a, b, c);

    return 0;
}