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

	def check_sync(x, y, tx, ty, table, game_board):
		for i in range(4):
			nx, ny = x + dx[i], y + dy[i]
			ntx, nty = tx + dx[i], ty + dy[i]
			# print("sync", nx, ny, ntx, nty)
			if not is_safe_point(nx, ny) and is_safe_point(ntx, nty):
				if table[nty][ntx] != 0:
					return False
			elif is_safe_point(nx, ny) and not is_safe_point(ntx, nty):
				if game_board[ny][nx] != 1:
					return False
			if is_safe_point(nx, ny) and is_safe_point(ntx, nty):
				if not((game_board[ny][nx] <= 0 and table[nty][ntx] != 0) or (game_board[ny][nx] == 1 and table[nty][ntx] == 0)):
					return False
		return True

	q = deque()
	q.append((x, y, tx, ty))
	table_visited = [[False] * len(game_board) for _ in range(len(game_board))]
	game_visited = [[False] * len(game_board) for _ in range(len(game_board))]
	# for i in table:
	# 	print(i)
	# print()
	# for i in game_board:
	# 	print(i)
	size = 0
	while q :
		# print(q[0])
		x, y, tx, ty= q.popleft()
		size += 1
		game_board[y][x] = -1
		if not check_sync(x, y, tx, ty, table, game_board):
			return (False, size)
		for i in range(4):
			nx, ny = x + dx[i], y + dy[i]
			ntx, nty = tx + dx[i], ty + dy[i]
			# print("new", nx, ny, ntx, nty)
			if is_safe_point(nx, ny) and is_safe_point(ntx, nty) and not table_visited[nty][ntx] and not game_visited[ny][nx] and \
				game_board[ny][nx] == 0 and table[nty][ntx] != 0:
				table_visited[nty][ntx] = True
				game_visited[ny][nx] = True
				q.append((nx, ny, ntx, nty))
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
					result.append((j, i, table[i][j]))
					blocks.add(table[i][j])
		# print(table)
		return result

	def get_rotated_table(table):
		n = len(table)
		new = deepcopy(table)
		for i in range(n):
			for j in range(n):
				new[j][n - i - 1] = table[i][j]
		return new

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
	new_table = table
	for i in range(4):
		tables.append(new_table)
		table_blocks.append(find_block(tables[i]))
		new_table = get_rotated_table(new_table)

	def delete_used_block(table_blocks_list, block):
		for table_blocks in table_blocks_list:
			for i in range(len(table_blocks)):
				x, y, value = table_blocks[i]
				if value == block:
					table_blocks.remove(table_blocks[i])
					break

	def select_block(x, y, game_board, table_blocks):
		answer = 0
		for i in range(4):
			table = tables[i]
			for tx, ty, table_value in table_blocks[i]:
				temp_game_board = deepcopy(game_board)
				result, size = bfs(x, y, temp_game_board, table, tx, ty)
				# print(result, size)
				if result:
					delete_used_block(table_blocks, table_value)
					return (size, temp_game_board)

		return (answer, 0)

	answer = 0
	for y in range(n):
		for x in range(n):
			if game_board[y][x] == 0:
				size, new_game_board = select_block(x, y, game_board, table_blocks)
				# print(size)
				if size > 0:			
					game_board = new_game_board
					answer += size

	# for b in game_board:
	# 	print(b)
	return answer

print(solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]	, [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]	))
print(solution([[0,0,0],[1,1,0],[1,1,1]]	, [[1,1,1],[1,0,0],[0,0,0]]	))