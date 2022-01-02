P = 1000000007
def factorial(n):
	result = 1
	for i in range(2, n + 1):
		result = (result * i) % P
	return result
def pow(base, exp):
	if exp == 1:
		return base % P
	result = (pow(base, exp // 2) ** 2) % P
	if exp % 2 == 1:
		result = (result * base) % P
	return result

n, r = map(int, input().rstrip().split())

print((factorial(n) * pow(factorial(r) * factorial(n - r), P - 2)) % P)