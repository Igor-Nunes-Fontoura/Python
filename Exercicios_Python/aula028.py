nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if not nome and not idade:
    print('Você não digitou seu nome nem sua idade!')
elif not nome:
    print('Você não digitou seu nome!')
elif not idade:
    print('Você não digitou sua idade!')
else:
    str_nome = str(nome)
    int_idade = int(idade)
    
    print(f'Seu nome é {str_nome}')
    print(f'Seu nome invertido é {str_nome[::-1]}')
    
    if ' ' in str_nome:
        print('Seu nome tem espaços')
    else:
        print('Seu não tem espaços')
    
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {str_nome[0]}')
    print(f'A última letra do seu nome é {str_nome[-1]}')