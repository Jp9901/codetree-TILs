n,m = map(int,input().split())

ans =[]

# (이전 숫자 < 현재 숫자)인 개수


def choose(curr_num,cnt):
    if curr_num == m+1:
        # 한 조합 내에서 모든 숫자들이 오름차순으로 정렬되어 있을때,
        if cnt == m:
            print(*ans)
        return

    for i in range(1,n+1):
        ans.append(i)
        # 오름차순 체크
        if len(ans) == 1 or ans[-2] <= ans[-1]:
            cnt += 1
            print(ans, cnt)
        choose(curr_num+1,cnt)
        ans.pop()
    return

choose(1,0)