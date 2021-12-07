n, m = map(int, input().rstrip().split())

trees = list(map(int, input().rstrip().split()))

s = 0
e = sum(trees)

result = 0

while s <= e:
	height = (e + s) // 2
	take = 0
	for i in range(n):
		tree = trees[i]
		take += tree - height if tree >= height else 0
	
	if take >= m:
		s = height + 1
		result = max(height, result)
	else :
		e = height - 1

print(result)
