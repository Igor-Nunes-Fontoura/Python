num1 = input('Digite um valor: ')
num2 = input('Digite outro valor: ')

int_num1 = int(num1)
int_num2 = int(num2)

if int_num1 > int_num2:
    print(f'O primeiro valor {int_num1} é maior que o segundo valor {int_num2}')
elif int_num1 < int_num2:
    print(f'O segundo valor {int_num2} é maior que o primeiro valor {int_num1}')
else:
    print('Os dois valores são iguais')
