import sys
# bottom up
input = sys.stdin.readline
t = int(input())
INF = int(1e10)
dp = [[False] * 500 for _ in range(500)]
for i in range(t):
	n = int(input())
	data = list(map(int, input().rstrip().split()))
	
	_sum = [0 for _ in range(n)]
	_sum[0] = data[0]
	for i in range(1, n):
		_sum[i] = _sum[i - 1] + data[i]

	for l in range(1, n):
		for s in range(n - l):
			e = s + l
			dp[s][e] = INF
			for mid in range(s, e):
				minus = 0 if s == 0 else _sum[s - 1]
				dp[s][e] = min(dp[s][e], dp[s][mid] + dp[mid + 1][e] + _sum[e] - minus)

	print(dp[0][n - 1])