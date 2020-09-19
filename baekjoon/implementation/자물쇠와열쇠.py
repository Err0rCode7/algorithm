
def rotate(array) :
	row = len(array)
	col = len(array[0])
	result = [[0 for _ in range(col)] for _ in range(row)]
	for i in range(row) :
		for j in range(col):
			result[j][row - i - 1] = array[i][j]
	return result
def check(array, n) :

	for y in range(n, 2 * n):
		for x in range(n, 2 * n):
			if array[y][x] != 1  :
				return False
	return True

def solution(key, lock) :

	m, n = len(key), len(lock)
	map = [[0 for _ in range(n * 3)] for _ in range(n * 3) ]

	for y in range(n, 2 * n):
		for x in range(n, 2 * n):
			map[y][x] = lock[y-n][x-n]

	for r in range(4) :
		key = rotate(key)
		for l_y in range(2 * n) :
			for l_x in range(2 * n) :
				for k_y in range(m):
					for k_x in range(m):
						map[l_y + k_y][l_x + k_x] += key[k_y][k_x]

				if check(map, n) :
					return True

				for k_y in range(m):
					for k_x in range(m):
						map[l_y + k_y][l_x + k_x] -= key[k_y][k_x]
	return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
