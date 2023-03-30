# args - Argumentos não nomeados

x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total

soma_1 = soma(1, 2, 3)
soma_2 = soma(4, 5, 6)
soma_3 = soma(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

print(soma_1)
print(soma_2)
print(soma_3)