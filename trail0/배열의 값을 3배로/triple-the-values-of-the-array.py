matrix = []
for i in range(3):
    r = list(map(int, input().split()))
    new_r = []
    for j in range(3):
        new_r.append(r[j]*3)    
    matrix.append(new_r)

for row in range(3):
    for col in range(3):
        print(matrix[row][col], end=' ')
    print()
