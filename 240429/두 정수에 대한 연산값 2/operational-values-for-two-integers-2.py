a, b = map(int, input().split())

# 계산 함수
def cal(n1,n2):
    if n1 > n2:
        return max(n1,n2)*2, max(n1,n2)+10
    else:
        return min(n1,n2)+10, max(n1,n2)*2

a, b = cal(a,b)
print(a,b)