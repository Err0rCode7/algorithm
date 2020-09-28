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
#print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))
#print(solution([[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 1], [0, 0, 1, 0, 0, 0, 0]]))
print(solution([[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 0]]))
#print(solution([[0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0]]))
