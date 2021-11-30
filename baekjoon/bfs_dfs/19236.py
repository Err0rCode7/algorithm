from collections import deque
import sys
from copy import deepcopy

input = sys.stdin.readline

dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]
n = 4

fishes = [0] * (n * n + 1)

# fish, value
FISH = 0
VECTOR = 1
board = [[[-1] * 2 for _ in range(n + 2)] for _ in range(n + 2)]

for y in range(1, n + 1):
	line = list(map(int, input().strip().split()))

	for i in range(1, n + 1):
		x = (i - 1) * 2
		board[y][i][FISH] = line[x]
		board[y][i][VECTOR] = line[x + 1]
		# y, x, dead, vector
		fishes[line[x]] = [y, i, False, line[x + 1]]

def get_rotated_vector(vector):
	if vector >= 8:
		vector = 1
	else:
		vector += 1
	return vector

def move(fishes, _map):
	global n, dx, dy
	for fish in range(1, n * n + 1):
		y, x, dead, vector = fishes[fish]
		if not dead:
			move_one(_map, fishes, x, y, vector)

def move_one(_map, fishes, x, y, vector):
	global SHARK, dx, dy

	for i in range(8):
		nx, ny = x + dx[vector], y + dy[vector]
		if _map[ny][nx][0] >= 0 and _map[ny][nx][0] != SHARK:
			next_fish = _map[ny][nx][0]
			cur_fish = _map[y][x][0]
			if next_fish != 0:
				fishes[next_fish][0], fishes[next_fish][1] = y, x
			fishes[cur_fish][0], fishes[cur_fish][1] = ny, nx
			fishes[cur_fish][3] = vector
			_map[y][x][1] = vector
			_map[ny][nx], _map[y][x] = _map[y][x], _map[ny][nx]
			break
		vector = get_rotated_vector(vector)

def print_map_fish(_map, fishes):
	global n, SHARK
	print()
	for y in range(n):
		for x in range(n):
			if _map[y + 1][x + 1][0] == SHARK:
				print('🔴', end=' ')
			else:
				print(_map[y + 1][x + 1][0], end=' ')
		print()
		for x in range(n):
			print(get_arrow(_map[y + 1][x + 1][1]), end=' ')
		print()
	print()

def get_arrow(vector):
	arrow = [' ', '↑', '↖', '←', '↙', '↓', '↘', '→', '↗']
	return arrow[vector]

SHARK = 20
q = deque()
q.append((board, fishes, 1, 1, 0))
_max = -1

while q:
	_map, _fishes, y, x, cost = q.popleft()
	## shark move ##
	fish, vector = _map[y][x]
	_max = max(cost + fish, _max)
	# fish dead
	_fishes[fish][2] = True
	# shark move
	_map[y][x][0] = SHARK
	_map[y][x][1] = vector
	# fish move
	move(_fishes, _map)

	_map[y][x][0] = 0
	nx, ny = x, y
	while True:
		nx, ny = nx + dx[vector], ny + dy[vector]
		next_fish, next_vector = _map[ny][nx]
		if next_fish < 0:
			break
		if next_fish == 0:
			continue
		new_fishes = deepcopy(_fishes)
		new_map = deepcopy(_map)
		q.append((new_map, new_fishes, ny, nx, cost + fish))

print(_max)