import sys

input = sys.stdin.readline

t = int(input().rstrip())

for i in range(t):
	n, m = map(int, input().rstrip().split())

	line = list(map(int, input().rstrip().split()))

	_map = []
	for i in range(n):
		_map.append(line[i * m : i * m + m])
	if n == 1:
		print(sum(_map[0]))
	else :
		result = 0
		for j in range(1, m):
			for i in range(n):
				if i == 0:
					_map[i][j] = _map[i][j] + max(_map[i + 1][j - 1], _map[i][j - 1])
				elif i == n - 1:
					_map[i][j] = _map[i][j] + max(_map[i - 1][j - 1], _map[i][j - 1])
				else :
					_map[i][j] = _map[i][j] + max(_map[i - 1][j - 1], _map[i][j - 1], _map[i + 1][j - 1])
				if j == m - 1:
					result = max(result, _map[i][j])
		print(result)