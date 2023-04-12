import os, time

number1 = number2 = number1_float = number2_float = result = user_option = user_option_int = 0
account_list = []

def addition(n1=0, n2=0):
    return n1 + n2

def subtraction(n1=0, n2=0):
    return n1 - n2

def division(n1=0, n2=0):
    return n1 / n2

def multiplication(n1=0, n2=0):
    return n1 * n2

print('!!!CALCULATOR!!!')
while True:
    print('Which operation do you want to do?\n'
          '[1] - Addition\n'
          '[2] - Subtraction\n'
          '[3] - Division\n'
          '[4] - Multiplication\n'
          '[5] - Exit'
          )
    print('-' * 15)

    user_option = input()

    os.system('clear')

    try:
        user_option_int = int(user_option)
        if user_option_int > 5:
            print('Please enter a valid option!')
            continue
    except:
        print('Please enter a valid option!')
        continue

    if user_option_int == 5:
        print(f'You did {len(account_list)} operations')
            
        counter = 0
        for item in account_list:
            print(item[0], item[1], item[2], item[3], item[4])

        print('End of program')
        break

    number1 = input('Enter the first number: ')

    number2 = input('Enter the second number: ')
    
    os.system('clear')

    try:
        number1_float = float(number1)
        number2_float = float(number2)
    except:
        print('Please enter a valid option!')
        continue

    match user_option_int:
        case 1:
            result = addition(number1_float, number2_float)

            account_list.append([number1_float, '+', number2_float, '=', result])
            
            print(f'The sum of {number1_float} and {number2_float} equals {result}')
        
        case 2:
            result = subtraction(number1_float, number2_float)

            account_list.append([number1_float, '-', number2_float, '=', result])

            print(f'Subtraction between {number1_float} and {number2_float} equals {result}')

        case 3:
            result = division(number1_float, number2_float)

            account_list.append([number1_float, '/', number2_float, '=', result])

            print(f'Subtraction between {number1_float} and {number2_float} equals {result}')
        
        case 4: 
            result = multiplication(number1_float, number2_float)

            account_list.append([number1_float, '*', number2_float, '=', result])

            print(f'Subtraction between {number1_float} and {number2_float} equals {result}')

        case _:
            print('You have entered an invalid option, Try again!')
            continue
    
    time.sleep(1)