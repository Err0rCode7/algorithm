def solution(m, n, puddles):

	dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

	for x, y in puddles:
		dp[y][x] = -1

	dp[1][1] = 1
	for y in range(1, n + 1):
		for x in range(1, m + 1):
			if dp[y][x] == -1:
				continue
			up = dp[y - 1][x]
			left = dp[y][x - 1]
			if up > 0:
				dp[y][x] += up % 1000000007
			if left > 0 :
				dp[y][x] += left % 1000000007
			dp[y][x] = dp[y][x] % 1000000007

	return dp[n][m]

print(solution(4, 3, [[2, 2]]))