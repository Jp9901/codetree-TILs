n = int(input())

A = ord("A")
for i in range(n):
    for j in range(n):
        if i > j:
            print(" ", end = " ")
        else:
            print(chr(A), end = " ")
            A += 1  
            if A > ord('Z'):
                A = ord("A")

                


            

    print()