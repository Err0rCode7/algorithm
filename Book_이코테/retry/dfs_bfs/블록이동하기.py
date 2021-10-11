
## 실패한 코드 DFS는 적합하지 않았던 문제
## 최소 시간을 구할 때에는 BFS를 이용하자.

##	DFS 실패한 코드 : 93점 ##

'''
import sys

sys.setrecursionlimit(10000)

# status, point1, point2

def dfs(robot, board, N, result, visited):

	status, point1, point2, time = robot
	y1, x1 = point1
	y2, x2 = point2
	if (x2 == N - 1 and y2 == N - 1) or (x1 == N - 1 and y1 == N - 1):
		result[0] = min(result[0], time)
		return

	# 가로
	if status == 0:
		if N > x2 + 1 >= 0:
			if board[y2][x2 + 1] == 0:
				# 오른쪽으로 이동
				if visited[0][y1][x1 + 1] == 0 or visited[0][y1][x1 + 1] > time + 1:
					visited[0][y1][x1 + 1] = time + 1
					n_robot = ((0, (y1, x1 + 1), (y2, x2 + 1), time + 1))
					dfs(n_robot, board, N, result, visited)
		if N > x1 - 1 >= 0:
			if board[y1][x1 - 1] == 0:
				# 왼쪽으로 이동
				if visited[0][y1][x1 - 1] == 0 or visited[0][y1][x1 - 1] > time + 1:
					visited[0][y1][x1 - 1] = time + 1
					n_robot = ((0, (y1, x1 - 1), (y2, x2 - 1), time + 1))
					dfs(n_robot, board, N, result, visited)
		if N > y1 + 1 >= 0:
			if board[y1 + 1][x1] == 0 and board[y1 + 1][x1 + 1] == 0:
				# 아래로 이동
				if visited[0][y1 + 1][x1] == 0 or visited[0][y1 + 1][x1] > time + 1:
					visited[0][y1 + 1][x1] = time + 1
					n_robot = ((0, (y1 + 1, x1), (y2 + 1, x2), time + 1))
					dfs(n_robot, board, N, result, visited)
				# 회전
				if visited[1][y1][x1] == 0 or visited[1][y1][x1] > time + 1:
					visited[1][y1][x1] = time + 1
					n_robot = ((1, (y1, x1), (y1 + 1, x1), time + 1))
					dfs(n_robot, board, N, result, visited)
				if visited[1][y2][x2] == 0 or visited[1][y2][x2] > time + 1:
					visited[1][y2][x2] = time + 1
					n_robot = ((1, (y2, x2), (y2 + 1, x2), time + 1))
					dfs(n_robot, board, N, result, visited)
		if N > y1 - 1 >= 0:
			if board[y1 - 1][x1] == 0 and board[y1 - 1][x1 + 1] == 0:
				# 위로 이동
				if visited[0][y1 - 1][x1] == 0 or visited[0][y1 - 1][x1] > time + 1:
					visited[0][y1 - 1][x1] = time + 1
					n_robot = ((0, (y1 - 1, x1), (y2 - 1, x2), time + 1))
					dfs(n_robot, board, N, result, visited)
				# 회전
				if visited[1][y1 - 1][x1] == 0 or visited[1][y1 - 1][x1] > time + 1:
					visited[1][y1 - 1][x1] = time + 1
					n_robot = ((1, (y1 - 1, x1), (y1, x1), time + 1))
					dfs(n_robot, board, N, result, visited)
				if visited[1][y2 - 1][x2] == 0 or visited[1][y2 - 1][x2] > time + 1:
					visited[1][y2 - 1][x2] = time + 1
					n_robot = ((1, (y2 - 1, x2), (y2, x2), time + 1))
					dfs(n_robot, board, N, result, visited)
	# 세로
	elif status == 1:
		if N > y1 - 1 >= 0:
			if board[y1 - 1][x1] == 0:
				# 위로이동
				if visited[1][y1 - 1][x1] == 0 or visited[1][y1 - 1][x1] > time + 1:
					visited[1][y1 - 1][x1] = time + 1
					n_robot = ((1, (y1 - 1, x1), (y2 - 1, x2), time + 1))
					dfs(n_robot, board, N, result, visited)
		if N > y2 + 1 >= 0:
			if board[y2 + 1][x2] == 0:
				# 아래로 이동
				if visited[1][y1 + 1][x2] == 0 or visited[1][y1 + 1][x2] > time + 1:
					visited[1][y1 + 1][x2] = time + 1
					n_robot = ((1, (y1 + 1, x1), (y2 + 1, x2), time + 1))
					dfs(n_robot, board, N, result, visited)
		if N > x1 - 1 >= 0:
			if board[y1][x1 - 1] == 0 and board[y2][x2 - 1] == 0:
				# 왼쪽으로 이동
				if visited[1][y1][x1 - 1] == 0 or visited[1][y1][x1 - 1] > time + 1:
					visited[1][y1][x1 - 1] = time + 1
					n_robot = ((1, (y1, x1 - 1), (y2, x2 - 1), time + 1))
					dfs(n_robot, board, N, result, visited)
				# 회전
				if visited[0][y1][x1 - 1] == 0 or visited[0][y1][x1 - 1] > time + 1:
					visited[0][y1][x1 - 1] = time + 1
					n_robot = ((0, (y1, x1 - 1), (y1, x1), time + 1))
					dfs(n_robot, board, N, result, visited)
				if visited[0][y2][x2 - 1] == 0 or visited[0][y2][x2 - 1] > time + 1:
					visited[0][y2][x2 - 1] = time + 1
					n_robot = ((0, (y2, x2 - 1), (y2, x2), time + 1))
					dfs(n_robot, board, N, result, visited)
		if N > x1 + 1 >= 0 :
			if board[y1][x1 + 1] == 0 and board[y2][x2 + 1] == 0:
				# 오른쪽으로 이동
				if visited[1][y1][x1 + 1] == 0 or visited[1][y1][x1 + 1] > time + 1:
					visited[1][y1][x1 + 1] = time + 1
					n_robot = ((1, (y1, x1 + 1), (y2, x2 + 1), time + 1))
					dfs(n_robot, board, N, result, visited)
				# 회전
				if visited[0][y1][x1] == 0 or visited[0][y1][x1] > time + 1:
					visited[0][y1][x1] = time + 1
					n_robot = ((0, (y1, x1), (y1, x1 + 1), time + 1))
					dfs(n_robot, board, N, result, visited)
				if visited[0][y2][x2] == 0 or visited[0][y2][x2] > time + 1:
					visited[0][y2][x2] = time + 1
					n_robot = ((0, (y2, x2), (y2, x2 + 1), time + 1))
					dfs(n_robot, board, N, result, visited)


def solution(board) :

	status = 0
	y1, x1 = 0, 0
	y2, x2 = 0, 1

	# 0 이동가능, 1 벽, 2 이미 이동
	N = len(board)

	visited = [[[0] * N for _ in range(N)] for _ in range(2)]

	result = [1e10]
	visited[0][y1][x1] = 1
	# 상태, 좌표1, 좌표2, 시간
	robot = (status, (y1,x1), (y2, x2), 0)
	dfs(robot, board, N, result, visited)
	return(result[0])

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))

'''

