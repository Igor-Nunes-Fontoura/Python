from random import choice

print('-' * 15)
print('!!!Black Jack!!!')
print('-' * 15)

while True:
    baralho = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # Lista de cartas possiveis

    mao_usuario = [] # Criação de lista da mão do usuário
    mao_maquina = [] # Criação de lista da mão da maquina

    mao_usuario_somado = 0 # Criação de váriavel que guarda o valor da mão
    mao_maquina_somado = 0 # Criação de váriavel que guarda o valor da mão

    mao_usuario.append(choice(baralho)) # Sorteia uma carta aleatória e adiciona na mão
    mao_usuario.append(choice(baralho)) # Sorteia uma carta aleatória e adiciona na mão

    mao_maquina.append(choice(baralho)) # Sorteia uma carta aleatória e adiciona na mão
    mao_maquina.append(choice(baralho)) # Sorteia uma carta aleatória e adiciona na mão


    print(f'Sua mão atual é: {mao_usuario}') # Mostra pro usuário sua mão

    if (mao_usuario[0] == 1 and mao_usuario[1] == 10) or (mao_usuario[0] == 10 and mao_usuario[1] == 1): # Verifica se não ouve black jack
        print('-' * 15)
        print('BLACK JACK!!!')
        print('Você ganhou!!!')
        break

    if (mao_maquina[0] == 1 and mao_maquina[1] == 10) or (mao_maquina[0] == 10 and mao_maquina[1] == 1): # Verifica se não ouve black jack
        print('-' * 15)
        print('BLACK JACK!!!')
        print('A maquina ganhou!!!')
        break

    for carta in mao_usuario: # Soma o valor das cartas da mão
        mao_usuario_somado += carta

    for carta in mao_maquina: # Soma o valor das cartas da mão
        mao_maquina_somado += carta

    if mao_usuario_somado > 21: # Verifica se o valor da mão não passou de 21
        print('-' * 15)
        print('Você tem mais que 21, você perdeu!')
        break

    if mao_maquina_somado > 21: # Verifica se o valor da mão não passou de 21
        print('-' * 15)
        print('A maquina tem mais que 21, Você ganhou!')
        break

    opcao = input('Deseja comprar mais uma carta? [S/N] ').lower() # Pergunta se o jogador quer comprar mais cartas
    
    if opcao == 's': # Se sim, sorteia uma carta nova e adiciona a mão do usuário
        print('-' * 15)
        print('Você comprou uma carta!')
        mao_usuario.append(choice(baralho))
        print(f'Sua mão atual é: {mao_usuario}') # Mostra pro usuário sua nova mão

        mao_usuario_somado = 0
        for carta in mao_usuario: # Soma o valor das cartas da nova mão
            mao_usuario_somado += carta

        if mao_usuario_somado > 21: # Verifica se o valor da mão não passou de 21
            print('-' * 15)
            print('Você tem mais que 21, você perdeu!')
            break

    if mao_maquina_somado < 17: # Verifica se o valor da mão da maquina é menor que 17, se sim, compra mais uma carta
        print('-' * 15)
        print('A maquina comprou uma carta!')
        mao_maquina.append(choice(baralho))

        mao_maquina_somado = 0
        for carta in mao_maquina: # Soma o valor das cartas da nova mão
            mao_maquina_somado += carta

        if mao_maquina_somado > 21: # Verifica se o valor da mão não passou de 21
            print('-' * 15)
            print('A maquina tem mais que 21, Você ganhou!')
            break
    
    empate = mao_usuario_somado == mao_maquina_somado # Variavel que verifica se ouve empate
    usuario_ganhou = mao_usuario_somado > mao_maquina_somado # Variavel que verifica se o usuário ganhou

    if usuario_ganhou: # Verifica se usuario_ganhou é True, se sim, ele ganha
        print('-' * 15)
        print('Você ganhou!!!')
        print(f'Você tem {mao_usuario_somado} e a maquina {mao_maquina_somado}')
        break

    if not usuario_ganhou and not empate: # Verifica se usuario_ganhou e empate são False, se sim, maquina ganhou
        print('-' * 15)
        print('Maquina ganhou!!!')
        print(f'Você tem {mao_usuario_somado} e a maquina {mao_maquina_somado}')
        break

    if empate: # Verifica se empate é True
        print('-' * 15)
        print('Empatou!!!')
        print(f'Você tem {mao_usuario_somado} e a maquina {mao_maquina_somado}')
        break