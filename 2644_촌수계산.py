from collections import deque

def bfs(a, b, ad_list, visited):
    # 현재 노드 방문 처리 & 큐에 넣기
    visited[a] = 1
    que = deque([a])

    while que:
        v = que.popleft()
        
        # 촌수 찾음
        if v == b:
            return
        for i in ad_list[v]:
            if visited[i] != 0: # 이미 방문한 노드
                continue
            que.append(i)
            visited[i] = visited[v] + 1

n = int(input())    # 사람 수
a, b = map(int, input().split())    # 촌수 계산해야하는 두 사람
m = int(input())    # 부모 자식 관계 개수(부모는 최대 한 명만 주어짐)

adjency_list = [[] for i in range(n + 1)]
visited = [0 for _ in range(n + 1)]

for i in range(m):
    x, y = map(int, input().split()) 
    adjency_list[x].append(y)
    adjency_list[y].append(x)

bfs(a,b,adjency_list, visited)

print(visited[b] - 1)