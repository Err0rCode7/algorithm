import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[1e9] * (n + 1) for _ in range(n + 1)]


for i in range(m):
	start, end, cost = map(int, input().rstrip().split())
	graph[start][end] = min(graph[start][end], cost)

for k in range(1, n + 1):
	for a in range(1, n + 1):
		for b in range(1, n + 1):
			if a == b:
				continue
			graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n + 1):
	for b in range(1, n + 1):
		if graph[a][b] == 1e9:
			graph[a][b] = 0
		if b == n:
			print(graph[a][b], end='')
		else :
			print(graph[a][b], end=' ')
	print()
