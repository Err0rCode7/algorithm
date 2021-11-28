import sys, heapq

input = sys.stdin.readline

n = int(input())

graph = [i for i in range(n)]
x_costs = []
y_costs = []
z_costs = []

for i in range(n):
	x, y, z = map(int, input().rstrip().split())
	
	heapq.heappush(x_costs, (x, i))
	heapq.heappush(y_costs, (y, i))
	heapq.heappush(z_costs, (z, i))

x_pre_cost, x_pre_node = heapq.heappop(x_costs)
y_pre_cost, y_pre_node = heapq.heappop(y_costs)
z_pre_cost, z_pre_node = heapq.heappop(z_costs)

edges = []

for i in range(1, n) :
	x_cur_cost, x_node = heapq.heappop(x_costs)
	y_cur_cost, y_node = heapq.heappop(y_costs)
	z_cur_cost, z_node = heapq.heappop(z_costs)

	heapq.heappush(edges, (abs(x_cur_cost - x_pre_cost), x_node, x_pre_node))

	heapq.heappush(edges, (abs(y_cur_cost - y_pre_cost), y_node, y_pre_node))

	heapq.heappush(edges, (abs(z_cur_cost - z_pre_cost), z_node, z_pre_node))

	x_pre_cost, x_pre_node = x_cur_cost, x_node
	y_pre_cost, y_pre_node = y_cur_cost, y_node
	z_pre_cost, z_pre_node = z_cur_cost, z_node

def find_parent(parent, x):
	if parent[x] != x:
		parent[x] = find_parent(parent, parent[x])
	return parent[x]
def union(parent, a, b):
	a = find_parent(parent, a)
	b = find_parent(parent, b)

	if a < b:
		parent[b] = a
	else :
		parent[a] = b

count = 0
total_cost = 0
while count < n - 1 and edges:
	cost, a, b = heapq.heappop(edges)
	if find_parent(graph, a) == find_parent(graph, b):
		continue
	union(graph, a, b)
	count += 1
	total_cost += cost
print(total_cost)