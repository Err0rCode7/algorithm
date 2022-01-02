import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int, input().rstrip().split())

def find_parent(parent, x):
	if parent[x] != x:
		parent[x] = find_parent(parent, parent[x])
	return parent[x]

parent = [x for x in range((c + 2) * (r + 2))]

# Block : default
board = [['B' for x in range(c + 2)] for y in range(r + 2)]
swans = []

for y in range(1, r + 1):
	line = input().rstrip()
	for x in range(1, c + 1):
		board[y][x] = line[x - 1]
		if board[y][x] == 'L':
			swans.append((x, y))

def union_parent(a, b):
	a = find_parent(parent, a)
	b = find_parent(parent, b)
	if a < b:
		parent[b] = a
	else:
		parent[a] = b

def union_4dir(board, x, y):
	for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
		nx, ny = x + dx, y + dy
		if board[ny][nx] == '.' or board[ny][nx] == 'L':
			union_parent(ny * (c + 2) + nx, y * (c + 2) + x)

def break_down_ice(board, break_pos_list):
	result = set()
	while len(break_pos_list) > 0:
		x, y = break_pos_list.pop()
		for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
			nx, ny = x + dx, y + dy
			if board[ny][nx] == 'X':
				board[ny][nx] = '.'
				union_parent(ny * (c + 2) + nx, y * (c + 2) + x)
				union_4dir(board, nx, ny)
				result.add((nx, ny))
	return result

def bfs(board, visited, q, result):
	while q:
		x, y, start = q.popleft()
		if visited[y][x]:
			continue
		visited[y][x] = True
		union_parent(y * (c + 2) + x, start)
		for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
			nx, ny = x + dx, y + dy
			if board[ny][nx] == 'L' or board[ny][nx] == '.':
				q.append((nx, ny, y * (c + 2) + x))
			elif board[ny][nx] == 'X':
				result.add((x, y))

def set_graph(board):
	q = deque()
	result = set()
	visited = [[False] * (c + 2) for _ in range(r + 2)]
	for i in range(1, r + 1):
		for j in range(1, c + 1):
			if board[i][j] == 'L' or board[i][j] == '.':
				if not visited[i][j]:
					q.append((j, i, i * (c + 2) + j))
					bfs(board, visited, q, result)
	return result

def check_swan():
	x1, y1 = swans[0]
	x2, y2 = swans[1]
	if find_parent(parent, y2 * (c + 2) + x2) == find_parent(parent, y1 * (c + 2) + x1):
		return True
	return False

def solve():

	for_break = set_graph(board)
	result = 0
	if check_swan():
		return result
	
	while True:
		result += 1
		for_break = break_down_ice(board, for_break)
		if check_swan():
			break
	return result

print(solve())