import sys

# 모든 노드들을 경로의 값이 낮은 값 경로부터 루프없이 연결하는 방식으로
# 최소 비용으로 모든 노드를 연결하는 알고리즘

def find_parent(parent, x) :
	if (parent[x] != x) :
		parent[x] = find_parent(parent, parent[x])
	return parent[x]

def union_parent(parent, a, b) :
	a = find_parent(parent, a)
	b = find_parent(parent, b)

	if (a < b) :
		parent[b] = a
	else :
		parent[a] = b

input = sys.stdin.readline
v, e = map(int, input().split())
parent = [0] * (v + 1)

edges = []
result = 0

for i in range(1, v + 1):
	parent[i] = i

for _ in range(e) :
	node1, node2, cost = map(int, input().split())
	edges.append((cost, (node1, node2)))

edges.sort()

for edge in edges :
	cost, node1, node2 = edge
	if find_parent(node1) != find_parent(node2) :
		union_parent(parent, node1, node2)
		result += cost

print(result)
