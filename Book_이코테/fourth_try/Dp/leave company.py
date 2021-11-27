import sys

input = sys.stdin.readline

n = int(input())

calendar = []

for i in range(n):
	t, p = map(int, input().rstrip().split())

	calendar.append((t, p))

dp = [0] * (n + 1)

for i in range(n - 1, -1, -1):
	t, p = calendar[i]
	if i + t > n :
		continue

	dp[i] = max(dp[i + t:]) + p

print(max(dp))
