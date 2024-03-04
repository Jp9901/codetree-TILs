# 변수 선언 및 입력
n = int(input())
	
# n칸의 정사각형에서 i, j가 조건에 맞으면 *을 출력합니다.
for i in range(n):
	for j in range(n):
		if i > j or i == 0 or j == n - 1:
			print("* ", end="")
		else:
			print("  ", end="")
	print()