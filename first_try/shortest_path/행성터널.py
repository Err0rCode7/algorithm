# BOJ 2887 크루스칼 알고리즘

import sys

def find_parent(parent, x):
	if parent[x] != x:
		parent[x] = find_parent(parent, parent[x])
	return (parent[x])

def union_graph(parent, a, b):
	a = find_parent(parent, a)
	b = find_parent(parent, b)

	if a < b:
		parent[b] = a
	else :
		parent[a] = b

input = sys.stdin.readline

n = int(input())

parent = [0] * (n + 1)
for i in range(1, n + 1):
	parent[i] = i

x = []
y = []
z = []

for i in range(1, n + 1):
	a, b, c = map(int, input().rstrip().split())
	x.append((a, i))
	y.append((b, i))
	z.append((c, i))

edges = []

x.sort()
y.sort()
z.sort()

for i in range(n - 1):
	edges.append((x[i + 1][0] - x[i][0], x[i][1], x[i + 1][1]))
	edges.append((y[i + 1][0] - y[i][0], y[i][1], y[i + 1][1]))
	edges.append((z[i + 1][0] - z[i][0], z[i][1], z[i + 1][1]))

edges.sort()

result = 0
count = 0

for cost, a, b in edges:
	print(cost)
	if count == n - 1:
		break
	if (find_parent(parent, a) != find_parent(parent, b)):
		union_graph(parent, a, b)
		result += cost
		count += 1

print(result)
