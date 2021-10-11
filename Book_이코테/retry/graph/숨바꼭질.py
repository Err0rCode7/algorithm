import heapq
import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

visited = [False] * (n + 1)
dp = [1e10] * (n + 1)
path = [[] for _ in range(n + 1)]

for i in range(m):
	a, b = map(int, input().rstrip().split())
	path[a].append(b)
	path[b].append(a)

q = []
heapq.heappush(q, (0, 1))
result = 0
_list = [[] for _ in range(n + 1)]

while q:
	cost, node = heapq.heappop(q)
	if visited[node] :
		continue
	if cost > result:
		result = cost
	_list[cost].append(node)
	visited[node] = True
	dp[node] = cost
	for new_node in path[node]:
		if visited[new_node] :
			continue
		heapq.heappush(q, (cost + 1, new_node))

print(min(_list[result]), result, len(_list[result]))