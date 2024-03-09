def print_hw(n):
    if n == 0:
        return
    
    print_hw(n-1)
    print("HelloWorld")

N = int(input())

print_hw(N)