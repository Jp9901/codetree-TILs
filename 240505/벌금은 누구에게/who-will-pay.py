n, m, k = map(int,input().split())

# 1~n번 까지의 학생의 벌칙 횟수 (첫 인덱스는 제외)
li = [-1]+[0]*n

# 벌금을 낼 최초의 학생 (없을 시 -1 출력)
fir_stu = -1 
for _ in range(m):
    i = int(input())
    li[i] += 1
    if li[i] == k and fir_stu == -1:
        fir_stu = i

print(fir_stu)