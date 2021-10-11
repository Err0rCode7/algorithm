# BOJ 14501

import sys
import copy

input = sys.stdin.readline

N = int(input().rstrip())

t = []
p = []

for i in range(N):
	day, money = map(int, input().rstrip().split())

	t.append(day)
	p.append(money)

dp = [0] * (N + 1)
max_value = 0

for i in range(N - 1, -1, -1):
	time = t[i] + i
	if time <= N:
		dp[i] = max(p[i] + dp[time], max_value)
		max_value = dp[i]
	else:
		dp[i] = max_value
print(max_value)
