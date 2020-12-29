# BOJ 18353

import sys

input = sys.stdin.readline

N = int(input().rstrip())

members = list(map(int, input().rstrip().split()))

dp = [1] * (N)
for i in range(N):
	for j in range(i):
		if (members[j] > members[i]):
			dp[i] = max(dp[j] + 1, dp[i])

print(N - max(dp))
