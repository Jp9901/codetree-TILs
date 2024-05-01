ch1 = list(input())
ch2 = list(input())

ch1.sort()
ch2.sort()

if ch1 == ch2:
    print('Yes')
else:
    print("No")