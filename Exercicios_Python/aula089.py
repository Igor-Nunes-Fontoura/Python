# Função lambda em Python

lista = [
    {'nome': 'Igor', 'sobrenome': 'Fontoura'},
    {'nome': 'Vitor', 'sobrenome': 'Fontoura'},
    {'nome': 'Andrei', 'sobrenome': 'Fontoura'},
]

lista.sort(key=lambda item: item['nome'])

for item in lista:
    print(item)