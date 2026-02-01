//Escreva uma função potencia() que receba dois inteiros, a e b, calcule a potência a^b, ou seja, a elevado a b e imprima o resultado.

#include <stdio.h>
#include <string.h>


// Função para calcular e imprimir a potência
void potencia(int a, int b) {
    int resultado = 1;
    for(int i = 0; i < b; i++) {// Loop que itera 'b' vezes
        resultado *= a;// Multiplica 'resultado' por 'a', 'b' vezes
    }
    printf("%d elevado a %d é %d\n", a, b, resultado);
}


int main() {
    int a, b;
    printf("Digite o valor de a: ");
    scanf("%d", &a);
    printf("Digite o valor de b: ");
    scanf("%d", &b);
    potencia(a, b);
    return 0;
}