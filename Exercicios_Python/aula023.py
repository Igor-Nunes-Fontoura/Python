# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True

print(not True) # False
print(not False) # True

senha = input('Senha: ')

if not senha:
    print('Senha incorreta')