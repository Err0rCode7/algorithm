import sys, copy
from collections import deque
from itertools import combinations

input = sys.stdin.readline
N, M = map(int, input().strip().split())

board = []
virus = []
empty = []
for y in range(0, N):
	line_list = list(map(int, input().strip().split()))
	board.append(line_list)
	for x, value in enumerate(line_list):
		if value == 0:
			empty.append((x, y))
		elif value == 2:
			virus.append((x, y))

combs = combinations(empty, 3)
queue = deque()

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

result = 1e9

for comb in combs :
	n_board = copy.deepcopy(board)
	for x, y in comb :
		n_board[y][x] = 1
	queue = deque()
	for x, y in virus:
		queue.append((x, y))
	count = 0
	while queue :
		x, y = queue.popleft()
		if n_board[y][x] == 0:
			count += 1
			n_board[y][x] = 2
		for i in range(4) :
			n_x, n_y = dx[i] + x, dy[i] + y
			if not (0 <= n_x < M and 0 <= n_y < N):
				continue
			if n_board[n_y][n_x] == 0:
				queue.append((n_x, n_y))
	result = min(result, count)
print(len(empty) - 3 - result)
