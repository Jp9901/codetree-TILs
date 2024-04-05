n=int(input())

R=0
L=0

for _ in range(n):
    stiring=input()
    k=int(stiring.split()[0])
    drec=stiring.split()[1]

    if drec=='R':
        R+=k
    else:
        L+=k


if R>=L:
    print(L)
else:
    print(R)