import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
n = int(input())

board = []
teachers = []
for i in range(n) :
	row = list(input().split())
	board.append(row)
	for j in range(len(row)) :
		if row[j] == "T" :
			teachers.append((j,i))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def is_valid(teachers, board) :

	for x, y in teachers :
		for i in range(4):
			nx, ny = x, y
			while True :
				nx, ny = nx + dx[i], ny + dy[i]
				if nx < 0 or ny < 0 or nx >= n or ny >= n or \
					board[ny][nx] == "O":
					break
				if board[ny][nx] == "S" :
					return False
	return True

def dfs(x, y, count) :
	global teachers, board, n
	if count == 3 :
		if is_valid(teachers, board):
			return True
		else :
			return False
	else :
		for i in range(y, n):
			for j in range(n):
				if board[i][j] != "X" :
					continue
				board[i][j] = "O"
				if dfs(j, i, count + 1) :
					return True
				board[i][j] = "X"

if dfs(0, 0, 0) :
	print("YES")
else :
	print("NO")
