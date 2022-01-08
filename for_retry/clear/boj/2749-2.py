n = int(input())

_map = dict()
_map[0] = 0
_map[1] = 1

P = int(1e6)

def half_search(n):

	if n in _map.keys():
		return _map[n]
	if n % 2 == 1:
		a = half_search((n + 1) // 2)
		b = half_search((n - 1) // 2)
		left = (a * a) % P
		right = (b * b) % P
		result = (left + right) % P
	else:
		a = half_search(n // 2)
		b = half_search((n // 2) - 1)
		left = a
		right = 2 * b
		right %= P
		right += a
		right %= P
		result = (left * right) % P
	_map[n] = result
	return _map[n]
print(half_search(n))