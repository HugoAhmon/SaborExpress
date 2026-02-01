#include<stdio.h>
#include<string.h>

void abertura() {
    printf("**********************************\n");
    printf("* Bem vindo ao jogo de Forca!    *\n");
    printf("**********************************\n");
}

void desenhaforca(int tentativas) {
    // Função para desenhar a forca com base no número de tentativas restantes
    // (Implementação pode ser adicionada aqui)
}

void chuta() {
    // Função para ler o chute do jogador
    
}

void letrasacertada() {
    for(int i = 0; i < strlen(palavrasecreta); i++) {   // para cada letra da palavra
            int achou = 0;
            for(int j = 0; j < chutesdados; j++) {
                if(chutes[j] == palavrasecreta[i]) {    // verifica se a letra ja foi chutada
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
}

void verificapalavracerta() {
    for(int i = 0; i < strlen(palavrasecreta); i++) {
            int achou = 0;
            for(int j = 0; j < chutesdados; j++) {
                if(chutes[j] == palavrasecreta[i]) {
                    achou = 1;
                    break;
                }
            }
        if(!achou) {
            acertouagora = 0;
            break;
        }
    }
}

char palavrasecreta[20] = "MELANCIA";
char chutes[26];
int chutesdados = 0;
int acertou = 0;
int enforcou = 0;
int tentativas = 10;
int acertouagora = 1;

int main() {
    // Apresentação do jogo
    abertura();


    while(!acertou && !enforcou) {
        char chute;// guarda o chute do jogador
        printf("Palavra secreta: ");
        //strlen retorna o tamanho da string
        // mostrando as letras ja acertadas
        letrasacertada();
        printf("\n");

        printf("Chutes até agora: ");
        for(int i = 0; i < chutesdados; i++) {
            printf("%c ", chutes[i]);
        }
        printf("\n");

        printf("Você tem %d tentativas restantes\n", tentativas);
        printf("Digite uma letra: ");
        scanf(" %c", &chute);// o espaço antes do %c consome qualquer espaço em branco anterior ou "enter"

        chutes[chutesdados] = chute;
        chutesdados++;

        

        // verifica se o jogador acertou a palavra
        verificapalavracerta();

        // atualiza as variaveis de controle do jogo
        if(acertouagora) {
            acertou = 1;
        } else {
            tentativas--;
            if(tentativas == 0) {
                enforcou = 1;
            }
        }
    }
    if(acertou) {
        printf("Parabéns! Você ganhou!\n");
    } else {
        printf("Você perdeu! A palavra era %s\n", palavrasecreta);
    }
    return 0;
}


   