li = list(input())

# 리스트 길이
n = len(li)

# 쌍의 수
cnt = 0

# '('로 시작할 때, ')'로 끝나는 경우
for i in range(n):
    if li[i] == '(':
        for j in range(i,n):
            if li[j] == ')':
                cnt += 1

print(cnt)