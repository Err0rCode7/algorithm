import sys

# 1을 만들기 위한 5, 3, 2의 최소 갯수를 구하는 문제

def make_one(x) :
	dp = [0] * 101

	for i in range(2, x + 1) :
		value = dp[i - 1] + 1
		if (i % 5 == 0) :
			value = min(value, dp[i // 5] + 1)
		if (i % 3 == 0) :
			value = min(value, dp[i // 3] + 1)
		if (i % 2 == 0) :
			value = min(value, dp[i // 2] + 1)
		dp[i] = value
	print(dp[x])

x = int(sys.stdin.readline().rstrip())
make_one(x)
