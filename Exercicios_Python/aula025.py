# Interpolação básica de strings
# s -> String
# d e i -> int
# f -> float
# x e X -> hexadecimal (ABCDEF0123456789)

nome = 'Igor'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)

print(variavel)