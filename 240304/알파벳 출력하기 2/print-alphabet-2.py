n = int(input())

A = ord("A")
for i in range(n):
    for j in range(n):
        if i > j:
            print(" ", end = " ")
        else:
            print(chr(A), end = " ")
            if chr(A) == 'Z':
                A = ord("A")
            else:
                A += 1


            

    print()