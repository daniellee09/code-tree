a, b = map(int,input().split())

while a <= b:
    print(a, end=' ')
    if a%2 == 1:
        a = 2 * a
    elif a % 2 == 0:
        a += 3
