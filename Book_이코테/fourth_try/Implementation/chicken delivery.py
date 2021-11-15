
from itertools import combinations
import sys

input = sys.stdin.readline

n, m =  map(int, input().rstrip().split())

houses = []
chickens = []

for y in range(n) :
	row = list(map(int, input().rstrip().split()))

	for x, value in enumerate(row) :
		if value == 1:
			# 집
			houses.append((x, y))
		elif value == 2:
			# 치킨
			chickens.append((x, y))

chicken_comb = combinations(chickens, m)

max_length = 2 * n + 1

min_chicken_dist = max_length * len(houses)
for one_comb in chicken_comb:
	chicken_dist = 0
	for h_x, h_y in houses :
		min_dist = max_length

		for x, y in one_comb :
			dist = abs(h_x - x) + abs(h_y - y)
			min_dist = min(min_dist, dist)
		chicken_dist += min_dist
	min_chicken_dist = min(chicken_dist, min_chicken_dist)
print(min_chicken_dist)
