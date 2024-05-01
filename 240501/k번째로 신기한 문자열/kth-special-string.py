n,k,T = input().split()

n = int(n)
k = int(k)

words = list()
for i in range(n):
    word = input()
    if T in word:
        words.append(word)

words.sort()

print(words[k-1])