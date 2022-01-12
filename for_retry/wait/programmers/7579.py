from collections import defaultdict
import sys

input = sys.stdin.readline
n, m = map(int, input().rstrip().split())

M_SIZE = int(1e7)
in_memory = list(map(int, input().rstrip().split())) #400B
inactivation_cost = list(map(int, input().rstrip().split())) #400B

_map = defaultdict(int)

keys = []


for i in range(n):
	cost, free = inactivation_cost[i], in_memory[i]
	keys.sort(reversed=True)

	for key in keys:
		if key + free in _map.keys():
			_map[key + free] = min(_map[key + free], _map[key] + cost)

		else:
			_map[key + free] = _map[key] + cost
			keys.append(key + free)
	if free in _map.keys():
		_map[free] = min(_map[free], cost)
	else:
		_map[free] = cost
		keys.append(key + free)