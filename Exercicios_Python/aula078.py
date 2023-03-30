# Dicionarios em Python
# par de CHAVE e VALOR

pessoa = {
    'nome': 'Igor',
    'sobrenome': 'Fontoura',
    'idade': 20,
    'altura': 1.75,
    'enderecos': [
        {'rua': 'tal tal', 'numero': 123},
        {'rua': 'tal tal', 'numero': 321},
    ]
}

for chave in pessoa:
    print(chave, pessoa[chave])