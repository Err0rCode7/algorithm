import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

chickens = []
houses = []
for i in range(N):
	_list = list(map(int, input().rstrip().split()))
	for j in range(len(_list)) :
		if _list[j] == 1 :
			houses.append((i, j))
		elif _list[j] == 2 :
			chickens.append((i, j))

combs = combinations(chickens, M)
result = 251 * len(houses)
for comb in combs:
	total = 0
	for h_y, h_x in houses:
		min_value = 251
		for c_y, c_x in comb:
			ab_y = c_y - h_y if c_y - h_y > 0 else h_y - c_y
			ab_x = c_x - h_x if c_x - h_x > 0 else h_x - c_x
			min_value = min(min_value, ab_x + ab_y)
		total += min_value
	result = min(result, total)
print(result)
