import sys

# m의 값에 돈을 만들기 위한 지폐 수를 구하는 문제
# dp를 INFINIT 값으로 초기화하고 각 지폐에 해당하는 값을 1로 초기화 해준다. (바텀 업 방식으로 구하는 문제)
# dp 값에는 지폐의 수가 저장되고 아랫단계에서부터 최소 값이 되는 dp를 쌓아올려 m이 되는 순간에 최소 지폐 수 를 구한다.

# 가장 큰 지폐부터 시작하여 지폐 1장의 값을 뺀 인덱스에 해당하는 dp값과 현재 dp값을 비교하여 최소 값을 찾아낸다.

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
