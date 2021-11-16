from collections import deque
import sys

input = sys.stdin.readline

N, M, K, X = map(int, input().rstrip().split())
graph = [[] for _ in range(N + 1)]

for i in range(M):
	_from, _to = map(int, input().rstrip().split())
	graph[_from].append(_to)

dists = [N + 1] * (N + 1)

stack = deque()
stack.append((X, 0))

# Dfs - Success
while stack :
	node, dist = stack.pop()
	dists[node] = dist
	if dist + 1 > K : # back-tracking
		continue
	for next_node in graph[node]:
		if dists[next_node] > dist + 1:
			stack.append((next_node, dist + 1))

result = []
for node in range(N + 1):
	if dists[node] == K :
		result.append(node)
if len(result) :
	result.sort()
	for node in result:
		print(node)
else :
	print(-1)

'''
# Bfs - Success
queue = deque((X, 0))
visited = [0] * (N + 1)
result = []
while queue :
	node, dist = queue.popleft()
	if visited[node]:
		continue
	visited[node] = 1
	if dist == K :
		result.append(node)
		continue
	for to in graph[node] :
		queue.append((to, dist + 1))

if len(result) :
	result.sort()
	for node in result:
		print(node)
else :
	print
'''