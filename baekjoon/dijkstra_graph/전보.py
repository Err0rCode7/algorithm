import heapq
import sys

input = sys.stdin.readline

n, m, c = map(int, input().rstrip().split())

INF = int(1e9)
graph = [[] for _ in range(n)]
distance = [INF] * (n + 1)

for i in range(m) :
	x, y, z = map(int, input().rstrip().split())
	graph[x].append((z, y))

def dijkstra(start) :
	q = []
	heapq.heappush(q, (0, start))

	while q :
		c_cost, now = heapq.heappop(q)

		if distance[now] < c_cost :
			continue
		for node in graph[now] :
			o_cost, next = node
			if distance[next] > o_cost + c_cost:
				distance[next] = o_cost + c_cost
				heapq.heappush(q, (c_cost + o_cost, next))

count = 0
max_distance = 0
for d in distance :
	if d != INF :
		count += 1
		max_distance = max(d, max_distance)

print(count, max_distance)
