n, m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

# 행복한 수열
def happy_seq(arr1):
    cnt = 1
    max_cnt = cnt
    for i in range(1,n):
        if arr1[i-1] == arr1[i]:
            cnt += 1
            max_cnt = max(max_cnt,cnt)
            
        else:
            cnt = 1

    if max_cnt >= m:
                return 1
        
    return 0

# 완전탐색
num = 0

# 행에 대해,
for row in range(n):
    tmp1 = arr[row]
    num += happy_seq(tmp1)


# 열에 대해,
for col in range(n):
    tmp2 = []
    for row in range(n):
        tmp2.append(arr[row][col])
    num += happy_seq(tmp2)
print(num)