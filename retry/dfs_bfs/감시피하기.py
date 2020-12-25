from itertools import combinations as cb
import sys

input = sys.stdin.readline

N = int(input().rstrip())

teachers = []
students = []
space = []
board = []
for i in range(N):
	line = list(input().rstrip().split())
	for j in range(N):
		if line[j] == 'T':
			teachers.append((i, j))
		elif line[j] == 'S':
			students.append((i, j))
		else:
			space.append((i, j))
	board.append(line)

comb_iter = cb(space, 3)
def check_board():
	global teachers, board

	dx = [1, 0, -1, 0]
	dy = [0, 1, 0, -1]
	for y, x in teachers:
		for i in range(4):
			ny, nx = y + dy[i], x + dx[i]
			while (0 <= ny < N) and (0 <= nx < N):
				if board[ny][nx] == "S":
					return (False)
				elif board[ny][nx] == 'O':
					break
				ny, nx = ny + dy[i], nx + dx[i]
	return (True)

flag = 0
for comb in comb_iter:

	for y, x in comb:
		board[y][x] = 'O'

	if check_board():
		flag = 1

	for y, x in comb:
		board[y][x] = 'X'

if flag:
	print("YES")
else :
	print("NO")
