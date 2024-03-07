A = input()
ans = list(A)

LR = list(input())

for ele in LR:
    if ele == "R":
        ch = ans.pop()
        ans.insert(0,ch)
    else:
        ch = ans.pop(0)
        ans.insert(len(A),ch)

print("".join(ans))