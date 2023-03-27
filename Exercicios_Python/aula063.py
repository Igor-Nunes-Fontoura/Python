# Lista de listas e seus índices

salas = [
    ['Maria', 'Helena'],
    ['Elaine'],
    ['Luiz', 'João', 'Eduarda'],
]

print(salas[1][0])
print(salas[0][1])
print(salas[2][2])

print('-'*15)

for sala in salas:
    for aluno in sala:
        print(aluno)