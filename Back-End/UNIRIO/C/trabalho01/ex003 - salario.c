#include <stdio.h>

void lerFuncionario(char *prof, int *xp, int *hrc, int *hrt){
    int l;
    
    do{
        printf("Função: ");
        fflush(stdin);
        scanf("%c", &*prof);
            
        switch (*prof){
            case 'P':
            case 'p':
            case 'A': 
            case 'a':
            case 'G':
            case 'g':
                l=0;
                break;
            default:
                printf("Opção invalida! Tente novamente.");
                l=1;
                break;
        }
    } while (l==1);
    
    do{
        printf("Anos de Exp.: ");
        scanf("%d", &*xp);
        if (*xp<0)
            printf("Valor inválido! Tente novamente.");
    } while (*xp<0);
    
    do{
        printf("Horas contratadas: ");
        scanf("%d", &*hrc);
        if (*hrc<=0)
            printf("Valor inválido! Tente novamente.");
    } while (*hrc<=0);
    
    do{
        printf("Horas trabalhadas: ");
        scanf("%d", &*hrt);
        if (*hrt<0)
            printf("Valor inválido! Tente novamente.");
    } while (*hrt<0);
}

float calcularSalario(char prof, int xp, int hrc, int hrt, float *salbruto, int *hre, float *inss, float *ir){
    float  salliq;
    
    // hora excedente
    *hre = 0;
    int hsb = hrt;
    if (hrt > hrc){
        *hre = hrt - hrc;
        hsb = hrt - *hre;
    }
    
    // hora salario bruto
    
    
    // salario bruto
    switch(prof){
        case 'P':
        case 'p':
            if (xp<=2){
                int y = 25;
                *salbruto = (hsb * y);
                if (*hre <= 13)
                    *salbruto += (*hre * y * 1.23);
                else if (*hre <= 22)
                    *salbruto += (*hre * y * 1.37);
                else
                    *salbruto += (*hre * y * 1.56);
            }
            else if (xp<=5){
                int y = 30;
                *salbruto = (hsb * y);
                if (*hre <= 13)
                    *salbruto += (*hre * y * 1.23);
                else if (*hre <= 22)
                    *salbruto += (*hre * y * 1.37);
                else
                    *salbruto += (*hre * y * 1.56);
            }
            else{
                int y = 38;
                *salbruto = (hsb * y);
                if (*hre <= 13)
                    *salbruto += (*hre * y * 1.23);
                else if (*hre <= 22)
                    *salbruto += (*hre * y * 1.37);
                else
                    *salbruto += (*hre * y * 1.56);
            }
            break;
        case 'A':
        case 'a':
            if (xp<=2){
                int y = 45;
                *salbruto = (hsb * y);
                if (*hre <= 13)
                    *salbruto += (*hre * y * 1.23);
                else if (*hre <= 22)
                    *salbruto += (*hre * y * 1.37);
                else
                    *salbruto += (*hre * y * 1.56);
            }
            else if (xp<=5){
                int y = 30;
                *salbruto = (hsb * y);
                if (*hre <= 13)
                    *salbruto += (*hre * y * 1.23);
                else if (*hre <= 22)
                    *salbruto += (*hre * y * 1.37);
                else
                    *salbruto += (*hre * y * 1.56);
            }
            else{
                int y = 38;
                *salbruto = (hsb * y);
                if (*hre <= 13)
                    *salbruto += (*hre * y * 1.23);
                else if (*hre <= 22)
                    *salbruto += (*hre * y * 1.37);
                else
                    *salbruto += (*hre * y * 1.56);
            }
            break;
        case 'G':
        case 'g':
            if (xp<=2){
                int y = 85;
                *salbruto = (hsb * y);
                if (*hre <= 13)
                    *salbruto += (*hre * y * 1.23);
                else if (*hre <= 22)
                    *salbruto += (*hre * y * 1.37);
                else
                    *salbruto += (*hre * y * 1.56);
            }
            else if (xp<=5){
                int y =102;
                *salbruto = (hsb * y);
                if (*hre <= 13)
                    *salbruto += (*hre * y * 1.23);
                else if (*hre <= 22)
                    *salbruto += (*hre * y * 1.37);
                else
                    *salbruto += (*hre * y * 1.56);
            }
            else{
                int y = 130;
                *salbruto = (hsb * y);
                if (*hre <= 13)
                    *salbruto += (*hre * y * 1.23);
                else if (*hre <= 22)
                    *salbruto += (*hre * y * 1.37);
                else
                    *salbruto += (*hre * y * 1.56);
            }
            break;
    }
    
    // inss
    *inss = *salbruto * 0.11;
    salliq = *salbruto - *inss;
    
    // ir
    if (salliq <= 2700 && salliq>1500)
        *ir = salliq * 0.15;
    else if (salliq <= 4200)
        *ir = salliq * 0.2;
    else
        *ir = salliq * 0.3;
    
    return (salliq - *ir);
}

void imprimirFolhaPagamento(float salbruto, int hre, float inss, float ir, float salliq){
    printf("- Salário Bruto.....(R$): %.2f\n", salbruto);
    if (hre != 0)
        printf("- Horas Excedentes...(H): %dhr\n", hre);
    printf("- Salário INSS......(R$): %.2f\n", inss);
    printf("- Salário IR........(R$): %.2f\n", ir);
    printf("- Salário Líquido...(R$): %.2f\n", salliq);
}

int main() {
    int qtdfunc, xp, hrc, hrt, hre, i;
    float salliq, salbruto, inss, ir;
    char prof;
    
    do{
        printf("Qtd: ");
        scanf("%d", &qtdfunc);
        fflush(stdin);
        if (qtdfunc <= 0)
            printf("ATENÇÃO: a quantidade de funcionários deve ser maior que zero. Informe novamente.\n");
    } while(qtdfunc<=0);

    for(i=0; i<qtdfunc; i++){
        printf("==============\nFuncionário %d\n", (i+1));
        lerFuncionario(&prof, &xp, &hrc, &hrt);
        salliq = calcularSalario(prof, xp, hrc, hrt, &salbruto, &hre, &inss, &ir);
        printf("Folha de Pagamento do Func. %d\n", i+1);
        imprimirFolhaPagamento(salbruto, hre, inss, ir, salliq);
    }
    return 0;
}