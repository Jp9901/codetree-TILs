n = int(input())
arr =[
    input().split() for _ in range(n)   
]

# 타일 개수 및 처음 위치 지정
num = 0
for i in range(n):
    num += int(arr[i][0])

tile = ["empty" for _ in range(4*num+1)]
pos = 2*num

# 타일 뒤집기
for i in range(n):
    x = int(arr[i][0])

    if arr[i][1] == 'R':
        for _ in range(x):
            tile[pos] = 'black'
            pos += 1
        else:
            pos = pos - 1 # 마지막에는 움직이지 않으므로 전 위치로
    else:
        for _ in range(x):
            tile[pos] = 'white'
            pos -= 1
        else:
            pos = pos + 1 # 마지막에는 움직이지 않으므로 전 위치로

# 타일 색 개수
cnt_wh = tile.count('white')
cnt_bl = tile.count('black')
print(cnt_wh,cnt_bl, sep = " " )