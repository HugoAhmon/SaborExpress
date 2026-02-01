# ========Exercícios========

# nome_pessoa = input('Digite seu nome: ')
# idade_pessoa = input('Digite sua idade: ')
# print(f'O nome digitado foi {nome_pessoa} e a idade digitada foi: {idade_pessoa} anos.')

#-----------------------------------------------------------------------------------------------------

#1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.
# numero = int(input('Digite um número: '))
# if numero % 2 == 0:                             #verifica se o resto da divisão por 2 é igual a 0
#     print(f'O número {numero} é par.')
# else:
#     print(f'O número {numero} é ímpar.')

#-----------------------------------------------------------------------------------------------------

#2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:

#Criança: 0 a 12 anos;
#Adolescente: 13 a 18 anos;
#Adulto: acima de 18 anos.

# idade = int(input('Digite sua idade: '))
# if idade >= 0 and idade <= 12:
#     print('Você é uma criança.')
#     #ou: if 0 <= idade <= 12:
# elif idade >= 13 and idade <= 18:
#     print('Você é um adolescente.')
# else:
#     print('Você é um adulto.')

#-----------------------------------------------------------------------------------------------------

#3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

# input_username = input('Digite o nome de usuário: ')
# input_password = input('Digite a senha: ')
# expected_username = 'admin'
# expected_password = 'senha123'
# if input_username == expected_username and input_password == expected_password:
#     print('Login bem-sucedido!')
# elif input_username != expected_username and input_password == expected_password:
#     print('Nome de usuário incorreto.')
#     #ou: elif not input_username == expected_username and input_password == expected_password:
# elif input_username == expected_username and input_password != expected_password:
#     print('Senha incorreta.')
#     #ou: elif input_username == expected_username and not input_password == expected_password:
# else:
#     print('Nome de usuário e senha incorretos.')

#-----------------------------------------------------------------------------------------------------

#4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:

# Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
# Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
# Terceiro Quadrante: os valores de x e y devem ser menores que zero;
# Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
# Caso contrário: o ponto está localizado no eixo ou origem.

# x = float(input('Digite a coordenada x: '))
# y = float(input('Digite a coordenada y: '))

# if x > 0 and y > 0:
#     print('O ponto está no primeiro quadrante.')
# elif x < 0 and y > 0:
#     print('O ponto está no segundo quadrante.')
# elif x < 0 and y < 0:
#     print('O ponto está no terceiro quadrante.')
# elif x > 0 and y < 0:
#     print('O ponto está no quarto quadrante.')
# else:
#     print('O ponto está localizado no eixo ou origem.')

#-------------------------------------------------------------------------------------

