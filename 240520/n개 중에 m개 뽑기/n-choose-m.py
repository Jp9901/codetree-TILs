n,m = map(int,input().split())

ans =[]

# num : 조합 내 마지막 수(비어있을 때, 값 = 0)


def choose(curr_num,num):
    if curr_num == m+1:
        print(*ans)
        return

    for i in range(1,n+1):
        # 조합 내 마지막 값과 i값 비교
        # => i값이 더 크다면 재귀함수
        if cnt < i :
            ans.append(i)
            choose(curr_num+1,i)
            ans.pop()
    return

choose(1,0)