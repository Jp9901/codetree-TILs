n = int(input())

nums = [0]+list(map(int,input().split()))

for i in range(1,n+1):
    if i%2 == 1:
        nums.sort()
        print(nums[i//2+1], end=' ')