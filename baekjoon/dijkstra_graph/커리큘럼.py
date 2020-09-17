from collections import deque
import sys, copy


input = sys.stdin.readline

n = int(input().rstrip())

_class = [[] for _ in range(n + 1)]
depth = [0 for _ in range(n + 1)]
cost = [0 for _ in range(n + 1)]

for i in range(1, n + 1) :
	input_list = list(map(int, input().rstrip().split()))
	for a in range(0, len(input_list)) :
		if a == 0 :
			cost[i] = input_list[a]
		elif input_list[a] == -1 :
			break
		else :
			_class[input_list[a]].append(i)
			depth[i] += 1

def topology_sort() :
	result = copy.deepcopy(cost)
	q = deque()

	for i in range(1, n + 1) :
		if depth[i] == 0 :
			q.append(i)

	while q :
		now = q.popleft()
		for i in _class[now] :
			depth[i] -= 1
			result[i] = max(result[i], result[now] + cost[i])
			if depth[i] == 0:
				q.append(i)

	print(result)
	for i in range(1, n + 1):
		print(result[i])

topology_sort()
