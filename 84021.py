from collections import deque
from copy import deepcopy

def is_safe_point(x, y, n):
	return 0 <= x < n and 0 <= y < n

def bfs(x, y, game_board, table, tx, ty):
	dx = [1, 0, -1, 0]
	dy = [0, 1, 0, -1]
	n = len(table)
	def is_safe_point(x, y):
		return 0 <= x < n and 0 <= y < n

	def check_sync(x, y, tx, ty, table, game_board): # pre_dir == (i + 2) % 4
		for i in range(4):
			nx, ny = x + dx[i], y + dy[i]
			ntx, nty = tx + dx[i], ty + dy[i]
			if is_safe_point(nx, ny) != is_safe_point(ntx, nty):
				return False
			if is_safe_point(nx, ny) and is_safe_point(ntx, nty):
				if not((game_board[ny][nx] == 0 and table[nty][ntx] != 0) or (game_board[ny][nx] == 1 and table[nty][ntx] == 0)):
					return False
		return True

	q = deque()
	q.append((x, y, tx, ty, 0))
	table_visited = [[False] * len(game_board) for _ in range(len(game_board))]
	game_visited = [[False] * len(game_board) for _ in range(len(game_board))]

	while q :
		print(q[0])
		x, y, tx, ty, size = q.popleft()
		if not check_sync(x, y, tx, ty, table, game_board):
			return (False, size)
		for i in range(4):
			nx, ny = x + dx[i], y + dy[i]
			ntx, nty = tx + dx[i], ty + dy[i]
			if is_safe_point(nx, ny) and is_safe_point(ntx, nty) and not table_visited[nty][ntx] and not game_visited[ny][nx] and \
				game_board[ny][nx] == 0 and table[nty][ntx] != 0:
				table_visited[nty][ntx] = True
				game_visited[ny][nx] = True
				game_board[ny][nx] = 1
				q.append((nx, ny, ntx, nty, size + 1))
	return (True, size)

def dfs(x, y, value, n, table):
	dx = [1, 0, -1, 0]
	dy = [0, 1, 0, -1]

	table[y][x] = value
	for i in range(4):
		nx, ny = x + dx[i], y + dy[i]
		if is_safe_point(nx, ny, n) and table[ny][nx] == 1:
			dfs(nx, ny, value, n, table)

def solution(game_board, table):
	
	n = len(table)
	def find_block(table):
		blocks = set()
		result = []
		for i in range(n):
			for j in range(n):
				if table[i][j] != 0 and table[i][j] not in blocks:
					# print(j, i, table[i][j])
					result.append((j, i, table[i][j]))
					blocks.add(table[i][j])
		return result

	def rotate_table(table):
		n = len(table)

		for i in range(n):
			for j in range(n):
				table[j][n - i - 1] = table[i][j]

	def set_block_value(table):
		count = 2
		for i in range(n):
			for j in range(n):
				if table[i][j] == 1:
					dfs(j, i, count, len(table), table)
					count += 1

	set_block_value(table)
	tables = []
	table_blocks = []
	for i in range(4):
		new_table = deepcopy(table)
		tables.append(new_table)
		table_blocks.append(find_block(tables[i]))
		rotate_table(table)

	def delete_used_block(table_blocks, block):
		for table_block in table_blocks:
			table_block[i].remove(block)
	print(table_blocks)
	answer = 0
	for y in range(n):
		for x in range(n):
			if game_board[y][x] == 0:
				temp_game_board = deepcopy(game_board)
				for i in range(4):
					table = tables[i]
					for tx, ty, table_value in table_blocks[i]:
						result, size = bfs(x, y, temp_game_board, table, tx, ty)
						print(result, size)
						if result:
							answer += size
							delete_used_block(table_blocks, table_value)
							game_board = temp_game_board

	return answer

print(solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]	, [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]	))