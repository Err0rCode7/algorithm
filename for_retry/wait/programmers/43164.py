import heapq

def dfs(tickets, visited, move_list, result, n) :

	if len(move_list) == n + 1:
		# print(move_list)
		heapq.heappush(result, list(move_list))
		return

	for i in range(n):
		start, end = tickets[i]
		# print("start", start, "end", end)
		if visited[i] == True or move_list[-1] != start:
			continue
		# print("from:", move_list[-1], "to", start, "to", end)
		visited[i] = True
		move_list.append(end)
		dfs(tickets, visited, move_list, result, n)
		visited[i] = False
		move_list.pop()


def solution(tickets):

	n = len(tickets)
	visited = [False] * n

	move_list = ["ICN"]
	result = []
	dfs(tickets, visited, move_list, result, n)
	
	return result[0]

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]	))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]	))