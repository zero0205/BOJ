import sys
from collections import deque

# n, m, v 입력받기
n, m, v = map(int, sys.stdin.readline().rstrip().split())

# 인접 리스트
array = [[] for _ in range(n + 1)]

# 방문한 노드인지 표시
visited_dfs = [False] * (n + 1) 
visited_bfs = [False] * (n + 1) 

# 간선 입력 받기
for i in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    # 연결 리스트 형태로 그래프 구성
    array[a].append(b)
    array[b].append(a)

# 정점 작은 번호부터 방문하려고 정렬
for arr in array:
    arr.sort()

# DFS
def dfs(v):
    # 현재 노드를 방문 처리
    visited_dfs[v] = True
    print(v, end=' ')

    for i in array[v]:
        if visited_dfs[i] == True:
            continue
        else:
            dfs(i)

# BFS
def bfs(v):
    # 시작 노드 큐에 넣기
    queue = deque([v])
    visited_bfs[v] = True
    # 큐가 빌 때까지 반복
    while queue:
        now = queue.popleft()
        print(now, end= ' ')

        for i in array[now]:
            if not visited_bfs[i]:
                queue.append(i)
                visited_bfs[i] = True
        

dfs(v)
print()
bfs(v)
