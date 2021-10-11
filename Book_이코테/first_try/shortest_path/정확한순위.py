import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

dp = [[M for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(M):
	a, b = map(int, input().rstrip().split())
	dp[a][b] = 1

for a in range(1, N + 1):
	for b in range(1, N + 1):
		if a == b :
			dp[a][b] = 0

for k in range(1, N + 1):
	for a in range(1, N + 1):
		for b in range(1, N + 1):
			dp[a][b] = min(dp[a][b], dp[a][k] + dp[k][b])

result = 0
for i in range(1, N + 1):
	count = 0
	for j in range(1, N + 1):
		if dp[i][j] != M or dp[j][i] != M:
			count += 1
	if count == N:
		result += 1

print(result)
