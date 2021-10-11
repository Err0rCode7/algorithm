# kruskal algorithm
# 가장 적은 비용으로 모든 노드를 연결하는 최소신장트리 알고리즘
# 가장 낮은 간선 부터 하나씩 신장 트리를 만들어 나간다.
# 사이클이 생기게되는 간선은 연결하지 않는다.
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

v, e = map(int, input().split())
parent = [0] * (v + 1)

edges = []
result = 0

for i in range(1, v + 1):
	parent[i] = i

for _ in range(e):
	a, b, cost = map(int, input().split())
	edges.append((cost, a, b))

edges.sort()

for edge in edges:
	cost, a, b = edge
	# 사이클이 발생하지 않는 경우에만 집합에 포함
	if find_parent(parent, a) != find_parent(parent, b):
		union_parent(parent, a, b)
		result += cost
print(result)
