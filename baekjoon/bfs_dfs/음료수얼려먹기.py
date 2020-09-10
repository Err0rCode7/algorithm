import sys

input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
graph = [[] for _ in range(n)]

for i in range(n) :
	instr = input().rstrip()
	for c in instr:
		graph[i].append(int(c))

dx = [1, 0, -1, 0]
dy = [0, 1, 0 ,-1]

def dfs(n, m, graph, stack) :

	while stack :
		x, y = stack.pop()
		graph[y][x] = 2
		for i in range(4) :
			nx, ny = x + dx[i], y + dy[i]
			if nx < 0 or ny < 0 or nx >= m or ny >= n :
				continue
			if graph[ny][nx] == 0 :
				stack.append((x, y))
				stack.append((nx, ny))


def solution(n, m, graph) :

	stack = []
	result = 0
	for y in range(n) :
		for x in range(m) :
			if (graph[y][x] == 0) :
				stack.append((x, y))
				result += 1
				dfs(n, m, graph, stack)
	return result

print(solution(n, m, graph))
for row in graph :
	print(row)

