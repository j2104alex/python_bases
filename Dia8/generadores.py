# Yield
def mi_generador():
    for number in range(1,5):
        yield number*10

print(mi_generador())

g=mi_generador()
print(next(g))

print(next(g))

print(next(g))

print(next(g))

def generador():
    x=1
    yield x
    x+=1
    yield x
    x += 1
    yield x

gen=generador()

print(next(gen))
print(next(gen))
print(next(gen))