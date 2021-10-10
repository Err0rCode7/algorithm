import heapq
import sys

# 기존의 다익스트라 알고리즘 O(n^2)에서 힙을 이용하여 O(nlogn)으로 개선한 방식
# 가장 작은 값을 찾는 방식이 필요없이 최단 경로로 갈 수 있는 노드를 힙에 넣어 정렬된 순서로 꺼내 사용할 수 있는 구조

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
				distance[i[0]] = cost
				heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n + 1) :
	if distance[i] == INF :
		print("INFINITE")
	else :
		print(distance[i])
