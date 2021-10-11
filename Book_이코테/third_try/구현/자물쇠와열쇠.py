# 카카오
# https://programmers.co.kr/learn/courses/30/lessons/60059

# test case

# key	lock	result
# Q:
# solution ([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])
# A:
# true

def getRotated2d(array) :

	n = len(array)

	result = [[0] * n for _ in range(n)]

	for y in range(n):
		for x in range(n):
			result[x][n - 1 - y] = array[y][x]
	return result

def isFull(board, m, n):

	for y in range(m - 1, m - 1 + n):
		for x in range(m - 1, m - 1 + n):
			if board[y][x] != 1:
				return False
	return True

def solution(key, lock):

	# 회전 360 // 2 -> 4번

	# 자물쇠를 기준으로 브루드 포스

	n = len(lock)
	m = len(key)

	array = lock

	boardSize = 2 * (m - 1) + n
	board = [[0] * boardSize for _ in range(boardSize)]
	# 총 4번 회전
	for i in range(4):
		# 첫 번째는 회전 안함
		if i > 0:
			array = getRotated2d(array)

		# 보드 중앙에 자물쇠 모양을 채움
		for y in range(m - 1, m - 1 + n):
			for x in range(m - 1, m - 1 + n):
				board[y][x] = array[y - (m - 1)][x - (m - 1)]

		# 보드에 키의 시작 위치 루프
		for y in range(boardSize - (m - 1)):
			for x in range(boardSize - (m - 1)):
				
				# 보드에 키를 꼽아본다.
				for y_key in range(m):
					for x_key in range(m):
						board[y + y_key][x + x_key] += key[y_key][x_key]

				# 자물쇠가 채워졌는지 확인한다.
				if isFull(board, m, n):
					return True

				# 보드 롤백
				for y_key in range(m):
					for x_key in range(m):
						board[y + y_key][x + x_key] -= key[y_key][x_key]
	
	return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))

