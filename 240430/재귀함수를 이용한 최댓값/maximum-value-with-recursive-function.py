n = int(input())
li = list(map(int,input().split()))

# a번째 까지 인덱스의 숫자 중 가장 큰 값 반환
def max_value(a):
    if a == 0:
        return li[0]
    return max(max_value(a-1),li[a]) 

print(max_value(n-1))