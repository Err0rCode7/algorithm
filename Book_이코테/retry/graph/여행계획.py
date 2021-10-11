import sys

def find_parent(parent, x):
	if parent[x] != x:
		parent[x] = find_parent(parent, parent[x])
	return parent[x]

def union_graph(parent, a, b):
	a = find_parent(parent, a)
	b = find_parent(parent, b)

	if a < b :
		parent[b] = a
	else :
		parent[a] = b

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

parent = [_ for _ in range(n)]
board = []
for i in range(n):
	line = list(map(int, input().rstrip().split()))
	board.append(line)
	for j in range(i + 1):
		if line[j] == 1:
			union_graph(parent, i, j)

plan = list(map(int, input().rstrip().split()))

root = find_parent(parent, plan[0])
is_possible = True
for i in plan[1:] :
	if find_parent(parent, root) != root:
		is_possible = False
		break
if is_possible:
	print("YES")
else :
	print("NO")



