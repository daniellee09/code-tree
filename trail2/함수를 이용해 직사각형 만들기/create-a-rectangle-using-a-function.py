def square_one(n,m):
    for i in range(n):
        for j in range(m):
            print(1, end='')
        print()

n, m = map(int, input().split())
square_one(n,m)
