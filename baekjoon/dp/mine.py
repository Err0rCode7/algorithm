import sys

def mine() :
	n, m = map(int, sys.stdin.readline().rstrip().split())
	grid = []
	dp = [[[] for x in range(20)] for y in range(20)]
	input_list = list(map(int, sys.stdin.readline().rstrip().split()))
	temp = []
	for i in range(len(input_list)) :
		temp.append(input_list[i])
		if ((i + 1) % m == 0) :
			grid.append(temp)
			temp = []

	for x in range(m) :
		for y in range(n) :
			if x == 0 :
				dp[y][x] = grid[y][x]
				continue
			if n == 1 :
				dp[y][x] = dp[y][x - 1] + grid[y][x]
			elif y + 1 < n and y > 0 :
				dp[y][x] = max(dp[y - 1][x - 1], dp[y][x - 1], dp[y + 1][x - 1]) + grid[y][x]
			elif y + 1 == n and y > 0 :
				dp[y][x] = max(dp[y - 1][x - 1], dp[y][x - 1]) + grid[y][x]
			elif y == 0 and y + 1 < n :
				dp[y][x] = max(dp[y][x - 1], dp[y + 1][x - 1]) + grid[y][x]
	max_value = 0
	for y in range(n) :
		if (max_value < dp[y][m - 1]) :
			max_value = dp[y][m - 1]
	result.append(max_value)

t = int(sys.stdin.readline().rstrip())
result = []
for i in range(t) :
	mine()
for value in result :
	print(value)
