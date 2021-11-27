import sys, heapq

input = sys.stdin.readline

t = int(input())

for i in range(t) :
	n = int(input())
	board = [[-1] * (n + 2) for _ in range(n + 2)]
	for y in range(1, n + 1):
		line = list(map(int, input().rstrip().split()))

		for x in range(1, n + 1):
			board[y][x] = line[x - 1]

	queue = [(0, 1, 1)]
	costs = [[int(1e9)] * (n + 2) for _ in range(n + 2)]
	dx = [1, 0, -1, 0]
	dy = [0, 1, 0, -1]
	while queue :
		
		cost, x, y = heapq.heappop(queue)
		if costs[y][x] <= cost + board[y][x] :
			continue
		costs[y][x] = cost + board[y][x]
		for i in range(4):
			nx, ny = x + dx[i], y + dy[i]
			if board[ny][nx] == -1 :
				continue
			heapq.heappush(queue, (costs[y][x], nx, ny))

	print(costs[n][n])