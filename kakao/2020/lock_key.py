key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

def rotate(key) :
	length = len(key)
	rotate = [[] for _ in range(length)]
	for y in range(length) :
		for x in range(length) :
			rotate[y].append(key[length - 1 - x][y])
	return rotate

def reverse(key) :
	length = len(key)
	reverse = [[] for _ in range(length)]
	for x in range(length) :
		reverse[y].append(key[y][length - 1 - x])
	return reverse

def is_valid(lock, key_extend, a, b, key_len) :
	for y in range(len(lock)) :
		for x in range(len(lock)) :
			if lock[y][x] + key_extend[a + y][b + x] >= 2  or \
				lock[y][x] + key_extend[a + y][b + x] == 0 :
				return False
	return True

def solution(key, lock) :
	key_len = len(key)
	lock_len = len(lock)
	key_extend = [[0 for _ in range(key_len + lock_len * 2)] for _ in range(key_len + lock_len * 2)]
	for y in range(key_len) :
		for x in range(key_len) :
			key_extend[y + lock_len][x + lock_len] = key[y][x]
	i = 0
	while i < 4 :
		for a in range(0, lock_len + key_len + 1) :
			for b in range(0, lock_len + key_len + 1) :
				if is_valid(lock, key_extend, a, b, key_len) :
					return True
		key_extend = rotate(key_extend)
		i += 1
	return False

print(solution(key, lock))
