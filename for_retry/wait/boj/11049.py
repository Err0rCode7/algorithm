import sys

input = sys.stdin.readline
n = int(input())

INF = 2147483647
dp = [[0] * n for _ in range(n)]

cost = []

for i in range(n):
	l, r = map(int, input().rstrip().split())
	cost.append((l, r))

def getMinRange(s, e):
	if s == e or dp[s][e] != 0:
		return dp[s][e]

	if s + 1 == e:
		dp[s][e] = cost[s][0] * cost[s][1] * cost[e][1]
		return dp[s][e]
	
	result = INF
	for mid in range(s, e):
		left = getMinRange(s, mid)
		right = getMinRange(mid + 1, e)
		result = min(result, left + right + cost[s][0] * cost[mid][1] * cost[e][1])
	dp[s][e] = result
	return dp[s][e]

print(getMinRange(0, n - 1))

'''
5
5 3
3 2
2 6
6 8
8 2
'''