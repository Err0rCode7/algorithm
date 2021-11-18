from collections import deque
import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, L, R = map(int, input().rstrip().split())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

board = []

for i in range(N):
	line = list(map(int, input().rstrip().split()))
	board.append(line)

def dfs(x, y, board, cluster, visited) :
	global L, R, N
	dx = [1, 0, -1, 0]
	dy = [0, 1, 0, -1]
	if visited[y][x]:
		return 0
	visited[y][x] = 1
	cluster.append((x, y))
	result = board[y][x]
	for i in range(4):
		nx, ny = x + dx[i], y + dy[i]
		if not (0 <= nx < N and 0 <= ny < N) :
			continue
		if L <= abs(board[ny][nx] - board[y][x]) <= R :
			result += dfs(nx, ny, board, cluster, visited)
	return result

result = 0
while True:
	clusters = []
	visited = [[0] * N for _ in range(N)]
	for y in range(N):
		for x in range(N):
			cluster = []
			_sum = dfs(x, y, board, cluster, visited)
			if len(cluster) > 1:
				clusters.append((_sum, cluster))
	if len(clusters) == 0:
		break
	else :
		for _sum, cluster in clusters:
			for x, y in cluster:
				board[y][x] = _sum // len(cluster)
		result += 1
print(result)
