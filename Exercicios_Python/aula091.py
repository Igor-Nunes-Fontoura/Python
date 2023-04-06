# Empacotamento e desempacotamento de dicionários

pessoa = {
    'nome': 'Igor',
    'sobrenome': 'Fontoura',
}

dados_pessoa = {
    'idade': 20,
    'altura': 1.75,
}

pessoa_completa = {**pessoa, **dados_pessoa}

print(pessoa_completa)

def mostra_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS: ', args)
    
    for chave, valor in kwargs.items():
        print(chave, valor)

mostra_argumentos_nomeados(**pessoa_completa)