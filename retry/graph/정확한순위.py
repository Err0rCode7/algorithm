import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

INF = 1e6
dp = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(m):
	a, b = map(int, input().rstrip().split())
	dp[a][b] = 1

for i in range(1, n + 1):
	for j in range(1, n + 1):
		if i == j:
			dp[i][j] = 0

for i in range(1, n + 1):
	for j in range(1, n + 1):
		for k in range(1, n + 1):
			dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

result = 0

for i in range(1, n + 1):
	count = 0
	for j in range(1, n + 1):
		if dp[i][j] != INF or dp[j][i] != INF:
			count += 1
	if count == n :
		result += 1

print(result)