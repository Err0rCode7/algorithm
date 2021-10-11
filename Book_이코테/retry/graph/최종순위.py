import sys
from collections import deque

input = sys.stdin.readline

for i in range(int(input().rstrip())):
	n = int(input().rstrip())
	order = list(map(int, input().rstrip().split()))
	update_list = []

	graph = [[False] * (n + 1) for _ in range(n + 1)]
	indegree = [0] * (n + 1)
	for i in range(0, n - 1):
		for j in range(i + 1, n):
			graph[order[i]][order[j]] = True
			indegree[order[j]] += 1

	m = int(input().rstrip())
	for i in range(m):
		a, b = map(int, input().rstrip().split())
		
		if graph[a][b]:
			graph[a][b] = False
			graph[b][a] = True
			indegree[a] += 1
			indegree[b] -= 1
		else :
			graph[a][b] = True
			graph[b][a] = False
			indegree[b] += 1
			indegree[a] -= 1

	q = deque()
	for i in range(1, n + 1):
		if indegree[i] == 0:
			q.append(i)

	result = []
	type = 0
	for i in range(n):
		if len(q) == 0 :
			type = 1
			break
		elif len(q) >= 2 :
			type = 2
			break
		target = q.popleft()
		result.append(target)

		for i in range(1, n + 1):
			if graph[target][i] > 0:
				indegree[i] -= 1
				if indegree[i] == 0:
					q.append(i)

	if type == 0:
		for node in result:
			print(node, end=" ")
		print()
	elif type == 1:
		print("IMPOSSIBLE")
	else :
		print("?")