nome = input('Digite seu nome: ')

curto = len(nome) <= 4
medio = len(nome) >= 5 and len(nome) <= 6
grande = len(nome) >= 7

if curto is True:
    print('Seu nome é curto')

if medio is True:
    print('Seu nome é médio')

if grande is True:
    print('Seu nome é grande')
