from collections import deque

# n : 컴퓨터의 수
n = int(input())

# m : 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수
m = int(input())

# 인접 리스트 생성
array = [[] for _ in range(n + 1)]

# 방문 노드 처리 위해서
visited = [False] * (n + 1)

# 네트워크 상에서 직접 연결되어 있는 컴퓨터들 입력받기
for i in range(m):
    a, b = map(int, input().split())
    array[a].append(b)
    array[b].append(a)

def bfs():
    que = deque([1])
    visited[1] = True
    cnt = 0

    while que:
        v = que.popleft()

        for i in array[v]:
            if not visited[i]:
                que.append(i)
                visited[i] = True
                cnt += 1
    return cnt

print(bfs())