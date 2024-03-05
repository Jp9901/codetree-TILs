a, b = map(int,input().split())
arr = list()

while a > 0:
    arr.append(a%b)
    a = a//b

sum_val = 0
for i in range(b):
    cnt = 0
    for ele in arr:
        if i == ele:
            cnt += 1
    sum_val += cnt**2
print(sum_val)