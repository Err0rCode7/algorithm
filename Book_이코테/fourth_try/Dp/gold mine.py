import sys

input = sys.stdin.readline

t = int(input())
def solution(n, m):
	line = list(map(int, input().rstrip().split()))

	mine = [[0] * (m + 2) for _ in range(n + 2)]

	for i in range(len(line)):
		mine[i // m + 1][i % m + 1] = line[i]
	dp = [[0] * (m + 2) for _ in range(n + 2)]

	for x in range(1, m + 1):
		for y in range(1, n + 1):
			dp[y][x] = max(dp[y - 1][x - 1], dp[y][x - 1], dp[y + 1][x - 1]) + mine[y][x]
	result = -1
	for i in range(1, n + 1):
		result = max(result, dp[i][m])
	return result

for i in range(t):

	n, m = map(int, input().rstrip().split())
	print(solution(n, m))
