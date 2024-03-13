N, T = map(int, input().split())
order = input()

arr = [
    list(map(int,input().split())) for _ in range(N)
]

direction = 0
x,y = N//2,N//2
sum_val = arr[x][y]

for ele in order:
    if ele == 'L':
        direction += -1
    elif ele == 'R':
        direction += 1
    else:
        if direction%4 == 0:
            if x != 0:
                x -= 1
                sum_val += arr[x][y]

        elif direction%4 == 1:
            if y != (N-1):
                y += 1
                sum_val += arr[x][y]

        elif direction%4 == 2:
            if x != (N-1):
                x += 1
                sum_val += arr[x][y]

        else:
            if y != 0:
                y -= 1
                sum_val += arr[x][y]

print(sum_val)