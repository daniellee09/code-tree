n = int(input())
SIZE = 200
OFFSET = 100
visited = [[0]*SIZE for _ in range(SIZE)]

for _ in range(n):
    a,b,c,d = map(int,input().split())
    a += OFFSET
    b += OFFSET
    c += OFFSET
    d += OFFSET
    
    for x in range(a,c):
        for y in range(b,d):
            visited[x][y] = 1

area = 0
for row in visited:
    area += sum(row)

print(area)
        
