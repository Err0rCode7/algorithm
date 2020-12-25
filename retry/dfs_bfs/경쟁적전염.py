from collections import deque
import sys

input = sys.stdin.readline

N, K = map(int, input().rstrip().split())

graph = []
virus = []

for i in range(N):
	line = list(map(int, input().rstrip().split()))
	for j in range(N):
		if line[j] > 0 :
			virus.append((line[j], 0, i, j,))
	graph.append(line)
S, X, Y = map(int, input().rstrip().split())

# bfs #
virus.sort()
queue = deque(virus)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while queue:
	virus_name, time, y, x = queue.popleft()
	if time == S:
		break
	for i in range(4):
		ny, nx = y + dy[i], x + dx[i]
		if ny >= N or nx >= N or ny < 0 or nx < 0:
			continue
		if graph[ny][nx] == 0:
			graph[ny][nx] = virus_name
			queue.append((virus_name, time + 1, ny, nx))

print(graph[X - 1][Y - 1])
