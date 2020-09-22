from itertools import combinations

n, m = map(int, input().split())

houses = []
shops = []
for y in range(n) :
	board = list(map(int, input().split()))
	for x in range(n) :
		if board[x] == 2 :
			houses.append((y, x))
		elif board[x] == 1 :
			shops.append((y, x))

comb = list(combinations(shops, m))

def get_sum(combi) :
	sum = 0
	for h in houses :
		temp = int(1e9)
		for shop in combi :
			temp = min(temp, abs(shop[0] - h[0]) + abs(shop[1] - h[1]))
		sum += temp
	return sum

result = int(1e9)
for c in comb :
	result = min(result, get_sum(c))

print(result)
