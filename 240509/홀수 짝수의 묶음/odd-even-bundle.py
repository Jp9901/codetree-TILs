n = int(input())
li = list(map(int,input().split()))

# 홀수 = 짝+홀 => 홀수일 때는 홀수 하나 이상이 필요
# 짝수 = 홀+홀 = 짝+짝

# 홀수, 짝수 개수
odd, even = 0,0
for num in li:
    if num%2 == 0:
        even += 1
    else:
        odd += 1

cnt = 0
while True:
    # 짝수 묶음 필요
    if cnt%2 == 0:
        # 짝수가 한 개 이상 존재할 때,
        if even:
            even -= 1
            cnt += 1
        
        # 짝수가 하나도 없을 때,
        elif odd >= 2:
            odd -= 2
            cnt += 1
        
        # 그룹을 만들지 못할 때,
        else:
            if even >0 or odd > 0:
                cnt -= 1

    # 홀수 묶음 필요
    else:
        # 홀수가 하나 이상 존재할 때,
        if odd:
            odd -= 1
            cnt += 1
        
        # 그룹을 만들지 못할 때,
        else:
            break

print(cnt)