from collections import deque
import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
	r, c = map(int, input().rstrip().split())
	board = [['.'] * (c + 2) for _ in range(r + 2)]
	prisoner = []
	for y in range(r):
		line = input().rstrip()
		for x in range(c):
			board[y + 1][x + 1] = line[x]
			if board[y + 1][x + 1] == '$':
				prisoner.append((x + 1, y + 1))
				board[y + 1][x + 1] = '.'
	
	def in_safe(x, y):
		return 0 <= x <= c + 1 and 0 <= y <= r + 1
	def bfs(x, y):
		q = deque()
		visited = [[-1] * (c + 2) for _ in range(r + 2)]
		q.append((x, y))
		visited[y][x] = 0
		while q:
			x, y = q.popleft()
			
			for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
				nx, ny = x + dx, y + dy
				if not in_safe(nx, ny) or visited[ny][nx] != -1 or board[ny][nx] == '*':
					continue
				if board[ny][nx] == '#':
					q.append((nx, ny))
					visited[ny][nx] = visited[y][x] + 1
				if board[ny][nx] == '.':
					q.appendleft((nx, ny))
					visited[ny][nx] = visited[y][x]
		return visited
	
	v1 = bfs(prisoner[0][0], prisoner[0][1])
	v2 = bfs(prisoner[1][0], prisoner[1][1])
	v3 = bfs(0, 0)
	result = int(1e10)
	for y in range(1, r + 1):
		for x in range(1, c + 1):
			if v1[y][x] == -1 or v2[y][x] == -1 or v3[y][x] == -1:
				continue
			minus = 2 if board[y][x] == '#' else 0
			result = min(result, v1[y][x] + v2[y][x] + v3[y][x] - minus)
	print(result)