import sys; input = sys.stdin.readline

n = int(input().rstrip())

data = []

for i in range(n):
	r, c = map(int, input().rstrip().split())
	data.append((r, c))

dp = [[0] * n for _ in range(n)]

INF = 2**31

for l in range(1, n):
	for s in range(n - l):
		e = s + l
		dp[s][e] = INF
		for mid in range(s, e):
			dp[s][e] = min(dp[s][e], dp[s][mid] + dp[mid + 1][e] + data[s][0] * data[mid][1] * data[e][1])
print(dp[0][n - 1])