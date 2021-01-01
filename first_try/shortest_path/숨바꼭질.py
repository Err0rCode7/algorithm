import sys, heapq

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

graph = [[] for _ in range(N + 1)]

for i in range(M):
	a, b = map(int, input().rstrip().split())
	graph[a].append(b)
	graph[b].append(a)

distance = [N + 1] * (N + 1)
visited = [0] * (N + 1)
heap = [(0, 1)]
distance[1] = 0
while heap:
	dist, node = heapq.heappop(heap)
	visited[node] = 1
	for next in graph[node]:
		if visited[next]:
			continue
		if dist + 1 < distance[next]:
			distance[next] = dist + 1
			heapq.heappush(heap, (dist + 1, next))

max_node = 1
result = []
for i in range(1, N + 1):
	if distance[i] == N + 1:
		continue
	if distance[i] > distance[max_node]:
		max_node = i
		result = [i]
	elif distance[i] == distance[max_node]:
		result.append(i)

print(max_node, distance[max_node], len(result))
