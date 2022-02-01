# k : 오영식이 갖고 있는 랜선의 개수, n : 필요한 랜선의 개수
k, n = map(int, input().split())

arr = []

# 이미 갖고 있는 각 랜선의 길이 입력받기
for _ in range(k):
    arr.append(int(input()))
    
arr.sort(reverse=True)
    
start = 1
end = arr[0]
mid = end
prev = arr[0]

def check_num(arr, mid):
    cnt = 0
    for el in arr:
        cnt += (el // mid)
    return cnt    

num = check_num(arr, mid)   # 일단 몇개로 나눠지는지 체크

while start <= end:
    if num == n:
        break
    prev = end
    mid = (start + end) // 2
    num = check_num(arr, mid)   # 몇개로 나눠지는지 체크
    
    if num < n:   # 적게 잘림 -> 더 작게 잘라야함
        end = mid - 1
    elif num > n:   # 많이 잘림 -> 크게 잘라야함
        start = mid + 1
        max = mid

if start > end:
    print(max)
else:
    while mid <= prev:
        if check_num(arr, mid) != num:
            break
        mid += 1
        
    print(mid - 1)