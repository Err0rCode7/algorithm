
def solution(board):
	n = len(board)
	dist = [[[25 * 25 * 600 + 1, 25 * 25 * 600 + 1] for _ in range(n)] for _ in range(n)]

	from collections import deque

	def is_in_range(x, y):
		return 0 <= x < n and 0 <= y < n
	def is_curve(_dir, pre_dir):
		if pre_dir == -1 :
			return False
		if abs(_dir - pre_dir) == 2 or abs(_dir - pre_dir) == 0:
			return False
		return True

	q = deque()
	q.append((0, 0, 0, -1))
	dx = [1, 0, -1, 0]
	dy = [0, 1, 0, -1]
	dist[0][0] = [0, 0]
	while q:
		x, y, cost, pre_dir = q.popleft()
		# print("####", x, y, cost, pre_dir)
		if x == n - 1 and y == n - 1:
			continue
		for i in range(4):
			nx, ny = x + dx[i], y + dy[i]
			# print(x, y, nx, ny, i, pre_dir)
			if is_in_range(nx, ny) and board[ny][nx] == 0:
				if is_curve(i, pre_dir) and dist[ny][nx][1] >= cost + 600 :
					dist[ny][nx][1] = cost + 600
					q.append((nx, ny, cost + 600, i))
				elif not is_curve(i, pre_dir) and dist[ny][nx][0] >= cost + 100:
						
					dist[ny][nx][0] = cost + 100
					q.append((nx, ny, cost + 100, i))
	# for i in dist:
	# 	print(i)
	return min(dist[n - 1][n - 1])

# print(solution([[0,0,0],[0,0,0],[0,0,0]]	))
# print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]	))
# print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]	))
# print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]	))