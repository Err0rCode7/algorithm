from collections import deque

n, k = map(int, input().split())

virus = []
board = []

for i in range(n) :
	row = list(map(int, input().split()))
	board.append(row)
	for j in range(len(row)) :
		if row[j] != 0 :
			virus.append((row[j],j,i,0))

s, x, y = map(int, input().split())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(virus, s) :
	virus = deque(sorted(virus, key= lambda x:x[0]))
	while virus :
		v, a, b, time = virus.popleft()
		if time >= s :
			continue
		for j in range(4) :
			nx, ny = a + dx[j], b + dy[j]
			if nx < 0 or ny < 0 or nx >= n or ny >= n :
				continue
			if board[ny][nx] == 0 :
				board[ny][nx] = v
				virus.append((v,nx,ny,time+1))

bfs(virus,s)
print(board[x-1][y-1])
