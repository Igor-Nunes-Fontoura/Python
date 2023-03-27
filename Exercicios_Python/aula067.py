from random import randint

nove_digitos = ''

for i in range(9):
    nove_digitos += str(randint(0, 9))

mult_1 = 10
resultado_1 = 0

for digito in nove_digitos:
    resultado_1 += int(digito) * mult_1
    mult_1 -= 1

digito_1 = resultado_1 * 10 % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1)

mult_2 = 11
resultado_2 = 0

for digito in dez_digitos:
    resultado_2 += int(digito) * mult_2
    mult_2 -= 1

digito_2 = resultado_2 * 10 % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf = f'{nove_digitos}{digito_1}{digito_2}'

print(cpf)