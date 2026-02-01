#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<time.h>

#define TAMANHO_PALAVRA 20
#define TOTAL_PALAVRAS 5
void imprime_cabecalho() {//
    printf("\n\n");
    printf("  ____                        _           _   _                 \n");
    printf(" |  _ \\ ___  __ _  ___ _ __  | |__   ___ | |_| |__   ___ _ __   \n");
    printf(" | |_) / _ \\/ _` |/ _ \\ '__| | '_ \\ / _ \\| __| '_ \\ / _ \\ '_ \\  \n");
    printf(" |  __/  __/ (_| |  __/ |    | | | | (_) | |_| | | |  __/ | | | \n");
    printf(" |_|   \\___|\\__, |\\___|_|    |_| |_|\\___/ \\__|_| |_|\\___|_| |_| \n");
    printf("            |___/                                               \n");
    printf("\n\n");
}
int main() {
    imprime_cabecalho();
    char palavrasecreta[TAMANHO_PALAVRA];
    char chutes[26];
    int chutesdados = 0;
    FILE *f;// ponteiro para arquivo
    f = fopen("palavras.txt", "r");//
    if(f == 0) {
        printf("Desculpe, banco de palavras não disponível\n\n");
        exit(1);
    }
    int quantidadepalavras;
    fscanf(f, "%d", &quantidadepalavras);
    srand(time(0));
    int randomico = rand() % quantidadepalavras;
    for(int i = 0; i <= randomico; i++) {
        fscanf(f, "%s", palavrasecreta);
    }
    fclose(f);
    int acertou = 0;
    int enforcou = 0;
    while(!acertou && !enforcou) {
        char chute;
        printf("Palavra secreta: ");
        for(int i = 0; i < strlen(palavrasecreta); i++) {
            int achou = 0;
            for(int j = 0; j < chutesdados; j++) {
                if(chutes[j] == palavrasecreta[i]) {
                    achou = 1;
                    break;
                }
            }
            if(achou) {
                printf("%c ", palavrasecreta[i]);
            } else {
                printf("_ ");
            }
        }
        printf("\n");
        printf("Chutes até agora: ");
        for(int i = 0; i < chutesdados; i++) {
            printf("%c ", chutes[i]);
        }
        printf("\n");
        printf("Digite uma letra: ");
        scanf(" %c", &chute);
        chutes[chutesdados] = chute;
        chutesdados++;
        int chutecorreto = 0;
        for(int i = 0; i < strlen(palavrasecreta); i++) {
            if(chute == palavrasecreta[i]) {
                chutecorreto = 1;
            }
        }
        if(!chutecorreto) {
            printf("Você errou!\n");
        }
        acertou = 1;
        for(int i = 0; i < strlen(palavrasecreta); i++) {
            int achou = 0;
            for(int j = 0; j < chutesdados; j++) {
                if(chutes[j] == palavrasecreta[i]) {
                    achou = 1;
                    break;
                }
            }
            if(!achou) {
                acertou = 0;
            }
        }
        if(!acertou && chutesdados >= 6) {
            enforcou = 1;
        }
    }
    if(acertou) {
        printf("Parabéns! Você ganhou!\n");
    } else {
        printf("Você perdeu! Tente novamente!\n");
        printf("A palavra secreta era %s\n", palavrasecreta);
    }
    return 0;
}
