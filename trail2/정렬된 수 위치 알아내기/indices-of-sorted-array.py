class Sequence:
    def __init__(self, num, idx):
        self.num = num
        self.idx = idx


n = int(input())
numbers = list(map(int, input().split()))

seq = [Sequence(num, i+1) for i, num in enumerate(numbers)]

seq.sort(key=lambda x : (x.num, x.idx))

result = [0] * n
for i, elem in enumerate(seq):
    result[elem.idx - 1] = i+1

for elem in result:
    print(elem, end=" ")
