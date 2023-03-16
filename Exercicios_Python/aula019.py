# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser verdadeiras

entrada = input('Entrar ou sair? [E/S] ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if entrada == 'E'and senha_digitada == senha_permitida:
    print('Entrar')
elif entrada == 'S':
    print('Sair')
else:
    print('Senha incorreta')