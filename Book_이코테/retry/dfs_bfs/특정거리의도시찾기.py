import sys
from collections import deque

input = sys.stdin.readline

N, M, K, X = map(int, input().rstrip().split())

graph = [[] for _ in range(N + 1)]

for i in range(M):
	a, b = map(int, input().rstrip().split())
	graph[a].append((b, 1))

queue = deque(graph[X])

result = []
visited = [X]
while queue:
	node, count = queue.popleft()
	if count == K:
		if not node in visited:
			result.append(node)
	else :
		for next in graph[node]:
			next_node, next_count = next
			if not next_node in visited:
				queue.append((next_node, count + 1))
	visited.append(node)

if len(result) > 0:
	for node in sorted(result):
		print(node)
else :
	print(-1)
