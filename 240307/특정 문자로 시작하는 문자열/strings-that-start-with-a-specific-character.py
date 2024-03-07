n = int(input())

arr = list()
for _ in range(n):
    arr.append(input())

alpha = input()

sum_val = 0
cnt = 0
for ele in arr:
    if ele[0] == alpha:
        sum_val += len(ele)
        cnt += 1

print(f"{cnt} {sum_val/cnt:.2f}")