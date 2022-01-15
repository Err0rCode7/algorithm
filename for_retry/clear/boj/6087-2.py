import sys, heapq

input = sys.stdin.readline

w, h = map(int, input().rstrip().split())

board = []
points = []

for i in range(h):
	line = input().rstrip()
	board.append(line)
	for j in range(w):
		if line[j] == 'C':
			points.append((j, i))

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def dijstra(x, y, tx, ty):
	visited = [[100 * 100 * 100] * w for _ in range(h)]
	q = [(0, x, y, -1)]
	visited[y][x] = 0
	while q :
		cost, x, y, v = heapq.heappop(q)
		if visited[y][x] < cost:
			continue
		for i in range(4):
			dx, dy = d[i]
			nx, ny = x + dx, y + dy
			add = 0 if v == -1 or v == i else 1
			if 0 <= nx < w and 0 <= ny < h and cost + add <= visited[ny][nx]\
				and (board[ny][nx] == 'C' or board[ny][nx] == '.'):
				
				visited[ny][nx] = cost + add
				heapq.heappush(q, (cost + add, nx, ny, i))
	return visited[ty][tx]

print(dijstra(points[0][0], points[0][1], points[1][0], points[1][1]))

'''
7 8
.......
......C
......*
*****.*
....*..
....*..
.C..*..
.......

'''