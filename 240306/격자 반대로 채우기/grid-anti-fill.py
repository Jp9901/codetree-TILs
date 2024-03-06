n = int(input())

arr = list()
for i in range(n):
    arr1 = list(n*i+j+1 for j in range(n))
    arr.append(arr1)


for i in range(n):
    for j in range(n):
        if j%2 == 0:
            print(arr[n-1-j][i], end= " ")
        else:
            print(arr[n-1-j][n-1-i], end = " ")
    print()