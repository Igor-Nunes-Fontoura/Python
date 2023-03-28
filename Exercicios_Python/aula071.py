# Escopo de funções em Python

x = 0

def escopo():
    x = 1
    print(x)

print(x)

escopo()