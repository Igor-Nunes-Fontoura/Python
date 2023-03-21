# Calculadora com while

while True:
    primeiro_numero = input('Digite o primeiro número: ')
    segundo_numero = input('Digite o segundo número: ')

    primeiro_numero_int = int(primeiro_numero)
    segundo_numero_int = int(segundo_numero)

    print('Selecione qual operação deseja realizar')
    print('[1] - Somar')
    print('[2] - Subtrair')
    print('[3] - Multiplicar')
    print('[4] - Dividir')
    opcao = input()

    if opcao == '1':
        soma = primeiro_numero_int + segundo_numero_int

        print(f'A soma entre {primeiro_numero} e {segundo_numero} é igual a {soma}')

    elif opcao == '2':
        subtracao = primeiro_numero_int - segundo_numero_int

        print(f'A subtração entre {primeiro_numero} e {segundo_numero} é igual a {subtracao}')

    elif opcao == '3':
        multiplicacao = primeiro_numero_int * segundo_numero_int

        print(f'A multiplicação entre {primeiro_numero} e {segundo_numero} é igual a {multiplicacao}')

    elif opcao == '4':
        divisao = primeiro_numero_int / segundo_numero_int

        print(f'A divisão entre {primeiro_numero} e {segundo_numero} é igual a {divisao}')

    else:
        print('Digite uma opção válida')

    sair = input('Quer sair? [S/N] ')
    if sair in 'Ss':
        break