def get_sum(a1, a2):
    global list1
    total = 0
    for i in range(a1-1, a2):
        total += list1[i]
    
    return total

n,m = map(int, input().split())
list1 = list(map(int, input().split()))
for i in range(m):
    a1, a2 = map(int, input().split())
    print(get_sum(a1,a2))




        
