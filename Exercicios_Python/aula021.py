# Operadores lógicos
# or - Qualquer condição verdadeira avaliada

entrada = input('Entrar ou sair: [E/S]')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')