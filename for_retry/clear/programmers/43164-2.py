from collections import defaultdict
import heapq

def solution(tickets):
	graph = defaultdict(list)
	for ticket in tickets:
		a, b = ticket
		heapq.heappush(graph[a], b)
	
	stack = ["ICN"]
	result = []
	while stack :
		start = stack[-1]
		if graph[start]:
			stack.append(heapq.heappop(graph[start]))
		else :
			result.append(stack.pop())
	return list(reversed(result))

# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]	))
# print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]	))
print(solution([["ICN", "BBB"],["ICN", "CCC"],["BBB", "CCC"],["CCC", "BBB"],["CCC", "ICN"]]
))