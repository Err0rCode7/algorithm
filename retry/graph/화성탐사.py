import heapq
import sys

input = sys.stdin.readline

t = int(input().rstrip())
for i in range(t):
	n = int(input().rstrip())
	_path = []
	for j in range(n):
		line = list(map(int, input().rstrip().split()))
		_path.append(line)
	visited = [[False] * n for _ in range(n)]
	dp = [[int(1e10)] * n for _ in range(n)]
	dx = [1, 0, -1, 0]
	dy = [0, 1, 0, -1]

	q = []
	heapq.heappush(q, (_path[0][0], 0, 0))
	while q:
		cost, y, x = heapq.heappop(q)
		if visited[y][x]:
			continue
		visited[y][x] = True
		dp[y][x] = cost
		if y == n - 1 and x == n - 1:
			break
		for i in range(4):
			new_y, new_x = y + dy[i], x + dx[i]
			if new_x < 0 or new_x >= n or new_y < 0 or new_y >= n :
				continue
			heapq.heappush(q, (cost + _path[new_y][new_x], new_y, new_x))
	print(dp[n - 1][n - 1])
