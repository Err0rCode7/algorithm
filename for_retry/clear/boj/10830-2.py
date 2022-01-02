n, b = map(int, input().rstrip().split())

base = []
P = 1000
def convertToIntWithMod(c):
	return int(c) % P

for i in range(n):
	line = list(map(convertToIntWithMod, input().rstrip().split()))
	base.append(line)

def multiply(a, b):
	result = [[0] * n for _ in range(n)]
	for y in range(n):
		for x in range(n):
			for i in range(n):
				result[y][x] = (result[y][x] + a[y][i] * b[i][x]) % 1000
	return result

def getMultiplied(base, b):
	if b == 1:
		return base
	half = getMultiplied(base, b // 2)
	result = multiply(half, half)
	if b % 2 == 1:
		result = multiply(result, base)
	return result

def print_result(result):
	for i in range(n):
		for j in range(n):
			print(result[i][j], end=' ')
		print()

answer = getMultiplied(base, b)
print_result(answer)