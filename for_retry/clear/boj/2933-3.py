from collections import deque
import sys

input = sys.stdin.readline
r, c = map(int, input().strip().split())

board = [[] for _ in range(r)]
for i in range(r):
	line = input().rstrip()
	for s in line:
		board[i].append(s)

n = int(input())

def delete(y, count):
	if count % 2 == 0: # left
		for x in range(c):
			if board[y][x] == 'x':
				board[y][x] = '.'
				return (True, x)
	else:
		for x in range(c - 1, -1, -1):
			if board[y][x] == 'x':
				board[y][x] = '.'
				return (True, x)
	return (False, 0)

def in_safe(x, y):
	return 0 <= x < c and 0 <= y < r

def bfs(visited, x, y, result):
	q = deque()
	q.append((x, y))
	visited[y][x] = True
	while q:
		x, y = q.popleft()
		if result != None:
			result.append((x, y))
		for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
			nx, ny = x + dx, y + dy
			if not in_safe(nx, ny) or visited[ny][nx] or board[ny][nx] == '.':
				continue
			visited[ny][nx] = True
			q.append((nx, ny))

heights = list(map(int, input().rstrip().split()))

for i in range(n):

	del_y = r - heights[i]
	result, del_x = delete(del_y, i)
	if result == False:
		continue
	visited = [[False] * c for _ in range(r)]
	for x in range(c):
		if board[r - 1][x] == 'x':
			bfs(visited, x, r-1, None)
	others_visited = [[False] * c for _ in range(r)]
	others = []
	for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
		nx, ny = del_x + dx, del_y + dy
		if not in_safe(nx, ny) or visited[ny][nx] or board[ny][nx] == '.':
			continue
		bfs(others_visited, nx, ny, others)
	count = 1
	while True and others:
		stop_flag = False
		for x, y in others:
			if not in_safe(x, y + count) or visited[y + count][x]:
				stop_flag = True
				break
		if stop_flag:
			if count - 1 > 0:
				for x, y in others:
					board[y][x] = '.'
				for x, y in others:
					board[y + count - 1][x] = 'x'
			break
		count += 1

for i in range(r):
	for j in range(c):
		print(board[i][j],end='')
	print()