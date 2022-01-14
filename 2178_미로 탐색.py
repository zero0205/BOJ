from collections import deque
import queue

# N, M 입력받기
n, m = map(int,input().split())

input_data = []

# 미로 입력
for i in range(n):
    input_data.append(list(map(int, input())))

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 지나온 거리를 맵에 표시
def bfs():
    que = deque([(0,0)])

    while que:
        x, y = que.popleft()
        # 도착??
        if x == n-1 and y == m-1:
            break
        # 4방향 순회
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 갈 수 없는 칸이면 패스
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 갈 수 있는 칸(1)이면 (1,1)에서부터 그 칸까지의 거리 표시 & 큐에 추가
            if input_data[nx][ny] == 1:
                input_data[nx][ny] = input_data[x][y] + 1
                que.append((nx, ny))
            else:
                continue

bfs()
print(input_data[n-1][m-1])