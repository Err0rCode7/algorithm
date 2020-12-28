# BOJ 1932

import sys

input = sys.stdin.readline

n = int(input().rstrip())

board = []
for y in range(n):
	line = list(map(int, input().rstrip().split()))
	for x in range(len(line), n):
		line.append(0)
	board.append(line)

dp = [[0 for _ in range(n)] for _ in range(n)]
for y in range(n):
	for x in range(n):
		if y == 0:
			dp[y][x] = board[y][x]
		elif x > 0 :
			dp[y][x] = max(dp[y - 1][x], dp[y - 1][x - 1]) + board[y][x]
		elif x == 0:
			dp[y][x] = dp[y - 1][x] + board[y][x]

result = 0
for x in range(n):
	result = max(result, dp[n - 1][x])
print(result)
