from itertools import combinations as cb
import copy
from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

board = []
virus = []
safezone = []
for i in range(N):
	line = list(map(int, input().rstrip().split()))

	for j, num in enumerate(line):
		if num == 2:
			virus.append((i, j))
		elif num == 0:
			safezone.append((i, j))
	board.append(line)

comb_iter = cb(safezone, 3)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
result = 0
for comb in comb_iter:
	new_board = copy.deepcopy(board)
	new_virus = deque(virus)
	for y, x in comb:
		new_board[y][x] = 1
	while new_virus:
		y, x = new_virus.popleft()
		for i in range(4):
			ny, nx = y + dy[i], x + dx[i]
			if (ny >= N or ny < 0 or nx >= M or nx < 0):
				continue
			elif (new_board[ny][nx] == 0):
				new_board[ny][nx] = 2
				new_virus.append((ny, nx))
	new_result = 0
	for y in range(N):
		for x in range(M):
			if new_board[y][x] == 0:
				new_result += 1
	result = max(result, new_result)

print(result)
