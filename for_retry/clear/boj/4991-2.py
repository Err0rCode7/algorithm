from collections import deque
import sys; input = sys.stdin.readline

while True:
	w, h = map(int, input().rstrip().split())
	if w == 0 and h == 0 :
		break

	board = []
	points = []
	robot = ()
	for i in range(h):
		line = input().rstrip()
		board.append(line)
		for j in range(w):
			if line[j] == 'o':
				robot = (j, i)
			elif line[j] == '*':
				points.append((j, i))
	INF = w * h + 1
	def bfs(x, y):
		visited = [[INF] * w for _ in range(h)]
		q = deque([(x, y)])
		visited[y][x] = 0
		count = 0
		while q :
			x, y = q.popleft()
			if board[y][x] == '*':
				count += 1
			for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
				nx, ny = x + dx, y + dy
				if 0 <= nx < w and 0 <= ny < h and board[ny][nx] != 'x'\
					and visited[ny][nx] == INF:
					q.append((nx, ny))
					visited[ny][nx] = visited[y][x] + 1
		return (visited, count)
	
	result = bfs(robot[0], robot[1])
	if result[1] != len(points):
		print(-1)
		continue
	dist = [result[0]]
	for x, y in points:
		dist.append(bfs(x, y)[0])

	visited = [False] * (1 + len(points))
	visited[0] = True
	result = w * h + 1
	def dfs(cur, cost, size, visited):
		global result
		if size == len(points):
			result = min(result, cost)
		
		for i in range(1, len(points) + 1):
			if visited[i] :
				continue
			tx, ty = points[i - 1]
			add = dist[cur][ty][tx]
			visited[i] = True
			dfs(i, cost + add, size + 1, visited)
			visited[i] = False
	
	dfs(0, 0, 0, visited)
	print(result)
