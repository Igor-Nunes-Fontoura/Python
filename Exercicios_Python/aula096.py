produto = {
    'nome': 'Caneta',
    'preco': 2.5,
    'categoria': 'Escritorio',
}

dc = {
    chave: valor
    for chave, valor
    in produto.items()
}

print(dc)