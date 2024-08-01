# n,m=tuple(map(int,input().split()))
# points=list(map(int,input().split()))
# ab=[]
# for _ in range(m):
#     ab.append(tuple(map(int,input().split())))

# #점들 중에서, 선분 ab에 포함되는 개수 찾기
# #-> a보다 작은 인덱스 중 max
# #-> b보다 큰  인덱스 중 min
# points.sort()

# def lower(arr,target): 
#     left=0
#     right=n-1
#     idx=-1
#     while left<=right:
#         mid=(left+right)//2
#         if arr[mid]<target:
#             idx=max(mid,idx)
#             left=mid+1
#         else:
#             right=mid-1
#     #idx가 n-1보다 크거나 같으면 문제에 대한 답은 0
#     #idx가 -1이면 제일 작은 점부터 선분에 포함된다는 뜻
#     return idx 

# def upper(arr,target): 
#     left=0
#     right=n-1
#     idx= n
#     while left<=right:
#         mid=(left+right)//2
#         if arr[mid]>target:
#             idx=min(mid,idx)
#             right=mid-1
#         else:
#             left=mid+1
#     #idx가 n이면 제일 큰점부터 선분에 포함된다는 뜻
#     #idx가 0보다 작거나 같으면 문제에 대한 답은 0
#     return idx



# for a,b in ab:
#     low=lower(points,a)
#     up=upper(points,b)
#     if low>up:
#         print(0)
#     else:
#         print(up-low-1)





n,m=tuple(map(int,input().split()))
points=list(map(int,input().split()))
ab=[]
for _ in range(m):
    ab.append(tuple(map(int,input().split())))

#점들 중에서, 선분 ab에 포함되는 개수 찾기
#-> a보다 작은 인덱스 중 max
#-> b보다 큰  인덱스 중 min
points.sort()
def lower(arr,target): 
    left=0
    right=n-1
    idx=-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]<target:
            idx=max(mid,idx)
            left=mid+1
        else:
            right=mid-1
    #idx가 n-1보다 크거나 같으면 문제에 대한 답은 0
    #idx가 -1이면 제일 작은 점부터 선분에 포함된다는 뜻
    return idx 

def upper(arr,target): 
    left=0
    right=n-1
    idx= n
    while left<=right:
        mid=(left+right)//2
        if arr[mid]>target:
            idx=min(mid,idx)
            right=mid-1
        else:
            left=mid+1
    #idx가 n이면 제일 큰점부터 선분에 포함된다는 뜻
    #idx가 0보다 작거나 같으면 문제에 대한 답은 0
    return idx



for a,b in ab:
    low=lower(points,a)
    up=upper(points,b)
    if low>=n-1 or up<=0:
        print(0)
        continue
    print(up-low-1)