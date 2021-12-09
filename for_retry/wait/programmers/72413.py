def solution(n, s, a, b, fares):

	INF = int(1e6) + 1
	graph = [[INF] * (n + 1) for _ in range(n + 1)]

	for start, end, fare in fares:
		graph[start][end] = fare
		graph[end][start] = fare

	for i in range(1, n + 1):
		graph[i][i] = 0
	for k in range(1, n + 1):
		for n1 in range(1, n + 1):
			for n2 in range(1, n + 1):
				# min 함수가 일반 조건문에 비하여 속도가 더 느리다 (부가적인 iter 처리나 등등이 있어서 그럴것으로 예상)
				# 특히나 이 문제의 플로이드 와샬 알고리즘은 n^3이므로 더 사이드이펙트가 크다.
				# 원래 n1과 n2가 같이 있을 때 묵어서 처리하였는데, n^3으로 인해 틀리는 테스트 케이스가 존재함.
				# 따로 O(n)이 되도록 for문을 빼주는 것이 좋다.
				if graph[n1][n2] > graph[n1][k] + graph[k][n2]:
					graph[n1][n2] = graph[n1][k] + graph[k][n2]
				# graph[n1][n2] = min(graph[n1][n2], graph[n1][k] + graph[k][n2])
	min_total = INF * (n + 1)
	for center in range(1, n + 1):
		temp = graph[center][s] + graph[center][a] + graph[center][b]
		if temp < min_total:
			min_total = temp
	
	return min_total

print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
print(solution(6, 4, 5, 6, [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))