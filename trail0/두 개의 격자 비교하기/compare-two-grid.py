n, m = map(int,input().split())
matrix1 = [[int(j) for j in input().split()] for _ in range(n)]
matrix2 = [[int(j) for j in input().split()] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if matrix1[i][j] == matrix2[i][j]:
            print(0, end=' ')
        else:
            print(1, end=' ')
    print()


