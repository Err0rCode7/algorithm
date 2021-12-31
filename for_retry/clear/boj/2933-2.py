import sys

input = sys.stdin.readline

n, k = map(int,input().rstrip().split())
dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
	stuff, value = list(map(int, input().rstrip().split()))
	for j in range(k + 1):
		if j < stuff:
			dp[i][j] = max(dp[i - 1][j], dp[i][j])
		else:
			dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - stuff] + value)

print(dp[n][k])
