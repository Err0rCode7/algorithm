import sys

input = sys.stdin.readline

n = int(input())

triangle = [[0] * (n + 2) for _ in range(n + 2)]
dp = [[0] * (n + 2) for _ in range(n + 2)]

for y in range(n):

	line = list(map(int, input().rstrip().split()))

	for x in range(0, len(line)):
		triangle[y + 1][x + 1] = line[x]

for y in range(1, n + 1):
	for x in range(1, y + 1):
		dp[y][x] = max(dp[y - 1][x], dp[y - 1][x - 1]) + triangle[y][x]

print(max(dp[n]))