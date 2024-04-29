a,o,c = input().split()

a = int(a)
c = int(c)

# 사칙 연산 여부 판단 함수
def discriminate_cal(o):
    return o in ['+','-','/','*']

# 연산 함수
def calculation(a,o,c):
    if o =='+':
        return a+c
    elif o == '-':
        return a-c
    elif o =='/':
        return a//c
    else:
        return a*c


if discriminate_cal(o):
    print(f'{a} {o} {c} = {calculation(a,o,c)}')
else:
    print('False')