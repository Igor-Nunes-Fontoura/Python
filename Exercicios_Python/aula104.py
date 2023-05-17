# Try, except, else e finally
try:
    a = 18
    b = 0
    print(a / b)

except ZeroDivisionError:
    print('Tentou dividir por zero')

except NameError:
    print('Nome b não está definido')
