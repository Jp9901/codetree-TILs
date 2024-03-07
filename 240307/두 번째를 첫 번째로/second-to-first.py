string = input()

ch = string[1]

ans = string[0]

for i in range(1,len(string)):
    if ch == string[i]:
        ans += string[0]
    else:
        ans += string[i]

print(ans)