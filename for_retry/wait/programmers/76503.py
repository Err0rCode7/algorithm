import heapq

def solution(a, edges):
	edge_counts = [0] * len(a)
	graph = [set() for _ in range(len(a))]
	for _from, to in edges:
		edge_counts[_from] += 1
		edge_counts[to] += 1
		graph[_from].add(to)
		graph[to].add(_from)

	q = []
	for i in range(len(a)):
		if len(graph[i]) == 1:
			heapq.heappush(q, i)

	answer = 0
	count = 0
	target = -1
	while q :
		node = heapq.heappop(q)
		count += 1
		cost = abs(a[node])
		if not graph[node]:
			continue
		target = graph[node].pop()
		if a[node] > 0:
			a[target] += cost
		else :
			a[target] -= cost
		a[node] = 0
		answer += cost
		graph[target].remove(node)
		if len(graph[target]) == 1:
			heapq.heappush(q, target)
	# 마지막 검사가 0이 아닐때
	if target >= 0 and a[target] != 0:
		return -1
	return answer

print(solution([-5,0,2,1,2]	, [[0,1],[3,4],[2,3],[0,3]]	))
print(solution([0,1,0]		, [[0,1],[1,2]]		))