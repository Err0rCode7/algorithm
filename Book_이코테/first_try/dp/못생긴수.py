import sys

input = sys.stdin.readline

n = int(input().rstrip())

def solution_1(n):
	dp = [0] * 1001
	dp[1] = 1

	for i in range(1, 1001):
		if i * 2 >= 1001:
			break
		if dp[i] == 1:
			dp[i * 2] = 1
			if i * 3 < 1001:
				dp[i * 3] = 1
			if i * 5 < 1001:
				dp[i * 5] = 1

	count = 0
	for i in range(1001):
		if dp[i] == 1:
			count += 1
			if count == n:
				print(i)
				break

def solution_2(n):
	dp = [0] * n
	dp[0] = 1

	idx2, idx3, idx5 = 0, 0, 0
	next2, next3, next5 = 2, 3 ,5
	for i in range(1, n):
		dp[i] = min(next2, next3, next5)
		if dp[i] == next2:
			idx2 += 1
			next2 = dp[idx2] * 2
		if dp[i] == next3:
			idx3 += 1
			next3 = dp[idx3] * 3
		if dp[i] == next5:
			idx5 += 1
			next5 = dp[idx5] * 5
	print(dp[n - 1])

solution_2(n)
