a, b = map(int,input().split())
n = list(input())

# 10진수
digit_10 = 0

for i in range(len(n)):
    digit_10  += int(n[-i])*(8**i)

# b진수
digit_b = list()
while True:
    if digit_10 < b:
        digit_b.append(digit_10)
        break

    digit_b.append(digit_10 % b)
    digit_10 //= b

for _ in digit_b[::-1]:
    print(_, end="")