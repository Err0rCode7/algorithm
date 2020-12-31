# BOJ 11404

import sys

input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())

dp = [[int(1e9) for _ in range(n + 1)] for _ in range(n + 1)]

for a in range(1, n + 1):
	for b in range(1, n + 1):
		if a == b:
			dp[a][b] = 0

for i in range(m):
	a, b, c = map(int, input().rstrip().split())
	dp[a][b] = min(dp[a][b], c)

for i in range(1, n + 1):
	for a in range(1, n + 1):
		for b in range(1, n + 1):
			dp[a][b] = min(dp[a][b], dp[a][i] + dp[i][b])

for a in range(1, n + 1):
	for b in range(1, n + 1):
		if dp[a][b] != int(1e9):
			print(dp[a][b], end='')
		else :
			print(0, end='')
		if b < n:
			print(' ',end='')
	print()
