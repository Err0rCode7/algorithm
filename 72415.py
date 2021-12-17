

def solution(board, r, c):

	dx = [1, 0, -1 ,0]
	dy = [0, 1, 0, -1]
	n = len(board)
	def is_safe_point(x, y):
		return 0 <= x < n and 0 <= y < n

	def find_dist_dfs(sx, sy, tx, ty, cost, visited):

		if tx == sx and ty == sy:
			return cost
		_min = n * n + n
		for i in range(4):
			nx, ny = sx + dx[i], sy + dy[i]
			if not is_safe_point(nx, ny):
				if not visited[ny][nx]:
					visited[ny][nx] = True
					find_dist_dfs(nx, ny, tx, ty, cost + 1, visited)
					visited[ny][nx] = False
				nx, ny = sx + dx[i], sy + dy[i]
				move = False
				while is_safe_point(nx, ny):
					if board[ny][nx] != 0:
						visited[ny][nx] = True
						find_dist_dfs(nx, ny, tx, ty, cost + 1, visited)
						visited[ny][nx] = False
						move = True
						break
					nx, ny = sx + dx[i], sy + dy[i]
				if not move and not is_safe_point(nx, ny):
					nx, ny = nx - dx[i], ny - dy[i]
					visited[ny][nx] = True
					find_dist_dfs(nx, ny, tx, ty, cost + 1, visited)
					visited[ny][nx] = False
	answer = 0
	return answer