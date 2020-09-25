from itertools import combinations
from collections import deque
import copy, sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())

graph = []
virus = []
safe = []

for i in range(n) :
	row = list(map(int, input().rstrip().split()))
	graph.append(row)
	for j in range(m) :
		if row[j] == 2 :
			virus.append((j, i))
		elif row[j] == 0 :
			safe.append((j, i))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(graph, virus) :
	queue = deque(virus)
	while queue :
		x, y = queue.popleft()

		for i in range(4) :
			nx, ny = x + dx[i], y + dy[i]
			if nx < 0 or ny < 0 or nx >= m or ny >= n :
				continue
			elif graph[ny][nx] == 0 :
				graph[ny][nx] = 2
				queue.append((nx, ny))

def get_num_of_safezone(graph) :
	result = 0
	for y in range(n):
		for x in range(m) :
			if graph[y][x] == 0:
				result += 1

	return (result)

def build(graph, safe, virus) :

	result = 0

	comb_list = combinations(safe, 3)
	for comb in comb_list :
		new = copy.deepcopy(graph)
		for x, y in comb :
			new[y][x] = 1
		bfs(new, virus)
		result = max(result, get_num_of_safezone(new))
	return (result)

print(build(graph, safe, virus))
