# Generator functions em Python

def generator(n=0):
    yield 1
    print('Continuando...')
    yield 2
    print('Mais uma...')
    yield 3
    print('Vou terminar')
    return 'ACABOU'

gen = generator(n=0)

for n in gen:
    print(n)