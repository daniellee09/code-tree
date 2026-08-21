n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.
tiles = [0] * 200001
pos = 100000
# 0 = 회색, 1 = 흰색, 2 = 검은색 
for i in range(len(x)):
    if dir[i] == "L":
        for j in range(x[i]):
            tiles[pos-j] = 1
        
        # 현재 칸을 1로 치니까 실제 이동은 x - 1 이다.
        pos -= x[i] - 1 
    
    else:
        for j in range(x[i]):
            tiles[pos+j] = 2
        
        pos += x[i] - 1

print(tiles.count(1), tiles.count(2))

