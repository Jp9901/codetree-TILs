n=int(input())
l=[i+1 for i in range(n)]
from itertools import permutations
all_perm=[list(a) for a in permutations(l,n)]
all_perm.sort(reverse=True)
for perm in all_perm:
    for i in range(n):
        if i==n-1:
            print(perm[i])
        else:
            print(perm[i],end=' ')