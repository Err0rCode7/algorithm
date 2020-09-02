import sys

def ant(n, warehouse) :
	dp = [0] * 101
	dp[1] = warehouse[0]
	dp[2] = max(warehouse[1], warehouse[0])
	for i in range(2, n) :
		value1 = warehouse[i] + dp[i + 1 - 2]
		value2 = dp[i + 1 - 1]
		dp[i + 1] = max(value1, value2)
	print(dp[n])

n = int(sys.stdin.readline().rstrip())
warehouse = list(map(int, sys.stdin.readline().rstrip().split()))
ant(n, warehouse)
