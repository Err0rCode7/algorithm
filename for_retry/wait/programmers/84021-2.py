from collections import deque
from copy import deepcopy

def solution(game_board, table):

	def in_safe(x, y, n):
		return 0 <= x < n and 0 <= y < n

	def bfs(table, x, y, src, dest):
		# 위상을 key에 저장
		key = [(0, 0)]
		q = deque()
		q.append([x, y, 0, 0])
		table[y][x] = dest
		while q:
			x, y, rx, ry = q.popleft()

			for dx, dy in [(1,0), (0, 1), (-1, 0), (0, -1)]:
				nx, ny = x + dx, y + dy
				nrx, nry = rx + dx, ry + dy
				if in_safe(nx, ny, len(table)) and table[ny][nx] == src:
					key.append((nrx, nry))
					table[ny][nx] = dest
					q.append([nx, ny, nrx, nry])
		return sorted(key)

	def find_blocks(table, src, dest):
		pos_set = []
		for i in range(len(table)):
			for j in range(len(table)):
				if table[i][j] == src:
					pos_set.append(bfs(table, j, i, src, dest))

		return pos_set

	def get_rotate_table(table):
		new_table = [[0] * len(table) for _ in range(len(table))]

		for y in range(len(table)):
			for x in range(len(table)):
				new_table[x][len(table) - y - 1] = table[y][x]
		return new_table

	def select_block(table, table_copy, pos_set):
		result = 0
		for y in range(len(table)):
			for x in range(len(table)):
				if table_copy[y][x] == 1:
					move = bfs(table_copy, x, y, 1, 0)
					if move in pos_set: # 블록이 있으면
						result += len(move)
						pos_set.remove(move)
						table = deepcopy(table_copy)
					else : # 블록이 없으면
						# 테이블 원상복구
						table_copy = deepcopy(table)
		return (result, table)

	copy_game_board = deepcopy(game_board)
	game_blocks_set = find_blocks(copy_game_board, 0, 1)

	answer = 0
	for i in range(4):
		table = get_rotate_table(table)
		table_for_search = deepcopy(table)
		# 알맞은 블록 선택, 선택후 블록은 제거됨
		result, updated_table = select_block(table, table_for_search, game_blocks_set)
		answer += result
		table = updated_table
	return answer

print(solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]	, [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]	))