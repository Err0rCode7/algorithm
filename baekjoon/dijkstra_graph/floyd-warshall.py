import sys
input = sys.stdin.readline

INF = int(1e9)
n, m = map(int, input().rstrip().split())
graph = [[INF] for _ in range(n + 1)]

for y in range(1, n + 1) :
	for x in range(1, n + 1) :
		if x == y :
			graph[y][x] = 0

for _ in range(m) :
	node, to_node, value = map(int, input().split())
	graph[to_node][node] = value

for k in range(1, n + 1) :
	for a in range(1, n + 1) :
		for b in range(1, n + 1) :
			graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n + 1) :
	for b in range(1, n + 1) :
		if graph[a][b] == 1e9 :
			print("INFINITY", end = " ")
		else :
			print(graph[a][b], end = " ")
	print()
