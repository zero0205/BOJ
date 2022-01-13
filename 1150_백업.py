# n, k 입력받기
n, k = map(int, input().split())

prev = 0
gap = []

# 출발점에서부터 각 회사까지의 거리 입력
for i in range(n):
    now = int(input())
    if i == 0:
        prev = now
        continue
    else:
        gap.append((i - 1, i, (now-prev)))
        prev = now


 