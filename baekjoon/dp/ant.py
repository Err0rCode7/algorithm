import sys

# dp 점화식을 이용한 문제 (바텀 업)

# dp 리스트를 모두 0으로 설정한 후에 점화식을 시작하기 위한 앞에의 값 들을 초기화 해준다.
# 바로 이전의 쌓아올린 dp 값과 현재의 값 + 전전까지 쌓아올린 값을 비교하여 큰 값을 선택하여 dp의 값을 쌓아올린다.

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
