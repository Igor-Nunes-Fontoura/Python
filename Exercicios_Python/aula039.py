contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print('Não vou mostrar o 6')
        continue

    if contador >= 10 and contador <= 20:
        print('Não vou mostar o', contador)
        continue

    print(contador)

    if contador == 40:
        break