import sys

input = sys.stdin.readline

n, b = map(int, input().rstrip().split())

base = [[] for _ in range(n)]

for i in range(n):
	line = list(map(int, input().rstrip().split()))

	for j in line:
		base[i].append(j)

def multiple(a, b):
	result = [[0] * (n) for _ in range(n)]
	for y in range(n):
		for x in range(n):
			temp = 0
			for i in range(n):
				temp += a[y][i] * b[i][x]
			result[y][x] = temp % 1000
	return result

def _pow(target, b):

	if b == 1:
		return target
	half = _pow(target, b // 2)
	result = multiple(half, half)
	if b % 2 == 1:
		result = multiple(result, base)
	
	return result

answer = _pow(base, b)

for y in range(n):
	for x in range(n):
		print(answer[y][x] % 1000, end=' ')
	print()
