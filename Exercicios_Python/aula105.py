import copy

def aumento(list):
    novos_produtos = copy.deepcopy(list)

    for item in novos_produtos:
        item['preco'] = item['preco'] + item['preco'] / 10
    
    return novos_produtos

def ordenar_por_nome(list):
    produtos_ordenados_por_nome = sorted(list, key=lambda p: p['nome'], reverse=True)

    return produtos_ordenados_por_nome

def ordenar_por_preco_crescente(list):
    produtos_ordenados_por_preco_crescente = sorted(list, key=lambda p: p['preco'])

    return produtos_ordenados_por_preco_crescente

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

novos_produtos = aumento(produtos)
produtos_ordenados_por_nome = ordenar_por_nome(produtos)
produtos_ordenados_por_preco_crescente = ordenar_por_preco_crescente(produtos)

print(*produtos, sep='\n')
print('-' * 50)
print(*novos_produtos, sep='\n')
print('-' * 50)
print(*produtos_ordenados_por_nome, sep='\n')
print('-' * 50)
print(*produtos_ordenados_por_preco_crescente, sep='\n')