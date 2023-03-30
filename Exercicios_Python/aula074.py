def multiplicar(*args):
    total = 1
    for numeros in args:
        total *= numeros
    return total

def par_ou_impar(n):
    return n % 2 == 0

mult = multiplicar(1, 2, 3, 4, 5)
print(mult)

print(par_ou_impar(mult))