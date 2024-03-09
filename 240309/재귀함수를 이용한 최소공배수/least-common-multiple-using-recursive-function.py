def lcm(n, ele1, arr):
    if n == 0:
        return ele1
    ele2 = arr[n-1]
    
    for i in range(max(ele1,ele2),ele1*ele2+1):
        if i%ele1 ==0 and i%ele2 == 0:
            ans = i
            break
    return lcm(n-1, ans, arr)
    

n = int(input())

arr = list(map(int,input().split()))

print(lcm(n,1,arr))