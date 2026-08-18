class Spot:
    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        self.num = num

coo = []
n = int(input())

for i in range(n):
    x, y = map(int,input().split())
    coo.append(Spot(x,y, i+1))

coo.sort(key = lambda x : (abs(x.x)+abs(x.y), x.num))

for c in coo:
    print(c.num)
