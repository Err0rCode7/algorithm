from collections import deque
import sys

input = sys.stdin.readline

w, h = map(int, input().rstrip().split())

board = []
points = []

for y in range(h):
	line = input().rstrip()

	board.append(line)
	for x in range(w):
		if board[y][x] == 'C':
			points.append((x, y))

def bfs():
	x, y = points[0]
	tx, ty = points[1]
	visited = [[[-1] * 4 for _ in range(w)] for _ in range(h)]
	d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
	X, Y = 0, 1
	ANY = -2
	q = deque()
	q.append((x, y, ANY, cost))
	visited[y][x] = [0, 0, 0, 0]
	while q:
		x, y, v, cost = q.popleft()
		if x == tx and y == ty:
			print(visited[y][x])
			continue
		for i in range(4):
			nx, ny = x + d[i][X], y + d[i][Y]
			if 0 <= nx < w and 0 <= ny < h and board[ny][nx] != '*':
				if v == ANY or v == i:
					if v == ANY:
						v = i
					visited[ny][nx][i] = visited[y][x][v]
					q.appendleft((nx, ny, i))
				else :
					visited[ny][nx][i] = visited[y][x][v] + 1
					q.append((nx, ny, i))
	result = 1000000
	for i in range(4):
		if visited[ty][tx][i] != -1:
			result = min(result, visited[ty][tx][i])
	return result

print(bfs())
'''tc
7 8
.......
......C
......*
*****.*
....*..
....*..
.C..*..
.......

7 8
.......
......C
......*
*****.*
C...*..
....*..
*...*..
.......

7 8
.......
......C
......*
.****.*
C...*..
....*..
*...*..
.......

4 4
C.**
..**
....
...C
'''