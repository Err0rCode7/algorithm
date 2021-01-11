# topology_sort 알고리즘

# 위상 정렬의 중요한 점은 진입차수이다.
# 진입차수에 맞게 다 진입이 된 노드는 다음 과정을 실행해도 되기 떄문이다.
# 따라서 진입 차수의 값을 세어나가면서 알고리즘을 진행한다.
# 1. 진입차수가 0인 노드를 큐에 넣는다.
# 2. 큐가 빌 때 까지 다음의 과정을 반복한다.
# 2-1. 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거한다.
# 2-1. 새롭게 진입차수가 0이 된 노드를 큐에 넣는다.

from collections import deque

v, e = map(int, input().split())

indegree = [0] * (v + 1)

graph = [[] for i in range(v + 1)]

for _ in range(e):
	a, b = map(int, input().split())
	graph[a].append(b)
	indegree[b] += 1

def topology_sort():
	result = []
	q = deque()

	for i in range(1, v + 1):
		if indegree[i] == 0:
			q.append(i)

	while q:
		now = q.popleft()
		result.append(now)

		for i in graph[now]:
			indegree[i] -= 1
			if indegree[i] == 0:
				q.append(i)

	for i in result:
		print(i, end=' ')
