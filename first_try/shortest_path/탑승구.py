import sys

def find_parent(parent, x):
	if parent[x] != x:
		parent[x] = find_parent(parent, parent[x])
	return parent[x]

def union_node(parent, a, b):
	a = find_parent(parent, a)
	b = find_parent(parent, b)

	if a < b:
		parent[b] = a
	else :
		parent[a] = b

input = sys.stdin.readline

g = int(input())
p = int(input())

parent = [0] * (g + 1)

for i in range(1, g + 1):
	parent[i] = i

count = 0

for i in range(p):

	node = find_parent(parent, int(input()))

	if node == 0:
		break
	union_node(parent, node, node - 1)
	count += 1
print(count)
