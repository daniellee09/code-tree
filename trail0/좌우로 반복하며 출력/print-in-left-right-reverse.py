n = int(input())

for i in range(n):
    row = []

    for j in range(n):
        row.append(j+1)
        
    
    if i % 2 == 1:
        for j in range(n-1, -1, -1):
            print(row[j], end='')
    else:
        for j in range(n):
            print(row[j], end='')

    print()
