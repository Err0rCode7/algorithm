from collections import deque
import sys

input = sys.stdin.readline
r, c = map(int, input().rstrip().split())

board = [['B'] * (c + 2) for _ in range(r + 2)]
water = deque()
swans = []

for y in range(1, r + 1):
	line = input().rstrip()
	for x in range(1, c + 1):
		board[y][x] = line[x - 1]
		if line[x - 1] == '.':
			water.append((x, y))
		elif line[x - 1] == 'L':
			swans.append((x, y))

dir_v = [(1, 0), (0, 1), (-1, 0), (0, -1)]
def spread(board, x, y, water):
	for dx, dy in dir_v:
		nx, ny = x + dx, y + dy
		if board[ny][nx] == 'X':
			board[ny][nx] = '.'
			water.append((nx, ny))

def ice_break(water, board):

	n = len(water)
	for i in range(n):
		x, y = water.popleft()

		spread(board, x, y, water)

def dfs(start, end, board, visited):
	x, y = start
	tx, ty = end

	if x == tx and y == ty:
		return True
	visited[y][x] = True
	for dx, dy in dir_v:
		nx, ny = x + dx, y + dy
		if board[ny][nx] not in ".L" or visited[ny][nx] == True:
			continue
		if dfs((nx, ny), end, board, visited):
			return True
	visited[y][x] = False
	return False

def try_contact(swans, board):
	visited = [[False] * (c + 2) for _ in range(r + 2)]
	return dfs(swans[0], swans[1], board, visited)

def count():
	count = 0
	while True:
		count += 1
		ice_break(water, board)
		if try_contact(swans, board):
			break
	return count

if try_contact(swans, board) :
	print(0)
else:
	print(count())

