import sys

input = sys.stdin.readline

n = int(input().rstrip())

soldier = list(map(int, input().rstrip().split()))

dp = [0] * (n)

result = 0

for i in range(n):
	pre = 0
	for j in range(0, i):
		if soldier[j] > soldier[i]:
			pre = max(pre, dp[j])
	dp[i] = pre + 1
	result = max(result, dp[i])

print(n - result)