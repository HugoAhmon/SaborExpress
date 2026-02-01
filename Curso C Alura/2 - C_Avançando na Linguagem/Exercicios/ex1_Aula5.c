//Escreva uma função soma que recebe um ponteiro de inteiro num e mais dois inteiros a e b. A função deve calcular a soma de a+b em num.

#include <stdio.h>

//função que calcula a soma de a e b e armazena o resultado no endereço apontado por num
void soma(int *num, int a, int b) {
    *num = a + b;
}


int main() {
    int resultado;
    int a = 5;
    int b = 10;
    
    soma(&resultado, a, b);//chama a função soma passando o endereço de resultado
    
    printf("A soma de %d e %d é %d\n", a, b, resultado);
    
    return 0;
}