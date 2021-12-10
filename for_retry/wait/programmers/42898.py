from collections import deque

def solution(m, n, puddles):
	dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
	board = [[0] * (m + 2) for _ in range(n + 2)]

	for puddle in puddles:
		x, y = puddle
		board[y][x] = -1
	dp[1][1] = 1
	for y in range(1, n + 1):
		for x in range(1, m + 1):
			if board[y][x] != 0 :
				continue
			count = 0
			if board[y - 1][x] == 0:
				count += dp[y - 1][x]
			if board[y][x - 1] == 0:
				count += dp[y][x - 1]
			dp[y][x] += count

	return dp[n][m] % 1000000007

def solution_(m, n, puddles):
	# dp = cost, count
	int(1e9), 0
	dp = [[[int(1e9), 0] for _ in range(m + 1)] for _ in range(n + 1)]
	board = [[0] * (m + 2) for _ in range(n + 2)]

	for i in range(m + 2):
		board[0][i] = -1
		board[n + 1][i] = -1
	for i in range(n + 2):
		board[i][0] = -1
		board[i][m + 1] = -1
	for puddle in puddles:
		x, y = puddle
		board[y][x] = -1
	q = deque()
	dx = [1, 0]
	dy = [0, 1]
	# bfs, visited dp
	q.append((1, 1, 0))
	COST = 0
	VISIT_COUNT = 1
	while q :
		x, y, cost = q.popleft()
		if dp[y][x][VISIT_COUNT] > 0 :
			if dp[y][x][COST] < cost :
				continue
			elif dp[y][x][COST] == cost :
				dp[y][x][VISIT_COUNT] += 1
			elif dp[y][x][COST] > cost:
				dp[y][x][COST] = cost
				dp[y][x][VISIT_COUNT] = 1
		else :
			dp[y][x][COST] = cost
			dp[y][x][VISIT_COUNT] += 1
		for i in range(2):
			nx, ny = x + dx[i], y + dy[i]
			if board[ny][nx] != 0:
				continue
			q.append((nx, ny, cost + 1))

	answer = dp[n][m][VISIT_COUNT]
	return answer

print(solution(4, 3, [[2, 2]]))