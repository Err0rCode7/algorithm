from collections import deque
import heapq

def solution(tickets):
	graph = {}
	airport = set()
	for start, end in tickets:
		if start == end:
			continue
		if start in airport:
			heapq.heappush(graph[start], end)
		else :
			airport.add(start)
			path = [end]
			graph[start] = path
		if end not in airport:
			graph[end] = []
			airport.add(end)
	start = "ICN"
	answer = []
	q = deque()
	answer.append(start)
	if graph[start]:
		q.append((start, heapq.heappop(graph[start])))
	while q:
		_from, to = q.popleft()
		answer.append(to)
		if graph[to]:
			temp = []
			_next = None
			if len(graph[to]) > 1:
				while graph[to] :
					_next = heapq.heappop(graph[to])
					if to not in graph[_next]:
						temp.append(_next)
					else :
						break
			else :
				_next = heapq.heappop(graph[to])
			q.append((to, _next))
			for _next in temp:
				heapq.heappush(graph[to], _next)

	return answer

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]	))
print(solution([["ICN", "ICN"], ["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]	))
