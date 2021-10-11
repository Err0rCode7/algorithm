import sys

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

n = int(input().rstrip())

x_list = []
y_list = []
z_list = []
parent = [_ for _ in range(n)]

for i in range(n):
	x, y, z = map(int, input().rstrip().split())

	x_list.append((x, i))
	y_list.append((y, i))
	z_list.append((z, i))

costs = []

x_list.sort()
y_list.sort()
z_list.sort()

for i in range(n - 1):
	costs.append((x_list[i + 1][0] - x_list[i][0], (x_list[i + 1][1], x_list[i][1])))
	costs.append((y_list[i + 1][0] - y_list[i][0], (y_list[i + 1][1], y_list[i][1])))
	costs.append((z_list[i + 1][0] - z_list[i][0], (z_list[i + 1][1], z_list[i][1])))

costs.sort()

count = 0
result = 0
for cost, planets in costs:
	if count == n - 1:
		break
	a, b = planets

	if find_parent(parent, a) == find_parent(parent, b):
		continue
	union_parent(parent, a, b)
	count += 1
	result += cost

print(result)