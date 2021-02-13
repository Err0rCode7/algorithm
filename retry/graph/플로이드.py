import sys

input = sys.stdin.readline

n = int(input()) # 도시의 수
m = int(input()) # 버스의 수

INF = 1e9

dp = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(m):
	start, end, cost = map(int, input().rstrip().split())

	if cost < dp[start][end]:
		dp[start][end] = cost

for a in range(1, n + 1):
	for b in range(1, n + 1):
		if a == b:
			dp[a][b] = 0

for k in range(1, n + 1):
	for i in range(1, n + 1):
		for j in range(1, n + 1):
			dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

for i in range(1, n + 1):
	for j in range(1, n + 1):
		if dp[i][j] == INF:
			print(0, end=" ")
		else :
			print(dp[i][j], end=" ")
	print()