import sys, heapq
from collections import deque

input = sys.stdin.readline

T = int(input().rstrip())

# bfs??
'''
for t in range(T):
	N = int(input().rstrip())

	INF = int(1e9)
	board = []
	for i in range(N):
		line = list(map(int, input().rstrip().split()))
		board.append(line)
	dp = [[INF for _ in range(N)] for _ in range(N)]
	queue = deque()
	queue.append((0, 0, 0))
	dx = [1, 0, -1, 0]
	dy = [0, 1, 0, -1]
	while queue:
		y, x, cost = queue.popleft()
		dp[y][x] = min(dp[y][x], cost + board[y][x])
		for i in range(4):
			ny, nx = y + dy[i], x + dx[i]
			if ny >= N or ny < 0 or nx >= N or nx < 0:
				continue
			if dp[y][x] + board[ny][nx] < dp[ny][nx]:
				queue.append((ny, nx, dp[y][x]))
	print(dp[N - 1][N - 1])
'''

# 다익스트라
for t in range(T):
	N = int(input().rstrip())

	INF = int(1e9)
	board = []
	for i in range(N):
		line = list(map(int, input().rstrip().split()))
		board.append(line)
	dp = [[INF for _ in range(N)] for _ in range(N)]
	heap = [(board[0][0], 0, 0)]
	dx = [1, 0, -1, 0]
	dy = [0, 1, 0, -1]
	while heap:
		cost, y, x = heapq.heappop(heap)
		if cost > board[y][x]:
			continue
		for i in range(4):
			ny, nx = y + dy[i], x + dx[i]
			if ny >= N or ny < 0 or nx >= N or nx < 0:
				continue
			new_cost = cost + board[ny][nx]
			if new_cost < dp[ny][nx]:
				dp[ny][nx] = new_cost
				heapq.heappush(heap, (new_cost, ny, nx))
	print(dp[N - 1][N - 1])
