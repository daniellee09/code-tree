n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
# 1. N개의 0으로 초기화된 리스트 생성
num = [0 for _ in range(n+1)]

# 2. 명령 수행
# commands에 저장된 각 튜플들 A번부터 B번 칸까지 블럭 1개씩 쌓기
for start, end in commands:
    for i in range(start, end+1):
        num[i] += 1

print(max(num))