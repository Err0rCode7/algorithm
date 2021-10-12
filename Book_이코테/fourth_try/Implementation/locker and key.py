'''
자물쇠와 열쇠

2차원 배열의 형태로 자물쇠와 열쇠가 존재하고 이 2차원 배열이 딱 맞물려서 하나의 자물쇠의 2차원 배열이 모두 채워지는 방법이 있는지 찾는 문제

1 2 3
4 5 6
7 8 9

7 4 1
8 5 2
9 6 3

'''
def getRotatedKey(key) :
	newKey = [[0] * len(key) for _ in range(len(key))]
	for y in range(len(key)):
		for x in range(len(key)) :
			newKey[x][len(key) - y - 1] = key[y][x]
	return newKey

def checkBoard(board) :
	m = len(board) // 3
	for y in range(m, 2 * m) :
		for x in range(m, 2 * m) :
			if board[y][x] != 1 :
				return False
	return True

def fillKey(board, startX, startY, key, sign) :
	for y in range(len(key)) :
		for x in range(len(key)) :
			board[y + startY][x + startX] += key[y][x] * sign

def solution(key, lock) :

	n = len(lock)
	m = len(key)

	# always m <= n

	board = [[0] * (n * 3 + 1) for _ in range(n * 3 + 1)]

	for y in range(n, 2 * n) :
		for x in range(n, 2 * n) :
			board[y][x] = lock[y - n][x - n]
	for i in range(4) :
		if i > 0 :
			key = getRotatedKey(key)

		for y in range(n - m + 1, 2 * n) :
			for x in range(n - m + 1, 2 * n) :
				fillKey(board, x, y, key, 1)
				if checkBoard(board) :
					return True
				fillKey(board, x, y, key, -1)

	return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))