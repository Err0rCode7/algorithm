from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
graph = [[] for _ in range(n)]

for i in range(n) :
	instr = input().rstrip()
	for c in instr :
		graph[i].append(int(c))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def solution(n, m, graph):
	queue = deque()
	queue.append((0, 0, 1))
	result = 0
	while queue :
		x, y, count = queue.popleft()
		graph[y][x] = 0
		if y == n - 1 and x == m - 1:
			result = count
			break
		for i in range(4) :
			nx, ny = x + dx[i], y + dy[i]
			if nx < 0 or ny < 0 or nx >= m or ny >= n :
				continue
			if graph[ny][nx] == 1 :
				queue.append((nx, ny, count + 1))
	return (result)

print(solution(n, m, graph))
