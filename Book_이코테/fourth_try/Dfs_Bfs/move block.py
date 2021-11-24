# BFS 사용
# N, N에 도달하는 최소 길이를 찾는 것이므로 BFS

# DFS 는 시간초과

# 왼쪽을 기준으로 시계, 반시계
# 오른쪽을 기준으로 시계, 반시계

from collections import deque

def get_non_vertical_case(board, start):
	result = []
	first_x, first_y = start
	try :
		if board[first_y - 1][first_x] == 0 and board[first_y - 1][first_x + 1] == 0:
			result.append(((first_x, first_y - 1), 1))
			result.append(((first_x + 1, first_y - 1), 1))
			result.append(((first_x, first_y - 1), 0))
	except:
		pass
	try:
		if board[first_y + 1][first_x] == 0 and board[first_y + 1][first_x + 1] == 0:
			result.append(((first_x, first_y), 1))
			result.append(((first_x + 1, first_y), 1))
			result.append(((first_x, first_y + 1), 0))
	except:
		pass
	try:
		if board[first_y][first_x - 1] == 0:
			result.append(((first_x - 1, first_y), 0))
	except:
		pass
	try:
		if board[first_y][first_x + 2] == 0:
			result.append(((first_x + 1, first_y), 0))
	except:
		pass
	return result

def get_vertical_case(board, start):
	result = []
	first_x, first_y = start
	try:
		if board[first_y][first_x + 1] == 0 and board[first_y + 1][first_x + 1] == 0:
			result.append(((first_x, first_y), 0))
			result.append(((first_x, first_y + 1), 0))
			result.append(((first_x + 1, first_y), 1))
	except:
		pass
	try:
		if board[first_y][first_x - 1] == 0 and board[first_y + 1][first_x - 1] == 0:
			result.append(((first_x - 1, first_y), 0))
			result.append(((first_x - 1, first_y + 1), 0))
			result.append(((first_x - 1, first_y), 1))
	except:
		pass
	try:
		if board[first_y - 1][first_x] == 0:
			result.append(((first_x, first_y - 1), 1))
	except:
		pass
	try:
		if board[first_y + 2][first_x] == 0:
			result.append(((first_x, first_y + 1), 1))
	except:
		pass
	return result

def get_next_points(board, start, vertical) :

	if vertical:
		return get_vertical_case(board, start)
	else :
		return get_non_vertical_case(board, start)

def get_tail(x, y, vertical):
	x2, y2 = 0, 0
	if vertical:
		x2, y2 = x, y + 1
	else :
		x2, y2 = x + 1, y
	return (x2, y2)

def is_last(n, x, y, vertical):
	x2, y2 = get_tail(x, y, vertical)
	if (x == n - 1 and y == n - 1) or (x2 == n - 1 and y2 == n - 1) :
		return True
	return False

def solution(board) :
	
	queue = deque()
	n = len(board)
	visited = [[[0] * (n + 2) for _ in range(n + 2)]for _ in range(2)]
	# [v][y][x]
	new_board = [[1] * (n + 2) for _ in range(n + 2)]
	for i in range(n):
		for j in range(n):
			new_board[i + 1][j + 1] = board[i][j]
	queue.append(((1, 1), 0, 0))
	while queue:
		point, vertical, depth = queue.popleft()
		x, y = point
		if point == (n, n) or get_tail(x, y, vertical) == (n, n):
			return depth
		
		for next_point, next_vertical in get_next_points(new_board, point, vertical) :
			nx, ny = next_point
			if not visited[next_vertical][ny][nx] :
				queue.append((next_point, next_vertical, depth + 1))
				visited[next_vertical][ny][nx] = 1

	return -1


# print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))
print(solution([[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 1], [0, 0, 1, 0, 0, 0, 0]]))
print(solution([[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 0]]))
print(solution([[0, 0, 0, 0, 1, 0], [0, 0, 1, 1, 1, 0], [0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
print(solution([[0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0]]))
for line in [[0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0]]:
	print(line)
# if solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]) == 7 :
# 	print(True)
# else :
	# print(False)