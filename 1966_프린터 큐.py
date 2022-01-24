# 테스트 케이스 개수
from collections import deque

t = int(input())    # t : 테스트 케이스 개수

for i in range(t):
    # n : 문서의 개수, m : 순서 궁금한 문서의 순서(현재 큐에서)
    n, m = map(int, input().split())
    que = deque(list(map(int, input().split())))
    cnt = 0
    
    while que:
        max_num = max(que)
        pop_num = que.popleft()
        m -= 1
        
        # 큐 맨 앞의 문서 우선순위가 가장 높음
        if max_num == pop_num:
            cnt += 1
            if m == -1: # 내 문서가 처리될 차례
                break
        # 큐 맨 앞의 문서보다 우선순위가 높은 문서가 뒤에 있음
        else:   
            que.append(pop_num)
            if m == -1:
                m = len(que) - 1
    print(cnt)