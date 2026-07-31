a, b = map(int, input().split())

li1 = [a, b]

for i in range(8):
    if (li1[i]+li1[i+1])<10:
        li1.append(li1[i]+li1[i+1])
    else:
        li1.append((li1[i]+li1[i+1])%10)

for j in li1:
    print(j, end=' ')

    