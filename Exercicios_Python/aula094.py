# Filtro em list comprehension

import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False)

lista = [n for n in range(10) if n < 5]

p(lista)