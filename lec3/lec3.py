

def f(x):
    return x**3



list = [(i,f(i)) for i in range(1, 15) if i % 2 == 0]
print(list)
