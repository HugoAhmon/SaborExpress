#Bibliotecas
import os         #importa a biblioteca os para interações com o sistema operacional


#Variaveis globais
APP_NAME = 'SaborExpress'
#nome_restaurantes = ['UAL Delicias', 'Mama Mia']  # Lista para armazenar os nomes dos restaurantes cadastrados
nome_restaurantes = [{'nome': 'UAL Delicias', 'categoria': 'Brasileira', 'status': False}, 
                     {'nome': 'Mama Mia', 'categoria': 'Italiana', 'status': True}]  # Dicionário para armazenar os nomes dos restaurantes cadastrados com status



# SaborExpress - Aplicativo de Delivery de Comida
def exibir_nome_do_app():
    print(f'{APP_NAME}!\n')

# Function
# Função Retornar ao menu principal
def retornar_ao_menu():
    input('Pressione Enter para continuar...')  # Pausa para o usuário ler a mensagem
    main()  # Retorna ao menu principal

# Função para exibir Submenu
def exibir_submenu(texto):
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa o terminal de forma compatível com Windows e Unix
    print(f'{texto}\n')

# Exibir menu de opções
def exibir_menu():
    print('Bem-vindo ao SaborExpress, seu aplicativo de delivery de comida favorito!')
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurantes')
    print('3. Ativação Restaurante')
    print('4. Sair\n')

# Função para finalizar o aplicativo
def finalizar_app():
    exibir_submenu('Finalizando o aplicativo...')

#Função opçao invalida
def opcao_invalida():
    print('Opção inválida. Por favor, escolha uma opção válida.\n')
    retornar_ao_menu()

#Função para cadastrar restaurante
def cadastrar_restaurante():
    '''
    Docstring for cadastrar_restaurante
    Função para cadastrar um novo restaurante no sistema.
    Solicita ao usuário o nome e a categoria do restaurante,
    cria um dicionário com essas informações e adiciona à lista de restaurantes.
    Exibe uma mensagem de sucesso e retorna ao menu principal.
    
    INPUTS:
    - nome_restaurante: Nome do restaurante a ser cadastrado (string).
    - categoria_restaurante: Categoria do restaurante (string).

    OUTPUTS:
    - Mensagem de confirmação do cadastro.
    RETURNS:
    - None
    '''
    exibir_submenu('Cadastro de Novos Restaurantes\n')
    nome_restaurante = input('Digite o nome do restaurante: ')
    categoria_restaurante = input(f'Digite a categoria do restaurante {nome_restaurante}: ')
    novo_restaurante = {'nome': nome_restaurante, 'categoria': categoria_restaurante, 'status': False}
    #nome_restaurantes.append(novo_restaurante) # Adiciona o restaurante à lista. | append = adicionar no final da lista | Usado quando a lista já existe
    dados_do_restaurante = {'nome': nome_restaurante, 'categoria': categoria_restaurante, 'status': False}  # Usado com Dicionário | status sempre inicia como False (inativo)
    nome_restaurantes.append(dados_do_restaurante)  # Adiciona o restaurante à lista de dicionários
    print(f'Restaurante {nome_restaurante} cadastrado com sucesso!\n')
    retornar_ao_menu()


#Função para listar restaurantes
def listar_restaurantes():
    exibir_submenu('Lista de Restaurantes Cadastrados:')
    for idx, restaurante in enumerate(nome_restaurantes, start=1):  #enumerate para numerar a lista. start=1 para começar a numeração do 1. 
        status = 'Ativo' if restaurante['status'] else 'Inativo'
        print(f'{idx}. {restaurante['nome']} - Categoria: {restaurante['categoria']} - Status: {status}\n')
    retornar_ao_menu()

# Função Status do restaurante
'''
Função para ativar ou desativar um restaurante existente.
Solicita ao usuário o nome do restaurante, verifica se ele existe na lista,
alterna seu status entre ativo e inativo, e exibe uma mensagem com o status atual.
Retorna ao menu principal após a operação.

Inputs:
- nome_restaurante: Nome do restaurante a ser ativado ou desativado (string).
Outputs:
- Mensagem indicando o novo status do restaurante ou se não foi encontrado.
Returns:
- None
'''
def alternar_status_restaurante():
    exibir_submenu('Ativação de Restaurante\n')
    nome_restaurante = input('Digite o nome do restaurante a ser ativado ou desativado: ')
    restaurante_encontrado = False
    for restaurante in nome_restaurantes:
        if restaurante['nome'].lower() == nome_restaurante.lower():  # .lower() para ignorar maiúsculas/minúsculas
            restaurante_encontrado = True
            restaurante['status'] = not restaurante['status']  # Alterna o status entre True e False
            status_atual = 'ativo' if restaurante['status'] else 'inativo' # Ternario para definir o status atual como string
            print(f'Restaurante {restaurante['nome']} agora está {status_atual}.\n')
            break
    if not restaurante_encontrado:
        print(f'Restaurante {nome_restaurante} não encontrado.\n')

    retornar_ao_menu()

# Capturar a opção do usuário
def capturar_opcao():
    # try except para tratar erro caso o usuário digite algo que não seja número
    try:
        opcao_escolhida = int(input('Escolha uma opção: ')) # Transformei em int aqui
        print(f'Opção escolhida: {opcao_escolhida}')

        # # Processar a opção escolhida
        # if opcao_escolhida == 1:
        #     nome_restaurante = input('Digite o nome do restaurante: ')
        #     print(f'Restaurante {nome_restaurante} cadastrado com sucesso!')
        # elif opcao_escolhida == 2:
        #     print('Listando restaurantes cadastrados...')
        # elif opcao_escolhida == 3:
        #     nome_restaurante = input('Digite o nome do restaurante a ser ativado: ')
        #     print(f'Restaurante {nome_restaurante} ativado com sucesso!')
        # elif opcao_escolhida == 4:
        #     finalizar_app()
        # else:
        #     print('Opção inválida. Por favor, escolha uma opção válida.')

        #Mesma função usando match case (Python 3.10+)
        match opcao_escolhida:
            case 1:
                cadastrar_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                alternar_status_restaurante()
            case 4:
                 finalizar_app()
            # case _:
            #     opcao_invalida()
    except ValueError:
        opcao_invalida()

# Função principal do aplicativo
def main():
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa o terminal ao iniciar o aplicativo
    exibir_nome_do_app()
    exibir_menu()
    capturar_opcao()

# Função principal para executar o aplicativo
if __name__ == '__main__':
    main()