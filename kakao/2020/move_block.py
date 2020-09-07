from collections import deque

# bfs를 이용한 구현문제

# 2 x 1 형태의 로봇이 이동할 수 있는 경로를 따라서 목적지에 도착하는 가장 짧은 시간을 구하는 문제이다.
# 0은 빈칸 1은 벽
# (1,1)에서 시작 (1,1) (1,2)은 처음 로봇의 시작점으로 항상 0

# 큐를 이용하여 bfs로 로봇이 이동할 수 있는 경로를 담고 Low 레벨에서 방문했으면 재방문을 안하는 형태로 풀면 되는 문제이다.

testcases = []
testcases.append([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]])
# output : 7
testcases.append([[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 1], [0, 0, 1, 0, 0, 0, 0]])
# output : 21
testcases.append([[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 0]])
# output : 11
testcases.append([[0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0]])
# output : 33

# 반시계 방향
def rotation (board, cur_pos, is_vertical, second, spindle) :
	x1, y1, x2, y2 = cur_pos
	if is_vertical == 0 :
		if spindle == 0 :
			result = (x1, y1 - 1, x1, y1, 1, second + 1)
		if spindle == 1:
			result = (x2, y2, x2, y2 + 1, 1, second + 1)
	if is_vertical == 1 :
		if spindle == 0 :
			result = (x1, y1, x1 + 1, y1, 0, second + 1)
		if spindle == 1:
			result = (x2 - 1, y2, x2, y2, 0, second + 1)
	return result

def check_rotation(board, cur_pos, is_vertical, n, spindle, visited) :
	x1, y1, x2, y2 = cur_pos

	if is_vertical == 0 :
		if spindle == 0 :
			x, y = x1, y1
			if x + 1 < n and y > 0 and board[y - 1][x + 1] == 0 and board[y - 1][x] == 0 and \
			1 not in visited[y - 1][x]:
				return True
		if spindle == 1 :
			x, y = x2, y2
			if x > 0 and y + 1 < n and board[y + 1][x - 1] == 0 and board[y + 1][x] == 0 and \
				1 not in visited[y][x]:
				return True
	if is_vertical == 1 :
		if spindle == 0:
			x, y = x1, y1
			if y + 1 < n and x + 1 < n and board[y][x + 1] == 0 and board[y + 1][x + 1] == 0 and \
				0 not in visited[y][x]:
				return True
		if spindle == 1:
			x, y = x2, y2
			if x > 0 and y > 0 and board[y][x - 1] == 0 and board[y - 1][x - 1] == 0 and \
				0 not in visited[y][x - 1]:
				return True
	return False


# 시계방향
def rev_rotation (board, cur_pos, is_vertical, second, spindle) :
	x1, y1, x2, y2 = cur_pos
	if is_vertical == 0 :
		if spindle == 0 :
			result = (x1, y1, x1, y1 + 1, 1, second + 1)
		if spindle == 1:
			result = (x2, y2 - 1, x2, y2, 1, second + 1)
	if is_vertical == 1 :
		if spindle == 0 :
			result = (x1 - 1, y1, x1, y1, 0, second + 1)
		if spindle == 1:
			result = (x2, y2, x2 + 1, y2, 0, second + 1)
	return result

def check_rev_rotation(board, cur_pos, is_vertical, n, spindle, visited) :
	x1, y1, x2, y2 = cur_pos

	if is_vertical == 0 :
		if spindle == 0 :
			x, y = x1, y1
			if x + 1 < n and y + 1 < n and board[y + 1][x] == 0 and board[y + 1][x + 1] == 0 and \
			1 not in visited[y][x]:
				return True
		if spindle == 1 :
			x, y = x2, y2
			if x > 0 and y > 0 and board[y - 1][x] == 0 and board[y - 1][x - 1] == 0 and \
				1 not in visited[y - 1][x]:
				return True
	if is_vertical == 1 :
		if spindle == 0:
			x, y = x1, y1
			if y + 1 < n and x > 0 and board[y + 1][x - 1] == 0 and board[y][x - 1] == 0 and \
				0 not in visited[y][x - 1]:
				return True
		if spindle == 1:
			x, y = x2, y2
			if x + 1 < n and y > 0 and board[y][x + 1] == 0 and board[y - 1][x + 1] == 0 and \
				0 not in visited[y][x]:
				return True
	return False

