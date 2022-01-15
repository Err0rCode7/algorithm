import sys
# tob down
input = sys.stdin.readline
t = int(input())
INF = 10001
dp = [[INF] * 500 for _ in range(500)]
for i in range(t):
	n = int(input())
	data = list(map(int, input().rstrip().split()))
	def initDp():
		for i in range(n):
			for j in range(n):
				dp[i][j] = 0
	
	_sum = [0 for _ in range(n + 1)]
	_sum[0] = data[0]
	for i in range(1, n):
		_sum[i] = _sum[i - 1] + data[i]

	def getMinimumBetweenPoints(l, r):
		if l == r or dp[l][r] > 0:
			return dp[l][r]
		elif l + 1 == r:
			dp[l][r] = data[l] + data[r]
			return dp[l][r]
		result = int(1e10)
		for mid in range(l, r):
			left = getMinimumBetweenPoints(l, mid)
			right = getMinimumBetweenPoints(mid + 1, r)
			# print(l, r, mid, left, right)
			new = left + right + _sum[r]
			if l > 0:
				new -= _sum[l - 1]

			result = min(result, new)
		dp[l][r] = result
		return dp[l][r]
	initDp()
	getMinimumBetweenPoints(0, n - 1)
	print(dp[0][n - 1])