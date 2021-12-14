from collections import deque

def solution(board, r, c):

	# BFS
	# 상하좌우 + 컨트롤 상하좌우
	dx = [1, 0, -1, 0]
	dy = [0, 1, 0, -1]

	# x, y, card, deleted, move
	q = deque()
	q.append((c, r, board[r][c], set(), 0))
	visited = [[[int(1e3), 0] for _ in range(4)] for _ in range(4)]

	def get_direction(deleted, x, y, board):

		def is_safe(x, y):
			return 0 <= x < 4 and 0 <= y < 4

		result = set()

		for i in range(4):
			nx, ny = x + dx[i], y + dy[i]
			if is_safe(nx, ny):
				result.add((nx, ny))
			nx, ny = nx + dx[i], ny + dy[i]
			while is_safe(nx,ny):
				# 카드가 있을 때
				if board[ny][nx] != 0 and board[ny][nx] not in deleted:
					result.add((nx, ny))
					break
				nx, ny = nx + dx[i], ny + dy[i]
			if not is_safe(nx, ny):
				nx, ny = nx - dx[i], ny - dy[i]
				# 카드가 존재하지 않을때
				if nx != x and ny != y:
					result.add((nx, ny))
		return result
	
	cards = set()
	for i in range(4):
		for j in range(4):
			if board[i][j] != 0:
				cards.add(board[i][j])
	_min = 16 * 3
	card_count = len(cards)
	while q :
		x, y, card, deleted, move = q.popleft()
		
		if visited[y][x][0] <= move and visited[y][x][1] >= len(deleted):
			continue
		if card == 0 and board[y][x] != card :
			card = board[y][x]

		visited[y][x][0] = move
		visited[y][x][1] = len(deleted)
		if len(deleted) == card_count:
			_min = min(_min, move)
			continue
		for nx, ny in get_direction(deleted, x, y, board):
			if board[ny][nx] != 0 and board[ny][nx] not in deleted:
				if board[ny][nx] == card:
					print(x, y, nx, ny, move, visited[y][x], deleted)
					new_set = set(deleted)
					new_set.add(card)
					card = 0
					q.append((nx, ny, 0, new_set, move + 1))
				else:
					q.append((nx, ny, card, deleted, move + 1))
			else :
				q.append((nx, ny, card, deleted, move + 1))

	answer = _min + 2 * card_count
	return answer

print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1, 0))