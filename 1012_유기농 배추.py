from collections import deque

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, map_data):
    que = deque([(x, y)])
        
    while que:
        a, b = que.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            # 범위를 벗어나는지?
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 배추가 심어져있는지?
            if map_data[nx][ny] == 1:
                que.append((nx, ny))
                map_data[nx][ny] = 0    # 이미 지나간 칸 표시


t = int(input())    # 테스트케이스 개수

for j in range(t):
    m, n, k = map(int, input().split()) # 가로, 세로, 배추 위치 개수
    map_data = [[0] * m for _ in range(n)]

    # 배추 심어진 위치 입력받기
    for i in range(k):
        x, y = map(int, input().split())
        map_data[y][x] = 1

    cnt = 0
        
    for row in range(n):
        for col in range(m):
                if map_data[row][col] == 1:
                    bfs(row, col, map_data)
                    cnt += 1

    print(cnt)