n = list(map(int,list(input())))

# 최댓값
max_val = 0

# 이진수에서 가장 앞 쪽에 있는 0 값을 변환(없을 시 마지막 1->0)
for i in range(len(n)):
    value = 0 

    if n[i] == 0:
        n[i] = 1
        break
else:
    n[-1] = 0

for idx, value in enumerate(n[::-1]):
    max_val += value * 2**idx

print(max_val)