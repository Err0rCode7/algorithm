import sys

input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()

n = len(str2)
m = len(str1)
dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
	dp[i][0] = dp[i - 1][0] + 1
for i in range(1, m + 1):
	dp[0][i] = dp[i - 1][0] + 1

for i in range(1, n + 1):
	for j in range(1, m + 1):
		if str2[i - 1] == str1[j - 1]:
			dp[i][j] = dp[i - 1][j - 1]
		else :
			dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1

print(dp[n][m])
