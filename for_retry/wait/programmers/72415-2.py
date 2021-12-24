from collections import deque
import heapq, sys
sys.setrecursionlimit(10000)

def solution(board, r, c):

	dx = [1, 0, -1, 0]
	dy = [0, 1, 0, -1]
	n = len(board)
	def in_safe(x, y):
		return 0 <= x < n and 0 <= y < n
	
	# BFS
	def smallest_from_a_to_b(ax, ay, bx, by, board):
		# print(ax, ay, bx, by)
		dist = [[int(1e9)] * len(board) for _ in range(len(board))]
		dist[ay][ax] = 0
		q = deque([(0, ax, ay)])
		result = int(1e9)
		while q :
			cost, x, y = q.popleft()
			if x == bx and y == by:
				result = min(result, cost)
				continue

			for i in range(4):
				ex, ey = x, y
				move = 0
				while in_safe(ex + dx[i], ey + dy[i]):
					ex, ey = ex + dx[i], ey + dy[i]
					move += 1
					if board[ey][ex] != 0:
						break
					if move == 1 and dist[ey][ex] > cost + 1:
						dist[ey][ex] = cost + 1
						q.append((cost + 1, ex ,ey))
				if board[ey][ex] != 0 and dist[ey][ex] > cost + 1:
					dist[ey][ex] = cost + 1
					q.append((cost + 1, ex ,ey))
					continue
				if move > 1 and board[ey][ex] == 0 and dist[ey][ex] > cost + 1:
					dist[ey][ex] = cost + 1
					q.append((cost + 1, ex ,ey))
		return result
	# 다익스트라
	# def smallest_from_a_to_b(ax, ay, bx, by, board):
	# 	# print(ax, ay, bx, by)
	# 	dist = [[int(1e9)] * len(board) for _ in range(len(board))]
	# 	dist[ay][ax] = 0
	# 	heap = [(0, ax, ay)]

	# 	while heap:
	# 		cost, x, y = heapq.heappop(heap)

	# 		if x == bx and y == by:
	# 			return cost
			
	# 		if dist[y][x] < cost:
	# 			continue
			
	# 		for v in range(4):
	# 			ex, ey = x, y
	# 			move = 0
	# 			while in_safe(ex + dx[v], ey + dy[v]) :
	# 				ex, ey = ex + dx[v], ey + dy[v]
	# 				move += 1
	# 				if board[ey][ex] != 0:
	# 					break
	# 				if dist[ey][ex] > cost + move:
	# 					dist[ey][ex] = cost + move
	# 					heapq.heappush(heap, (cost + mve, ex, ey))

	# 			if dist[ey][ex] > cost + 1:
	# 				dist[ey][ex] = cost + 1
	# 				heapq.heappush(heap, (cost + 1, ex, ey))

	def get_card_pos(board, card):
		result = []
		for y in range(4):
			for x in range(4):
				if board[y][x] == card:
					result.append((x, y))
		return result

	def is_end():
		for i in range(4):
			for j in range(4):
				if board[i][j] != 0:
					return False
		return True

	def card_dfs(x, y):
		if is_end():
			return 0

		result = int(1e9)
		for card in range(1, 7):

			cards_pos = get_card_pos(board, card)
			if len(cards_pos) != 2:
				continue
			first = cards_pos[0]
			second = cards_pos[1]

			dist_to_second = smallest_from_a_to_b(x, y, first[0], first[1], board) + smallest_from_a_to_b(first[0], first[1], second[0], second[1], board) + 2
			dist_to_first = smallest_from_a_to_b(x, y, second[0], second[1], board) + smallest_from_a_to_b(second[0], second[1], first[0], first[1], board) + 2
			board[first[1]][first[0]] = 0
			board[second[1]][second[0]] = 0

			result = min(dist_to_first + card_dfs(first[0], first[1]), dist_to_second + card_dfs(second[0], second[1]), result)

			board[first[1]][first[0]] = card
			board[second[1]][second[0]] = card

		return result

	answer = card_dfs(c, r)
	return answer

print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]]	, 1, 0))