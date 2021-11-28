import sys

input = sys.stdin.readline

G = int(input())
P = int(input())

graph = [i for i in range(G + 1)]

def find_parent(parent, x):
	if parent[x] != x:
		parent[x] = find_parent(parent, parent[x])
	return parent[x]

def union(parent, a, b):
	a = find_parent(parent, a)
	b = find_parent(parent, b)

	if a < b :
		parent[b] = a
	else:
		parent[a] = b

count = 0
for i in range(P):
	airplane = int(input())
	parent = find_parent(graph, airplane)
	if parent == 0:
		break
	count += 1
	union(graph, parent - 1, parent)

print(count)