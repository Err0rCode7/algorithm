import sys, heapq
from collections import deque

input = sys.stdin.readline

# BFS

n = int(input())
baby_shark = ()
board = [[-1] * (n + 2) for _ in range(n + 2)]
for y in range(1, n + 1) :
	line = list(map(int, input().rstrip().split()))

	for x in range(1, n + 1) :
		if line[x - 1] == 9:
			baby_shark = (x, y, 0)
		board[y][x] = line[x - 1]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
game_time = 0
bs_size = 2
eat_count = 0
q = deque([baby_shark])
board[baby_shark[1]][baby_shark[0]] = 0

while True:

	fishes = []
	visited = [[0] * (n + 2) for _ in range(n + 2)]
	time = 0
	# BFS
	while q:
		bs_x, bs_y, time = q.popleft()
		if visited[bs_y][bs_x]:
			continue
		visited[bs_y][bs_x] = 1
		if fishes and time > fishes[0][0]:
			continue
		if (0 < board[bs_y][bs_x] < 9) and board[bs_y][bs_x] < bs_size:
			heapq.heappush(fishes, (time, bs_y, bs_x))
			continue
		for i in range(4):
			nx, ny = bs_x + dx[i], bs_y + dy[i]
			if board[ny][nx] == -1 or board[ny][nx] > bs_size:
				continue
			q.append((nx, ny, time + 1))

	if not fishes or time == 0:
		break
	time, n_bs_y, n_bs_x = heapq.heappop(fishes)
	board[n_bs_y][n_bs_x] = 0

	q.append((n_bs_x, n_bs_y, 0))
	game_time += time
	eat_count += 1
	if eat_count == bs_size:
		bs_size += 1
		eat_count = 0
print(game_time)