import sys

def find_parent(parent, x):
	if parent[x] != x:
		parent[x] = find_parent(parent, parent[x])
	return parent[x]

def union_graph(parent, a, b):
	a = find_parent(parent, a)
	b = find_parent(parent, b)

	if a < b:
		parent[b] = a
	else :
		parent[a] = b

input = sys.stdin.readline

g = int(input().rstrip())
p = int(input().rstrip())

parent = [_ for _ in range(g + 1)]
result = 0
for i in range(p):
	node = int(input().rstrip())

	if find_parent(parent, node) == 0:
		break
	result += 1
	union_graph(parent, node, find_parent(parent, node) - 1)

print(result)
