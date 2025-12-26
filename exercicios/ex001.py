import os

def numero_par_impar():

    numero = int(input('Digite um número:'))
    if numero % 2 == 0:
        print('O número é par.')
    else:
        print('O número é impar.')

def escolha_idade():

    idade = int(input('Digite sua idade:'))
    if 0 > idade <= 12:
        print('Criança') 
    elif 13 > idade <= 18:
        print('Adolescente')
    elif idade >= 18  :
        print('Adulto')
    else:
        print('Valor inválido')

def usuario_senha():

    usuario_correto = 'alura'
    senha_correta = 'alura123'

    usuario = input('Digite o usuário: ')
    senha = input('Digite a senha: ')

    if usuario == usuario_correto and senha_correta:
        print('Login bem sucedido!')
    else: 
        print('Credenciais inválidas, Tente novamente.')


def main():
    numero_par_impar()
    escolha_idade()
    usuario_senha()
    
if __name__ == '__main__':
        main()


