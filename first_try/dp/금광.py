import sys

input = sys.stdin.readline

T = int(input().rstrip())

for i in range(T):

	n, m = map(int, input().rstrip().split())
	line = list(map(int, input().rstrip().split()))

	lines = []
	dp = [[0 for _ in range(m)] for _ in range(n)]
	for i in range(0, n * m, m):
		lines.append(line[i:i+m])

	for y in range(n):
		dp[y][0] = lines[y][0]

	for x in range(m):
		for y in range(n):
			if x == 0:
				dp[y][0] = lines[y][0]
			elif y == 0:
				dp[y][x] = max(dp[y][x - 1], dp[y + 1][x - 1]) + lines[y][x]
			elif y == n - 1:
				dp[y][x] = max(dp[y][x - 1], dp[y - 1][x - 1]) + lines[y][x]
			else :
				dp[y][x] = max(dp[y + 1][x - 1], dp[y][x - 1], dp[y - 1][x - 1]) + lines[y][x]
	result = 0
	for y in range(n):
		result = max(result, dp[y][m - 1])
	print(result)
