# while/else

string = 'Valor qualquer'

i = 0

while i < len(string):
    letra = string[i]

    if letra == ' ':
        print(f'Encontrei um espaço no indice {i}')
        break

    i += 1
else:
    print('Não tem espaço na string')