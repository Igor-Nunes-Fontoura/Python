# Iterando strings com while

nome = 'Andrei'
tamanho_nome = len(nome)
nova_string = ''
contador = 0

while contador < tamanho_nome:

    if contador == tamanho_nome - 1:
        nova_string += nome[contador]
        contador += 1
        continue

    nova_string += nome[contador] + "-"

    contador += 1

print(nova_string)