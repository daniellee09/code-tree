binary = list(map(int,(input())))
num = 0
# Please write your code here.
for i in range(len(binary)):
    num = num * 2 + binary[i]

print(num)