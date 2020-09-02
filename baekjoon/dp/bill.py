import sys

def bill(n, m, dp, bills) :
	dp[0] = 0
	for i in range(n) :
		dp[bills[i]] = bills[i]
	for k in range(1, m + 1) :
		for i in range(n - 1, -1, -1) :
			if k >= bills[i] :
				dp[k] = min(dp[k], dp[k - bills[i]] + 1)
	if dp[m] == 10001 :
		print(-1)
	else :
		print(dp[m])




n, m = map(int, sys.stdin.readline().rstrip().split())
dp = [10001] * 101
bills = []
for i in range(n) :
	bills.append(int(sys.stdin.readline().rstrip()))
bills.sort()
bill(n, m, dp, bills)
