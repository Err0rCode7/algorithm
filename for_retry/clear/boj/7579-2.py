import sys; input=sys.stdin.readline

n, m = map(int, input().rstrip().split())
byte = list(map(int, input().rstrip().split()))
cost = list(map(int, input().rstrip().split()))
byte.insert(0, 0)
cost.insert(0, 0)
dp = [[0] * (100 * 100 + 1) for _ in range(102)] # n * cost

for i in range(1, n + 1):
	for j in range(0, 100 * 100 + 1):
		if j >= cost[i]:
			dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost[i]] + byte[i])
		else :
			dp[i][j] = dp[i - 1][j]

for i in range(100 * 100 + 1):
	if dp[n][i] >= m:
		print(i)
		break