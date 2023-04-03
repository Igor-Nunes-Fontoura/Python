perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

contador = acertos = 0

for item in perguntas:
    pergunta = perguntas[contador].get('Pergunta')
    opcoes = perguntas[contador].get('Opções')
    resposta_certa = perguntas[contador].get('Resposta')

    print(f'Pergunta: {pergunta}')
    print('Opções:')
    print(f'0) {opcoes[0]}')
    print(f'1) {opcoes[1]}')
    print(f'2) {opcoes[2]}')
    print(f'3) {opcoes[3]}')
    resposta = input('Escolha uma opção: ')
    print('-' * 15)

    resposta_int = int(resposta)

    if opcoes[resposta_int] == resposta_certa:
        print('Você acertou!!!')
        print('-' * 15)
        acertos += 1
    else:
        print('Você errou!!!')
        print('-' * 15)

    contador += 1

print(f'Você acertou {acertos} de {contador} perguntas')