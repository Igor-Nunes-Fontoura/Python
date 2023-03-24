from random import choice
import os

print('!!!Pedra, Papel ou Tesoura!!!')

while True:
    jogada_usuario = input('Qual sua jogada? ').upper() # Pede que o usuário digite sua jogada e deixa a resposta em maiúsculo

    jogadas_possiveis = ['PEDRA', 'PAPEL', 'TESOURA'] # Lista com as jogadas possíveis

    if jogada_usuario in jogadas_possiveis: # Verifica se a jogada do usuário é válida dentro da lista de jogadas possíveis
        jogada_maquina = choice(jogadas_possiveis) # Sorteia uma jogada aleatória para a maquina

        empate = jogada_usuario == jogada_maquina # Váriavel para verificar se ouve um empate
        maquina_ganha = (jogada_usuario == jogadas_possiveis[0] and jogada_maquina == jogadas_possiveis[1])\
        or (jogada_usuario == jogadas_possiveis[1] and jogada_maquina == jogadas_possiveis[2])\
        or (jogada_usuario == jogadas_possiveis[2] and jogada_maquina == jogadas_possiveis[0]) # Váriavel para verificar se a maquina ganhou


        if maquina_ganha: # Verifica se maquina ganhou
            os.system('clear')
            print('Você perdeu!')
            print(f'A maquina escolheu {jogada_maquina} e você escolheu {jogada_usuario}')
        
        if not maquina_ganha and not empate: # Verifica se o usuário ganhou, partindo do principio que se a maquina nao ganhou e não ouve empate
            os.system('clear')
            print('Você ganhou!')
            print(f'A maquina escolheu {jogada_maquina} e você escolheu {jogada_usuario}')

        if empate: # Verifica se não ouve empate
            os.system('clear')
            print('Empatou!')
            print(f'A maquina escolheu {jogada_maquina} e você escolheu {jogada_usuario}')
        
    else:
        print('Escolha uma opção válida!')
        continue