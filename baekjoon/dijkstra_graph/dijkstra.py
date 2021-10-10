import sys

# 최단 경로 알고리즘 : 다익스트라 알고리즘
# 각 노드까지의 최단 경로의 값을 업데이트 해나가면서 최단 경로를 구하는 알고리즘

# 그래프 (이동 가능한 노드를 나타냄), 방문확인, 최단 거리 값 리스트를 초기화 하고 시작한다.
# 그래프는 입력값 대로, 방문 확인은 모두 0으로, 최단 거리 리스트는 INFINITE로 초기화한다.
# 방문할 수 있는 노드 중에서 처음 노드로부터 가장 거리가 짧고 방문하지 않은 노드를 선택하고
# 선택한 노드를 가는 값이 최단 거리 리스트에 있는 값보다 짧으면 업데이트 한다.
# 위의 과정을 반복하여 출발지로부터 모든 노드까지의 최단 경로를 구한다

n, m = map(int, sys.stdin.readline().rstrip().split())
INF = int(1e9)

start = int(sys.stdin.readline().rstrip())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

for _ in range(m) :
	node, to_node, value = map(int, sys.stdin.readline().rstrip().split())
	graph[node].append((to_node, value))

def get_smallest_node() :
	min_value = INF
	index = 0
	for i in range(1, n + 1) :
		if (distance[i] < min_value and not visited[i]):
			min_value = distance[i]
			index = i
	return index

def dijkstra(start) :

	distance[start] = 0
	visited[start] = True
	for j in graph[start] :
		distance[j[0]] = j[1]

	for i in range(n - 1) :
		now = get_smallest_node()
		visited[now] = True

		for j in graph[now] :
			cost = distance[now] + j[1]
			if cost < distance[j[0]] :
				distance[j[0]] = cost

dijkstra(start)

for i in range(1, n + 1) :
	if distance[i] == INF :
		print("INFINITE")
	else :
		print(distance[i])
