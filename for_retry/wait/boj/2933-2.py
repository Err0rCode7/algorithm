from collections import deque
import sys

input = sys.stdin.readline
r, c = map(int, input().rstrip().split())

board = [['B' for _ in range(c + 2)] for _ in range(r + 2)]
_dir = [(1,0), (0,1), (-1,0), (0,-1)]
for y in range(1, r + 1):
	line = input().rstrip()
	for x in range(1, c + 1):
		board[y][x] = line[x - 1]

n = int(input().rstrip())
heights = list(map(int, input().rstrip().split()))

def bfs_visit(visited, x, y, q):
	q.append((x, y))
	visited[y][x] = True
	while q :
		x, y = q.popleft()
		for dx, dy in _dir:
			nx, ny = x + dx, y + dy
			if board[ny][nx] == 'x' and visited[ny][nx] == False:
				visited[ny][nx] = True
				q.append((nx, ny))

def check_connection(visited, q):
	y = r
	for x in range(1, c + 1):
		if board[y][x] == 'x' and not visited[y][x]:
			bfs_visit(visited, x, y, q)

def delete_one(height, src, dest):
	offset = 1 if dest - src >= 0 else -1
	y = height
	for x in range(src, dest, offset):
		if board[y][x] == 'B':
			break
		elif board[y][x] == 'x':
			board[y][x] = '.'
			break
	return (x, y)

def get_direction(height, offset):
	result_height, src, dest = None, None, None
	if offset % 2 == 0: # left to right
		result_height = r - height + 1
		src = 1
		dest = c + 1
	else:
		result_height = r - height + 1
		src = c
		dest = 0
	return (result_height, src, dest)

def get_offset(move_list, visited):
	offset = 1
	while True and move_list:
		flag = False
		for x, y in move_list:
			if board[y + offset][x] == 'B' or visited[y + offset][x]:
				flag = True
				break
		if flag:
			return offset - 1
		offset +=1
	return 0

def do_gravity(result, offset):
	for x, y in result:
		y += offset
		board[y][x] = 'x'

def get_min(visited, x, y):
	result = r - y
	for height in range(y, r + 1):
		if visited[height + 1][x] or board[height + 1][x] == 'B':
			result = height - y
			break
	return result

def get_bfs_pos(x, y, q):
	q.append((x, y))
	result = []
	visited = [[False for _ in range(c + 2) ] for _ in range(r + 2)]
	move_list = []
	board[y][x] = '.'
	while q :
		x, y = q.popleft()
		result.append((x, y))
		if board[y + 1][x] == '.' and not visited[y + 1][x]:
			move_list.append((x, y))
		for dx, dy in _dir:
			nx, ny = x + dx, y + dy
			if board[ny][nx] == 'x' and not visited[ny][nx]:
				visited[ny][nx] = True
				board[ny][nx] = '.'
				q.append((nx, ny))
	return (result, move_list)

def apply_gravity(visited, x, y, q):
	result, move_list = [], []
	for dx, dy in _dir:
		nx, ny = x + dx, y + dy
		if board[ny][nx] == 'x' and not visited[ny][nx]:
			result, move_list = get_bfs_pos(nx, ny, q)
	offset = get_offset(move_list, visited)
	do_gravity(result, offset)

def print_result(board):
	for y in range(1, r + 1):
		for x in range(1, c + 1):
			print(board[y][x], end=' ')
		print()

def solve(height, i, q):
	visited = [[False for _ in range(c + 2) ] for _ in range(r + 2)]
	start_height, src, dest = get_direction(height, i)
	x, y = delete_one(start_height, src, dest)
	check_connection(visited, q)
	apply_gravity(visited, x, y, q)

def solution():
	q = deque()
	for i in range(n):
		height = heights[i]
		solve(height, i, q)
	print_result(board)

solution()