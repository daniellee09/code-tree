fruits = ["apple", "banana", "grape", "blueberry", "orange"]
chr = input()
cnt = 0

for str in fruits:
    if str[2] == chr or str[3] == chr:
        print(str)
        cnt += 1

print(cnt)

