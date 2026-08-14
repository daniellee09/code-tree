n = int(input())
numbers = [int(x) for x in input().split()][:n]

def median(numbers):
    sorted_num = sorted(numbers)
    length = len(numbers)
    mid = length // 2

    if n % 2 == 0:
        return (sorted_num[mid-1] + sorted_num[mid]) / 2
    else:
        return sorted_num[mid]
    
new_list = []
result = []
# 홀수번째의 원소마다의 중앙값을 저장함
for i in range(1,len(numbers)+1):
    new_list.append(numbers[i-1])
    if i % 2 != 0:
        result.append(median(new_list))
    else:
        continue

for elem in result:
    print(elem, end=' ')