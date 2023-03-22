print('Bem vindo ao jogo da palvra secreta!')
print('Esse jogo consiste em:')
print('Eu pensar em uma palavra mas não te contar qual')
print('E você tentar adivinhar a palavra apenas dizendo as letras')
print('Vamos começar!!!')
print('-'*50)

palavra_secreta = 'Python'.lower()
letras_acertadas = ''
contador = 0

while True:
    letra_digitada = input('Digite uma letra: ').lower()

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra')
        continue

    contador += 1

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('palavra formada: ', palavra_formada)
    
    if palavra_formada == palavra_secreta:
        print('Parabéns, você ganhou!!!')
        print(f'A palavra secreta era: {palavra_secreta}')
        print(f'E voçê acertou em {contador} tentativas')
        break