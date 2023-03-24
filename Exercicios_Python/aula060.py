import os

lista = []

while True:
    os.system('clear')
    print('Selecione uma opção:')
    print('[I] Inserir')
    print('[A] Apagar')
    print('[L] Listar')
    print('[S] Sair')
    print('-' * 15)
    opcao = input().lower()
    print('-' * 15)

    if opcao not in 'ials':
        os.system('clear')
        print('Digite uma opção válida!')
        print('-' * 15)
        continue
    
    if opcao == 'i':
        os.system('clear')
        add_lista = input('Digite o item que deseja por na lista: ')
        print('-' * 15)
        lista.append(add_lista)
    
    if opcao == 'a':
        os.system('clear')
        apaga_indice = input('Digite o índice que deseja apagar: ')
        print('-' * 15)

        try:
            apaga_indice_int = int(apaga_indice)
            lista.pop(apaga_indice_int)
        except:
            print('Não foi possível apagar este índice!')
            print('-' * 15)
            continue
    
    if opcao == 'l':
        os.system('clear')
        for item in lista:
            print(item)
        
        print('-' * 15)

    if opcao == 's':
        os.system('clear')

        if len(lista) == 0:
            print('Sua lista ficou vazia!')
        else:
            print('Sua lista ficou:')

        for item in lista:
            print(item)

        break