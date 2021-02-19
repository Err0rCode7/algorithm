import sys, heapq

sys.setrecursionlimit(10000)

def find_parent(parent, x):
	if parent[x] != x:
		parent[x] = find_parent(parent, parent[x])
	return parent[x]

def union_parent(parent, a, b):
	a = find_parent(parent, a)
	b = find_parent(parent, b)

	if a < b:
		parent[b] = a
	else :
		parent[a] = b

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

roads = []
parent = [_ for _ in range(n + 1)]


total = 0
for i in range(m):
	x, y, z = map(int, input().rstrip().split())
	heapq.heappush(roads, (z, x, y))
	total += z
result = 0
while roads:
	cost, a, b = heapq.heappop(roads)

	if find_parent(parent, a) == find_parent(parent, b):
		continue
	result += cost
	union_parent(parent, a, b)

print(total - result)