import sys
import collections

input = sys.stdin.readline

tc = int(input())
for i in range(tc):
	n = int(input())
	graph = [[False] * (n + 1) for _ in range(n + 1)]
	indegree = [0] * (n + 1)
	
	data = list(map(int, input().rstrip().split()))
	for i in range(0, n):
		for j in range(i + 1, n):
			graph[data[i]][data[j]] = True
			indegree[data[j]] += 1
	m = int(input())
	for i in range(m):
		a, b = map(int, input().rstrip().split())

		if graph[a][b] :
			indegree[a] += 1
			indegree[b] -= 1
		else :
			indegree[b] += 1
			indegree[a] -= 1
		graph[a][b] = not graph[a][b]
		graph[b][a] = not graph[b][a]
	q = collections.deque()
	for i in range(1, n + 1):
		if indegree[i] == 0:
			q.append(i)
	cycle = False
	multiple = False
	result = []
	for i in range(n) :
		if not q:
			cycle = True
			break
		if len(q) > 1 :
			multiple = True
			break
		
		node = q.popleft()
		result.append(node)
		for j in range(1, n + 1):
			if graph[node][j]:
				indegree[j] -= 1
				if indegree[j] == 0:
					q.append(j)
	if cycle:
		print("IMPOSSIBLE")
	elif multiple:
		print("?")
	else:
		for node in result :
			print(node, end=' ')
		print()

