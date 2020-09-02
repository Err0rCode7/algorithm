import sys

def spot_soldier() :
	dp = [1] * (n)

	for x in range(1, n) :
		for i in range(0, x) :
			if (powers[i] > powers[x]) :
				dp[x] = max(dp[x], dp[i] + 1)
	print(n - max(dp))
n = int(sys.stdin.readline().rstrip())
powers = list(map(int, sys.stdin.readline().rstrip().split()))
spot_soldier()
