import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
INF = int(1e9)

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(m) :
	a, b = map(int, input().rstrip().split())
	graph[a][b] = 1
	graph[b][a] = 1

x, k = map(int, input().rstrip().split())

for k in range(1, n + 1) :
	for a in range(1, n + 1) :
		for b in range(1, n + 1):
			graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][k] + graph[k][x]

if distance >= INF :
	print("-1")
else :
	print(distance)
