def solution(n, stations, w):
	
	count = 0
	_range = w * 2 + 1

	_range_list = []
	pre_right = 1
	last = stations[-1]
	for station in stations:
		left = station - w - 1
		right = station + w + 1
		if station == last:
			if right <= n:
				_range_list.append((right, n))
		if left <= 0 or left < pre_right:
			pre_right = right
			continue
		_range_list.append((pre_right, left))
		pre_right = right
	count = 0
	for left, right in _range_list:
		size = right - left + 1
		if size % _range > 0:
			count += 1
		count += size // _range

	return count

# print(solution(11, [4, 11], 1))
# print(solution(16, [3, 14], 2))
print(solution(16, [6, 9], 2))