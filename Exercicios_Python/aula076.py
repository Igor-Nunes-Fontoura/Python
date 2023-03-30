# Closure e funções que retornam outras funções

def criar_saudacao(saudacao, nome):
    def saudar():
        return f'{saudacao}, {nome}!'
    return saudar

s1 = criar_saudacao('Bom dia', 'Igor')
s2 = criar_saudacao('Boa tarde', 'Igor')

print(s1())
print(s2())