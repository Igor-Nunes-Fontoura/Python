'''
Repetição
while
Executa uma ação enquanto uma condição for verdadeira
'''

while True:
    nome = input('Digite seu nome: ')
    
    if nome == 'sair':
        break

    print(f'Seu nome é {nome}')