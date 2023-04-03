p1 = {
    'nome': 'Igor',
    'sobrenome': 'Fontoura',
}

nome = p1.pop('nome')

print(nome)
print(p1)

p1.update({
    'nome': 'novo valor',
    'idade': 30,
})

print(p1)

ultima_chave = p1.popitem()

print(p1)
print(ultima_chave)