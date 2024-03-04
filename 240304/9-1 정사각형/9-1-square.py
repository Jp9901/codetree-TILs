n = int(input())

num = 9
for _ in range(n):
    for _ in range(n):
        if num == 0:
            num = 9
        print(num, end='')
        num -= 1
    print()