n, k = map(int, input().split())

# 바구니의 좌표와 각 사탕의 개수
value = [0]*101

# 바구니의 좌표에 사탕 추가(같은 좌표에 여러 바구니 가능)
for _ in range(n):
    num, x = map(int,input().split())
    value[x] += num

# [c-K,c+K]구간에 사탕의 수
max_cnt = 0
for c in range(0,101):
    # 구간의 한계 지정
    lower = max(c-k,0)
    upper = min(c+k,100)
    # if lower <0:
    #     lower =0

    # if upper > 100:
    #     upper = 100
    
    cnt = sum(value[lower:(upper+1)])
    max_cnt = max(max_cnt,cnt)

print(max_cnt)