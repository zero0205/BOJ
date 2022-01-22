from collections import deque

# 8방향(위부터 시계방향으로)
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1 , -1, -1]

def bfs(x, y, w, h, map_data):
    que = deque([(x, y)])
    
    while que:
        a, b = que.popleft()
        
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]
            # 범위 내가 아니면 그냥 패스
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            # 갈 수 있는 땅인가?
            if map_data[nx][ny] == 1:
                que.append((nx, ny))
                map_data[nx][ny] = 0    # 방문했으니 0으로 변경


while True:
    map_data = []
    cnt = 0
    
    # 너비(w)와 높이(h) 입력 (50 이하의 정수)
    w, h = map(int, input().split())
    # 입력 종료
    if w == 0 and h == 0:
        break
    
    # 맵 입력받기
    for i in range(h):
        map_data.append(list(map(int, input().split())))
        
    # 맵 탐색
    for i in range(h):
        for j in range(w):
            if map_data[i][j] == 1:
                bfs(i, j, w, h, map_data)
                cnt += 1
                
    print(cnt)
    map_data.clear()