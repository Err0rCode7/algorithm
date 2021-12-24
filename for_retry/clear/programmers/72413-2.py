def solution(n, s, a, b, fares):

	graph = [[int((n * (n - 1) // 2) * 1e5)] * (n + 1) for _ in range(n + 1)]

	for _from, to, cost in fares:
		graph[_from][to] = cost
		graph[to][_from] = cost
	
	for i in range(n):
		graph[i][i] = 0

	for k in range(1, n + 1):
		for _from in range(1, n + 1):
			for to in range(1, n + 1):
				graph[_from][to] = min(graph[_from][to], graph[_from][k] + graph[k][to])
	answer = int((n * (n - 1) // 2) * 1e5)
	for i in range(n):
		answer = min(graph[s][i] + graph[i][b] + graph[i][a], answer)
	answer = min(answer, graph[s][a] + graph[a][b], graph[s][b] + graph[b][a])
	return answer

print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]	))
print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]	))