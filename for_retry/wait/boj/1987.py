import sys

input = sys.stdin.readline
r, c = map(int, input().rstrip().split())

board = [['1' for _ in range(c + 2)] for _ in range(r + 2)]

for y in range(1, r + 1):
	line = input().rstrip()
	for x in range(1, c + 1):
		board[y][x] = line[x - 1]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

_max = 1
x, y = 1, 1
q = set([(x, y, board[y][x])])

while q :
	x, y, visited = q.pop()
	
	for i in range(4):
		ny, nx = y + dy[i], x + dx[i]
		if board[ny][nx] == '1':
			continue
		if board[ny][nx] in visited:
			continue
		q.add((nx, ny, visited + board[ny][nx]))
		_max = max(_max, len(visited) + 1)

print(_max)