import sys

sys.setrecursionlimit(10000)

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

parent = [i for i in range(n + 1)]

def find_parent(parent, x):
	if parent[x] != x:
		parent[x] = find_parent(parent, parent[x])
	return parent[x]

def union(parent, a, b):
	a = find_parent(parent, a)
	b = find_parent(parent, b)

	if a == b:
		return
	if a < b:
		parent[b] = a
	else :
		parent[a] = b

for a in range(1, n + 1) :
	line = list(map(int, input().rstrip().split()))

	for b in range(1, n + 1):
		if line[b - 1] == 1:
			union(parent, a, b)

plan = list(map(int, input().rstrip().split()))
pre = -1
fail = False
for node in plan:
	if pre == -1:
		pre = node
		continue
	
	pre_parent = find_parent(parent, pre)
	cur_parent = find_parent(parent, node)
	if pre_parent != cur_parent:
		fail = True
		break

if fail :
	print("NO")
else :
	print("YES")
