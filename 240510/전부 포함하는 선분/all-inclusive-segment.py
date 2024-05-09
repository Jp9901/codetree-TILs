n = int(input())
x1,x2 = [],[]

for _ in range(n):
    a,b = map(int, input().split())
    x1.append(a)
    x2.append(b)

# 가장 왼쪽에 있는 선분을 없앨 때,
min_x1 = min(x1)
min_idx = x1.index(min_x1)

x1_L = [val for idx,val in enumerate(x1) if idx != min_idx]
x2_L = [val for idx,val in enumerate(x2) if idx != min_idx]
len_L = abs(max(x2_L)-min(x1_L))

# 가장 오른쪽에 있는 선분을 없앨 때,
max_x2 = max(x2)
max_idx = x2.index(max_x2)

x1_R = [val for idx,val in enumerate(x1) if idx != max_idx]
x2_R = [val for idx,val in enumerate(x2) if idx != max_idx]
len_R = abs(max(x2_R)-min(x1_R))

# 최소 길이
min_len = min(len_L,len_R)
print(min_len)