##	BFS 성공한 코드 : 100점 ##

from collections import deque
import copy
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def solution(board) :
	queue = deque()
	_min = int(1e9)
	# x, y, is_vertical
	n = len(board)
	visited = [[0 for _ in range(n)] for _ in range(n)]
	vt_visited = [[0 for _ in range(n)] for _ in range(n)]
	queue.append((0, 0, 0, 0))
	visited[0][0] = True
	while queue :
		x, y, is_vertical, count = queue.popleft()
		# (n, n)
		if is_vertical :
			rx, ry = x, y + 1
		else :
			rx, ry = x + 1, y
		if (x == n - 1 and y == n - 1) or (rx == n - 1 and ry == n - 1):
			_min = min(_min, count)
			continue
		# move
		for i in range(4) :
			nx, ny = x + dx[i], y + dy[i]
			nrx, nry = rx + dx[i], ry + dy[i]
			if nx < 0 or ny < 0 or nx >= n or ny >= n or \
				nrx < 0 or nry < 0 or nrx >= n or nry >= n:
				continue
			if is_vertical :
				if board[ny][nx] == 0 and board[nry][nrx] == 0 and (vt_visited[ny][nx] == 0 or vt_visited[ny][nx] > count + 1):
					vt_visited[ny][nx] = count + 1
					queue.append((nx, ny, is_vertical, count + 1))
			else :
				if board[ny][nx] == 0 and board[nry][nrx] == 0 and (visited[ny][nx] == 0 or visited[ny][nx] > count + 1):
					visited[ny][nx] = count + 1
					queue.append((nx, ny, is_vertical, count + 1))
		# rotate
		if is_vertical :
			# select left side of robot
			# clock wise
			nx, ny = x - 1, y
			if nx >= 0 and board[ny][nx] == 0 and board[ny + 1][nx] == 0 and (visited[ny][nx] == 0 or visited[ny][nx] > count + 1):
				visited[ny][nx] = count + 1
				queue.append((nx, ny, 0, count + 1))
			# reverse clock wise
			nx, ny = x, y
			if nx < n - 1 and board[ny + 1][nx + 1] == 0 and \
				board[ny][nx + 1] == 0 and (visited[ny][nx] == 0 or visited[ny][nx] > count + 1):
				visited[ny][nx] = count + 1
				queue.append((nx, ny, 0, count + 1))
			# select right side of robot
			# clock wise
			nx, ny = x, y + 1
			if nx < n - 1 and board[ny - 1][nx + 1] == 0 and \
				board[ny][nx + 1] == 0 and (visited[ny][nx] == 0 or visited[ny][nx] > count + 1):
				visited[ny][nx] = count + 1
				queue.append((nx, ny, 0, count + 1))
			# reverse clock wise
			nx, ny = x - 1, y + 1
			if nx >= 0 and board[ny][nx] == 0 and board[ny - 1][nx] == 0 and (visited[ny][nx] == 0 or visited[ny][nx] > count + 1):
				visited[ny][nx] = count + 1
				queue.append((nx, ny, 0, count + 1))
		else :
			# select left side of robot
			# clock wise
			nx, ny = x, y
			if ny < n - 1 and board[ny + 1][nx] == 0 and \
				board[ny + 1][nx + 1] == 0 and (vt_visited[ny][nx] == 0 or vt_visited[ny][nx] > count + 1):
				vt_visited[ny][nx] = count + 1
				queue.append((nx, ny, 1, count + 1))
			# reverse clock wise
			nx, ny = x, y - 1
			if ny >= 0 and board[ny][nx] == 0 and board[ny][nx + 1] == 0 and (vt_visited[ny][nx] == 0 or vt_visited[ny][nx] > count + 1):
				vt_visited[ny][nx] = count + 1
				queue.append((nx, ny, 1, count + 1))
			# select right side of robot
			# clock wise
			nx, ny = x + 1, y - 1
			if ny >= 0 and board[ny][nx - 1] == 0 and board[ny][nx] == 0 and (vt_visited[ny][nx] == 0 or vt_visited[ny][nx] > count + 1):
				vt_visited[ny][nx] = count + 1
				queue.append((nx, ny, 1, count + 1))
			# reverse clock wise
			nx, ny = x + 1, y
			if ny < n - 1 and board[ny + 1][nx - 1] == 0 and \
				board[ny + 1][nx] == 0 and (vt_visited[ny][nx] == 0 or vt_visited[ny][nx] > count + 1):
				vt_visited[ny][nx] = count + 1
				queue.append((nx, ny, 1, count + 1))
	return(_min)


