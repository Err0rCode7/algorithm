import heapq

def solution(a, edges):


	graph = [set() for _ in range(len(a))]
	for s, e in edges:
		graph[e].add(s)
		graph[s].add(e)

	heap = []
	for i in range(len(a)):
		if len(graph[i]) == 1:
			heapq.heappush(heap, (i))

	answer = 0
	while heap :
		start = heapq.heappop(heap)
		if len(graph[start]) == 0:
			continue
		end = graph[start].pop()
		cost = a[start]
		answer += abs(cost)
		a[start] = 0
		if cost > 0:
			a[end] += abs(cost)
		else :
			a[end] -= abs(cost)

		graph[end].remove(start)
		if len(graph[end]) == 1:
			heapq.heappush(heap, end)

	_sum = 0
	for cost in a:
		_sum += cost
	
	if cost == 0:
		return answer
	return -1

print(solution([-5,0,2,1,2]	, [[0,1],[3,4],[2,3],[0,3]]	))
print(solution([0, 1, 0]	, [[0,1],[1,2]]	))