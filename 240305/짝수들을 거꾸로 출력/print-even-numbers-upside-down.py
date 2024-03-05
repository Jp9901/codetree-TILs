n = int(input())

arr = list(map(int,input().split()))

for ele in arr[::-1]:
    if ele%2 == 0:
        print(ele,end = " ")