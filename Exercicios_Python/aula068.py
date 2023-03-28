# Indrodução às funções (def) em Python
# Funções são trechos de código usados para replicar determinada ação no seu código

def mostrar_na_tela():
    print('Mostrar 1')
    print('Mostrar 2')
    print('Mostrar 3')
    print('Mostrar 4')
    print('Mostrar 5')

mostrar_na_tela()

def somar(a = 0 , b = 0):
    print(f'A soma entre {a} e {b} é {a + b}')

somar(2, 2)