#x를 찾는 이진탐색 함수 정의, 없으면 -1출력 
n,m = tuple(map(int,input().split()))
arr= list(map(int,input().split()))
targets= list(map(int,input().split()))

def find(arr, target):
    left=0
    right=n-1
    idx=n

    while left<=right:
        mid=(left+right)//2
        if arr[mid]>=target:
            idx=min(idx,mid)
            right=mid-1
        else: 
            left=mid+1
            
    if arr[idx]==target:
        return idx+1
    else:
        return -1

for i in range(m):
    target=targets[i]
    a= find(arr,target)
    print(a)