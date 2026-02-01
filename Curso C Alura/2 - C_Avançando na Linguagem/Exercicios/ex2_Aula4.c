//Escreva uma função soma(int numeros[10]) que receba um array de inteiros e imprime a soma de todos os elementos dentro desse array.

#include <stdio.h>
#include <string.h>


void soma(int numeros[10]) {
    int total = 0;
    for(int i = 0; i < 10; i++) {
        total += numeros[i];
    }
    printf("A soma dos elementos do array é: %d\n", total);
}

int main() {
    int numeros[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    soma(numeros);
    return 0;
}