iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable) # ter __iter__ e __next__

generator = (n for n in range(10000))

print(generator)

print(next(generator))
print(next(generator))
print(next(generator))