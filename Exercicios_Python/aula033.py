numero = input('Digite um número inteiro: ')

try:
    numero_int = int(numero)

    if numero_int % 2 == 0:
        print(f'O número {numero_int} é par')
    else:
        print(f'O número {numero_int} não é par')
except:
    print('Você não digitou um inteiro!')