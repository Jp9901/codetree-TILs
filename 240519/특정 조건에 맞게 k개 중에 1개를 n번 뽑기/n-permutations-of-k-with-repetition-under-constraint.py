k,n = map(int,input().split())

ans = []

def choose(curr_num):
    if curr_num == n+1:
        print(*ans)
        return
    
    for i in range(1,k+1):
        # 같은 숫자가 3번 이상 연속
        if (curr_num == 1 or curr_num == 2) or (ans[-1] != i or ans[-2] != i):
            ans.append(i)
            choose(curr_num+1)
            ans.pop()

    return

choose(1)