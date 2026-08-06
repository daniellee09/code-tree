def find_number(a,b):
    cnt = 0
    for i in range(a,b+1):
        num_string = set(str(i))
        if num_string & {'3','6','9'} or i%3 == 0:
            cnt += 1
    return cnt


a,b = map(int,input().split())
print(find_number(a,b))
