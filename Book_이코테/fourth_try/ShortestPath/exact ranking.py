import sys
from collections import deque

input = sys.stdin.readline
print("## DFS 풀이 ##")
n, m = map(int, input().rstrip().split())

graph = [[] for _ in range(n + 1)]

for i in range(m):
	start, end = map(int, input().rstrip().split())
	graph[start].append(end)

out_count = [0 for _ in range(n + 1)]
in_count = [0 for _ in range(n + 1)]
visited = [[0] * (n + 1) for _ in range(n + 1)]
for cur_node in range(1, n + 1):
	one_out_count = 0
	queue = deque(graph[cur_node])
	while queue:
		next_node = queue.pop()
		if visited[cur_node][next_node] != 0 or next_node == cur_node:
			continue
		visited[cur_node][next_node] = 1
		in_count[next_node] += 1
		out_count[cur_node] += 1
		for node in graph[next_node]:
			queue.append(node)
result = 0
for node in range(1, n + 1):
	print("--", out_count[node], in_count[node])
	if out_count[node] + in_count[node] == n - 1:
		result += 1
print(result)

print("## Floyd 풀이 ##")
n, m = map(int, input().rstrip().split())

graph = [[int(1e9)] * (n + 1) for _ in range(n + 1)]

for i in range(m):
	start, end = map(int, input().rstrip().split())
	graph[start][end] = 1

for k in range(1, n + 1):
	for a in range(1, n + 1):
		for b in range(1, n + 1):
			graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
result = 0
for a in range(1, n + 1):
	count = 0
	for b in range(1, n + 1):
		if graph[a][b] != int(1e9) or graph[b][a] != int(1e9):
			count += 1
	if count == n - 1:
		result += 1
print(result)