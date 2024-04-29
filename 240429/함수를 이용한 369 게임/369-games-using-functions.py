a, b = map(int, input().split())

# 3,6,9 함수
def three_digit(num):
    return '3' in str(num) or '6' in str(num) or '9' in str(num)

# 3의 배수 함수
def three_multi(num):
    return num%3==0

# 숫자의 개수
cnt = 0

for i in range(a,b+1):
    if three_digit(i):
        cnt += 1
    elif three_multi(i):
        cnt += 1

print(cnt)