import sys, heapq

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
graph = [[] for _ in range(n + 1)]

costs = [int(1e9)] * (n + 1)
for i in range(m):
	a, b = map(int, input().rstrip().split())
	graph[a].append(b)
	graph[b].append(a)

queue = []
costs[1] = 0
for next_node in graph[1]:
	heapq.heappush(queue, (costs[1], next_node))

while queue :
	cost, cur = heapq.heappop(queue)
	if costs[cur] <= cost + 1:
		continue
	
	costs[cur] = cost + 1
	for next_node in graph[cur]:
		heapq.heappush(queue, (costs[cur], next_node))

distance = -1
count = 0
result_node = -1
for node in range(2, n + 1):
	if distance < costs[node]:
		distance = costs[node]
		count = 1
		result_node = max(node, result_node)
	elif distance == costs[node]:
		count += 1