from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

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

parent = [0] * (N + 1)
for i in range(1, N + 1):
	parent[i] = i

for i in range(N):

	line = list(map(int, input().rstrip().split()))
	for j in range(N):
		if line[j] == 1:
			union_graph(parent, i + 1, j + 1)

plan = list(map(int, input().rstrip().split()))

first = parent[plan[0]]

flag = False

for i in plan:
	if first != parent[i]:
		flag = True
		break

if flag:
	print("NO")
else:
	print("YES")

