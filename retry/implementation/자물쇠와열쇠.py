def is_valid(N, board):
	for y in range(N, N*2):
		for x in range(N, N*2):
			if board[y][x] != 1:
				return False
	return True

def rotate(array_2d):
	row = len(array_2d)
	col = len(array_2d[0])
	rotated_array = [[0] * col for i in range(row)]
	for y in range(row):
		for x in range(col):
			rotated_array[x][row - 1 - y] = array_2d[y][x]
	return (rotated_array)

def solution(key, lock):

	N = len(lock)
	M = len(key)
	board = [[0 for _ in range(N * 3)] for _ in range(N * 3)]

	for y in range(N, N*2):
		for x in range(N, N*2):
			board[y][x] = lock[y - N][x - N]

	for i in range(4):
		if i > 0 :
			key = rotate(key)
		for lock_y in range(2 * N):
			for lock_x in range(2 * N):
				for key_y in range(M):
					for key_x in range(M):
						board[lock_y + key_y][lock_x + key_x] += key[key_y][key_x]
				if is_valid(N, board):
					return True
				for key_y in range(M):
					for key_x in range(M):
						board[lock_y + key_y][lock_x + key_x] -= key[key_y][key_x]
	return (False)

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(solution(key, lock))
