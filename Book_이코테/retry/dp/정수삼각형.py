import sys

input = sys.stdin.readline

n = int(input().rstrip())

_map = []
for i in range(n):
	line = list(map(int, input().rstrip().split()))
	_map.append(line)

result = 0

if i == 1:
	result = _map[0][0]

for i in range(1, n):
	for j in range(i + 1):
		if j == 0:
			_map[i][j] = _map[i][j] + _map[i - 1][j]
		elif j == i:
			_map[i][j] = _map[i][j] + _map[i - 1][j - 1]
		else :
			_map[i][j] = _map[i][j] + max(_map[i - 1][j - 1], _map[i - 1][j])
		if i == n - 1:
			result = max(result, _map[i][j])
print(result)