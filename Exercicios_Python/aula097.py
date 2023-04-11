lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2), {0, 1}, {'nome': 'Igor'}
]

for item in lista:
    print(item, isinstance(item, set))