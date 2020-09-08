from collections import deque
import sys

# queue를 이용한 bfs 문제
# map에서 0이 아니고 가장 낮은 값 부터 시작하여 이 값이 1초마다 동서남북으로 0인 칸에 한 칸씩 증식을 할 때,
# s초 상황에서 (o_x, o_y) 좌표에 있는 값 찾는 문제

def bfs(graph) :
	queue = deque()

	for c_k in range(1, k + 1) :
		for c_y in range(n) :
			for c_x in range(n) :
				if graph[c_y][c_x] == c_k :
					queue.append((c_x, c_y, 0))
	while queue :
		x, y, level = queue.popleft()
		if (level == s) :
			continue
		for i in range(4) :
			nx = x + dx[i]
			ny = y + dy[i]
			if nx < 0 or nx >= n or ny < 0 or ny >= n :
				continue
			if graph[ny][nx] != 0 :
				continue
			graph[ny][nx] = graph[y][x]
			queue.append((nx, ny, level + 1))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, k = map(int, sys.stdin.readline().rstrip().split())
graph = [[] * 3 for _ in range(n)]
result = []

for i in range(n):
	graph[i] = list(map(int, sys.stdin.readline().rstrip().split()))

s, o_x, o_y = map(int, sys.stdin.readline().rstrip().split())
bfs(graph)
print(graph[o_x - 1][o_y - 1])
