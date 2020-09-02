import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().rstrip().split())

start = int(input().rstrip())

graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m) :
	node, to_node, value = map(int, input().rstrip().split())
	graph[node].append((to_node, value))

def dijkstra(start) :
	q = []
	heapq.heappush(q, (0, start))
	distance[start] = 0

	while q:
		dist, now = heapq.heappop(q)

		if (distance[now] < dist) :
			continue
		for i in graph[now] :
			cost = dist + i[1]
			if cost < distance[i[0]] :
				distancep[i[0]] = cost
				heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n + 1) :
	if distance[i] == INF :
		print("INFINITE")
	else :
		print(distance[i])
