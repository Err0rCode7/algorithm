# 크루스칼 알고리즘

import sys, heapq

def find_parent(parent, x):
	if parent[x] != x:
		parent[x] = find_parent(parent, parent[x])
	return (parent[x])

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
total = 0

for i in range(m):
	a, b, cost = map(int, input().rstrip().split())
	total += cost
	roads.append((cost, a, b))

heapq.heapify(roads)
parent = [0] * (n + 1)

for i in range(n + 1):
	parent[i] = i

result = 0
while roads:
	cost, a, b = heapq.heappop(roads)

	if find_parent(parent, a) != find_parent(parent, b):
		print("a: {a}, b: {b}".format(a=a, b=b))
		result += cost
		union_parent(parent, a, b)

print(total - result)