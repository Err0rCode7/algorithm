import heapq
from collections import defaultdict, deque

def solution(tickets):

	graph = defaultdict(list)

	def init_graph(graph, tickets):
		for start, end in tickets:
			heapq.heappush(graph[start], end)
	
	init_graph(graph, tickets)

	stack = deque()
	stack.append("ICN")
	result = []
	n = len(tickets)
	while stack :
		start = stack[-1]
		if graph[start] :
			stack.append(heapq.heappop(graph[start]))
		else :
			result.append(stack.pop())
	result.reverse()
	return (result)

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]	))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]	))