def solution(board) :
	n = len(board)
	queue = deque()
	queue.append((0, 0, 1, 0, 0, 0))
	result = []
	visited = [[[] for _ in range(n)] for _ in range(n)]

	while queue :
		l_x, l_y, r_x, r_y, is_vertical, second = queue.popleft()
		#print((l_x, l_y, r_x, r_y, is_vertical, second))

		if (l_x == n - 1 and l_y == n - 1) or (r_x == n - 1 and r_y == n - 1) :
			result.append(second)
			continue
		if l_x < 0 or r_x < 0 or l_y >= n or r_y >= n :
			continue
		if is_vertical in visited[l_y][l_x] :
			continue

		visited[l_y][l_x].append(is_vertical)

		if is_vertical == 1:
			#move left
			if l_x > 0 and r_x > 0 and board[l_y][l_x - 1] == 0 and board[r_y][r_x - 1] == 0 and \
				is_vertical not in visited[l_y][l_x - 1] :
				#print("left", end=", ")
				queue.append((l_x - 1, l_y, r_x - 1, r_y, is_vertical, second + 1))
			#move right
			if l_x + 1 < n and r_x + 1 < n and board[l_y][l_x + 1] == 0 and board[r_y][r_x + 1] == 0 and \
				is_vertical not in visited[l_y][l_x + 1] :
				#print("right", end=", ")
				queue.append((l_x + 1, l_y, r_x + 1, r_y, is_vertical, second + 1))
			#move up
			if l_y > 0 and board[l_y - 1][l_x] == 0:
				if is_vertical not in visited[l_y - 1][l_x] :
					#print("up", end=", ")
					queue.append((l_x, l_y - 1, l_x, l_y, is_vertical, second + 1))
			#move down
			if r_y + 1 < n and board[r_y + 1][r_x] == 0:
				if is_vertical not in visited[r_y][l_x] :
					#print("down", end=", ")
					queue.append((r_x, r_y, r_x, r_y + 1, is_vertical, second + 1))

		if is_vertical == 0:
			#move left
			if l_x > 0 and board[l_y][l_x - 1] == 0:
				if is_vertical not in visited[l_y][l_x - 1] :
					#print("left", end=", ")
					queue.append((l_x - 1, l_y, l_x, l_y, is_vertical, second + 1))
			#move right
			if r_x + 1 < n and board[r_y][r_x + 1] == 0:
				if is_vertical not in visited[l_y][l_x + 1] :
					#print("right", end=", ")
					queue.append((r_x, r_y, r_x + 1, r_y, is_vertical, second + 1))
			#move up
			if l_y > 0 and r_y > 0 and board[l_y - 1][l_x] == 0 and board[r_y - 1][r_x] == 0 and \
				is_vertical not in visited[l_y - 1][l_x] :
				#print("up", end=", ")
				queue.append((l_x, l_y - 1, r_x, r_y - 1, is_vertical, second + 1))
			#move down
			if l_y + 1 < n and r_y + 1 < n and board[l_y + 1][l_x] == 0 and board[r_y + 1][r_x] == 0 and \
				is_vertical not in visited[l_y + 1][l_x] :
				#print("down", end=", ")
				queue.append((l_x, l_y + 1, r_x, r_y + 1, is_vertical, second + 1))

		cur_pos = (l_x, l_y, r_x, r_y)
		#rotate left position
		if check_rotation(board, cur_pos, is_vertical, n, 0, visited) :
			#print("rot for left", end=", ")
			queue.append(rotation(board, cur_pos, is_vertical, second, 0))
		#rotate right positon
		if check_rotation(board, cur_pos, is_vertical, n, 1, visited) :
			#print("rot for right", end=", ")
			queue.append(rotation(board, cur_pos, is_vertical, second, 1))
		#rev_rotate left position
		if check_rev_rotation(board, cur_pos, is_vertical, n, 0, visited) :
			#print("rev_rot for left", end=", ")
			queue.append(rev_rotation(board, cur_pos, is_vertical, second, 0))
		#rev_rotate right positon
		if check_rev_rotation(board, cur_pos, is_vertical, n, 1, visited) :
			#print("rev_rot for right", end=", ")
			queue.append(rev_rotation(board, cur_pos, is_vertical, second, 1))
		#print()

	answer = min(result)
	return answer

for testcase in testcases :
	print(solution(testcase))
