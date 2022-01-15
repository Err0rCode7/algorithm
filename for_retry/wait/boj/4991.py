from collections import deque
import sys

input = sys.stdin.readline

q = deque()
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

while True:
	w, h = map(int, input().rstrip().split())
	if w == 0 and h == 0:
		break
	board = []
	robot = []
	trash = []
	
	for y in range(h):
		line = input().rstrip()
		result = ""
		for x in range(w):
			if line[x] == 'o':
				robot.append((x, y))
			elif line[x] == '*':
				trash.append((x, y))
			if line[x] == 'x':
				result += 'x'
			else:
				result += '.'
		board.append(result)


	trash_visited = [False] * len(trash)
	INF = 20 * 20 * 20 * 20
	result = INF
	stop = False
	def bfs(x, y, tx, ty):
		visited = [[False for _ in range(w)] for _ in range(h)]
		q.append((x, y, 0))
		while q:
			x, y, cost = q.popleft()
			if x == tx and y == ty:
				q.clear()
				return cost
			for dx, dy in d:
				nx, ny = x + dx, y + dy
				if 0 <= nx < w and 0 <= ny < h and board[ny][nx] == '.' and visited[ny][nx] == False:
					visited[ny][nx] = True
					q.append((nx, ny, cost + 1))
		return -1

	def dfs(x, y, size, move):
		global result, stop
		if size == len(trash):
			result = min(result, move)
			return
		for i in range(len(trash)):
			if stop :
				return
			if trash_visited[i] == True:
				continue
			trash_visited[i] = True
			tx, ty = trash[i]
			add_move = bfs(x, y, tx, ty)
			if add_move == -1:
				stop = True
				result = INF
				return
			dfs(tx, ty, size + 1, move + add_move)
			trash_visited[i] = False

	dfs(robot[0][0], robot[0][1], 0, 0)

	if result == INF:
		print(-1)
	else :
		print(result)

