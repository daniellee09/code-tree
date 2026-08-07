def func1(a,b):
    if a < b:
        a += 10
        b *= 2
        return a, b
    else:
        a *= 2
        b += 10
        return a, b

a,b = map(int, input().split())
x, y = func1(a,b)
print(x, y)

    
    