from random import randint
import os

numero_aleatorio = randint(1, 10) # Sorteia um número aleatório
contador = 0

print('!!!Adivinhe o número!!!')

while True:
    resposta = input('Escolha um número de 1 a 10: ') # Pede um número do usuário

    try:
        resposta_int = int(resposta) # Tenta transformar a resposta do usuário em um int
    except:
        os.system('clear')           # Se não conseguir, volta pro início do laço
        print('Digite um número!')
        continue

    if resposta_int >= 1 and resposta_int <=10: # Verifica se o número do usuário está entre 1 e 10
        contador += 1

        if resposta_int == numero_aleatorio: # Verifica se o número digitado é o mesmo sorteado
            os.system('clear')
            print('Parabéns, você acertou!!!')
            print(f'Você acertou o número {numero_aleatorio} em {contador} tentativas')
            break
    else:
        print('Este número não é válido!')