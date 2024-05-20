n = int(input())

ans = []
visited = [False]*(n+1)

def choose(curr_num):
    if curr_num == n+1:
        print(*ans)
        return

    for i in range(1, n+1):
        if visited[i]:
            continue
            
        ans.append(i)
        visited[i] = True
        choose(curr_num+1)
        ans.pop()
        visited[i] = False
    
    return

choose(1)