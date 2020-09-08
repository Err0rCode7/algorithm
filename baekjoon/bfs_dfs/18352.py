from collections import deque
import sys

# queue를 이용한 bfs 문제
# x 노드 부터 시작하여 거리가 k인 노드의 갯수 문제

def bfs(graph, x) :

	queue = deque()
	queue.append(x)
	visited[x] = 1
	distance[x] = 0

	while queue :
		vt = queue.popleft()
		for node in graph[vt] :
			if visited[node] == 0 :
				queue.append(node)
				visited[node] = 1
				distance[node] = distance[vt] + 1

n, m, k, x = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
distance = [0] * (n + 1)

for i in range(m) :
	start, end = map(int, sys.stdin.readline().rstrip().split())
	graph[start].append(end);

bfs(graph, x)

count = 0
for i in range(n + 1) :
	if (distance[i] == k) :
		count +=1

if count == 0 :
	print(-1)
else :
	print(count)
