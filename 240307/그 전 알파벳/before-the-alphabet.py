ch = input()

arr = list(
    chr(i) for i in range(ord('a'),ord('z')+1)
)

print(arr[arr.index(ch)-1])