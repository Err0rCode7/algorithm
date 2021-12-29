import sys

input = sys.stdin.readline

n, k = map(int, input().rstrip().split())

dp = [[0] * (n + 1) for _ in range(3)]

def in_safe(x, y):
	return 0 <= x <= y and 0 <= y <= n


dp[0][0] = 1
dp[1][0] = 1
dp[1][1] = 1
for y in range(2, n + 1):
	for x in range(0, y + 1):
		result = 0
		ny = (y - 1) % 3
		if in_safe(x - 1, y - 1):
			result += dp[ny][x - 1]
		if in_safe(x, y - 1):
			result += dp[ny][x]
		result %= 1000000007
		dp[y % 3][x] = result

print(dp[n % 3][k])