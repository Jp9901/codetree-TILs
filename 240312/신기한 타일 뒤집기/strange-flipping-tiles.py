n = int(input())
arr =[
    input().split() for _ in range(n)   
]

# 타일 개수 및 처음 위치 지정
num = 0
for i in range(n):
    num += int(arr[i][0])

tile = [0 for _ in range(4*num+1)]
pos = 2*num

# 타일 뒤집기
for i in range(n):
    x = int(arr[i][0])
    if arr[i][1] == 'R':
        tile[pos:(pos+x+1)] = [-1 for _ in range(x)] # black
        pos = pos + (x-1)
    else:
        tile[pos: (pos-x):-1] = [1 for _ in range(x)] # white
        pos = pos - x + 1 

# 타일 색 개수
cnt_wh = tile.count(1)
cnt_bl = tile.count(-1)

print(cnt_wh,cnt_bl, sep = " " )