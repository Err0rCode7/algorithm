from itertools import combinations
from collections import deque
import sys

input = sys.stdin.readline

N = int(input())

teachers = []
students = []
empty = []
board = []

for y in range(N):
	line = input().rstrip().split()

	for x in range(N):
		if line[x] == 'S':
			students.append((x, y))
		elif line[x] == 'T':
			teachers.append((x, y))
		else :
			empty.append((x, y))

	board.append(line)


def isPossibleForAllDirection(x, y, board):
	dx = [1, 0, -1, 0]
	dy = [0, 1, 0, -1]
	for i in range(4):
		tx, ty = x, y
		while (True):
			tx, ty = tx + dx[i], ty + dy[i]
			if not (0 <= tx < N and 0 <= ty < N) or board[ty][tx] == 'O':
				break
			if board[ty][tx] == 'S' :
				return False
	return True

def isPossibleForTeacher(board):

	for teacher in teachers :
		tx, ty = teacher
		if not isPossibleForAllDirection(tx, ty, board):
			return False

	return True

def process():
	global empty, board, teachers, N

	wall_combs = combinations(empty, 3)
	for wall_comb in wall_combs :
		for x, y in wall_comb:
			board[y][x] = 'O'
		if isPossibleForTeacher(board):
			return True
		for x, y in wall_comb:
			board[y][x] = 'X'
	return False

if process() :
	print("YES")
else :
	print("NO")