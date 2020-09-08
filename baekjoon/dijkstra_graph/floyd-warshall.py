import sys
input = sys.stdin.readline

# 다익스트라는 바로 연결되어 있는 값 중에서 최단 경로를 선택하는 알고리즘이였다면,
# 플로이드 워셜 알고리즘은 현재의 노드를 통해서 갈 수 있는 최단 경로를 업데이트 하는 방식이다.
# a 에서 b로 가는 값을 선택할 때, a에서 b로 바로 갈 수 있는 값과 k노드를 통해 a에서 k와 k에서 b를 통해 가는 방식 중 최소 값을 선택한다.
# 점화식을 통해 모든 경로를 해보기 때문에 O(n^3)의 시간복잡도를 갖는다.

# 2차원 배열을 선언하여 a에서 b로 가는 INFINITE 값으로 초기화하고 자기 자신으로 가는 즉, a에서 a로 가는 경로를 최소 값 0으로 초기화한다.
# a에서 b로 직접 가는 경로와 k를 통해 a에서 b 로 가는 경로를 비교하여 최단 경로를 얻기 위해 3중 포문을 이용하여 모든 경로를 탐색한다.

INF = int(1e9)
n, m = map(int, input().rstrip().split())
graph = [[INF for _ in range(n + 1)] for _ in range(n + 1)]

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
