# BOJ 3665 위상정렬

from collections import deque
import sys

input = sys.stdin.readline

for tc in range(int(input().rstrip())):
	n = int(input().rstrip())
	nodes = list(map(int, input().rstrip().split()))

	board = [[False] * (n + 1) for _ in range(n + 1)]
	indegree = [0] * (n + 1)
	m = int(input().rstrip())
	
	for i in range(0, n - 1):
		for j in range(i + 1, n):
			board[nodes[i]][nodes[j]] = True
			indegree[nodes[j]] += 1

	for i in range(m):
		a, b = map(int, input().rstrip().split())
		if board[a][b] :
			board[a][b] = False
			board[b][a] = True
			indegree[b] -= 1
			indegree[a] += 1
		else :
			board[b][a] = False
			board[a][b] = True
			indegree[a] -= 1
			indegree[b] += 1

	queue = deque()

	for i in range(1, n + 1):
		if indegree[i] == 0:
			queue.append(i)

	length = 0
	is_cycle = False
	certain = True
	result = []

	for i in range(n):

		if len(queue) == 0:
			is_cycle = True
			break
		if len(queue) >= 2:
			certain = False
			break

		node = queue.popleft()
		result.append(node)
		for i in range(1, n + 1):
			if board[node][i]:
				indegree[i] -= 1
				if indegree[i] == 0:
					queue.append(i)
	if is_cycle:
		print("IMPOSSIBLE")
	elif not certain:
		print("?")
	else:
		print(result)