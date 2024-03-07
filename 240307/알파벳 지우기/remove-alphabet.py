A = list(input())
B = list(input())

arr1 = list()
arr2 = list()
sum_val = 0

for ele in A:
    if ele.isdigit():
        arr1.append(ele)
sum_val += int("".join(arr1))

for ele in B:
    if ele.isdigit():
        arr2.append(ele)  
sum_val += int("".join(arr2))

print(sum_val)