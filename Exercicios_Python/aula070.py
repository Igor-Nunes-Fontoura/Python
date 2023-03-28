# Valores padrão para parâmetros

def soma(x, y, z = None):
    if z is not None:
        print(x + y + z)
    else:
        print(x + y)

soma(1, 2)
soma(3, 5)
soma(7, 9, 4)