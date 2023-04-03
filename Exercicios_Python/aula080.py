# Métodos úteis dos dicionários em Python

pessoa = {
    'nome': 'Igor',
    'sobrenome': 'Fontoura',
}

pessoa.setdefault('idade', 0)

print(pessoa['idade'])

print(len(pessoa))

print(list(pessoa.keys()))

print(list(pessoa.values()))

print(list(pessoa.items()))