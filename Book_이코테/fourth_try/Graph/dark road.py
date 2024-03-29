import sys, heapq

input= sys.stdin.readline

n, m = map(int, input().rstrip().split())
edges = []
parent = [i for i in range(n)]

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

total = 0

for i in range(m):
	a, b, cost = map(int, input().rstrip().split())
	total += cost
	heapq.heappush(edges, (cost, a, b))

save = 0

while edges:
	cost, a, b = heapq.heappop(edges)

	if find_parent(parent, a) != find_parent(parent, b):
		save += cost
		union(parent, a, b)

print(total - save)