import sys

input = sys.stdin.readline

sys.setrecursionlimit(10000)
n, c = map(int, input().rstrip().split())
house = []
for i in range(n):
	house.append(int(input()))

house.sort()

def binary_search(house, c, n) :
	_min = 1
	_max = house[-1] - house[0]

	result = _max
	while _min <= _max :
		mid = (_min + _max) // 2
		count = 1
		start = house[0]
		for i in range(1, n) :
			if mid <= house[i] - start :
				start = house[i]
				count += 1
		if count >= c :
			result = mid
			_min = mid + 1
		else :
			_max = mid - 1
	return(result)

print(binary_search(house, c, n))
