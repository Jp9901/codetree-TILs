n = int(input())

arr = list()
for _ in range(n):
    arr.append(int(input()))

sum_val = list(str(sum(arr)))
print(''.join(sum_val[1:]),sum_val[0], sep="")