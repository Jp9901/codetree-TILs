n = int(input())

# 별 출력 함수
def star_print(n):
    if n < 1:
        return

    print('* '*n)
    star_print(n-1)
    print('* '*n)

star_print(n)