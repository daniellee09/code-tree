a,b,c = map(int, input().split())

if (a>b):
    if(c>a):
        print(a)
    else:
        if(b>c):
            print(b)
        else:
            print(c)

if (b>a):
    if (c>b):
        print(b)
    else:
        if(a>c):
            print(a)
        else:
            print(c)