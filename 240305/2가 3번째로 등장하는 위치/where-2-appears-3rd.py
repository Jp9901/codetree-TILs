n = int(input())
arr = list(map(int,input().split()))

cnt = 0
cnt_2 = 0
for ele in arr:
    cnt += 1
    if ele == 2:
        cnt_2 += 1
    
    if cnt_2 == 3:
        break
print(cnt)