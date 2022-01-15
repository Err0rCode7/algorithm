from collections import deque
import sys

input = sys.stdin.readline

t = int(input())

def is_end(x, y, r, c):
	return x == 0 or y == 0 or x == c - 1 or y == r - 1

def get_cost(vistied_other, board, x, y):
	if vistied_other[y][x] != 10000:
		return 0
	elif board[y][x] == '#':
		return 1
	return 0

for i in range(t):
	r, c = map(int, input().rstrip().split())
	board = []
	prisoner = []
	for y in range(r):
		line = input().rstrip()
		board.append(line)
		for x in range(c):
			if line[x] == '$':
				prisoner.append((x, y))
	visited_A = [[10000 for _ in range(c)] for _ in range(r)]
	visited_B = [[10000 for _ in range(c)] for _ in range(r)]
	delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
	q = deque()
	q.append((prisoner[0], prisoner[1], 0))
	result = 100 * 100
	visited_A[prisoner[0][1]][prisoner[0][0]] = 0
	visited_B[prisoner[1][1]][prisoner[1][0]] = 0
	while q:
		A, B, cost = q.popleft()
		ax, ay = A
		bx, by = B
		A_end = False
		B_end = False
		print(A, B, q)
		if is_end(ax, ay, r, c) and is_end(bx, by, r, c):
			result = min(result, cost)
			continue
		elif is_end(ax, ay, r, c):
			A_end = True
		elif is_end(bx, by, r, c):
			B_end = True
		visit_list = []
		if not A_end:
			for i in range(4):
				adx, ady = delta[i]
				nax, nay = ax + adx, ay + ady
				
				if board[nay][nax] == '*':
					continue
				add_A = get_cost(visited_B, board, nax, nay)
				if visited_A[nay][nax] < cost + add_A:
					continue
				if not B_end:
					for j in range(4):
						bdx, bdy = delta[j]
						nbx, nby = bx + bdx, by + bdy

						if board[nby][nbx] == '*':
							continue
						add_B = get_cost(visited_A, board, nbx, nby)
						
						if visited_B[nby][nbx] < cost + add_B:
							continue
						minus = 0
						if nax == nbx and nay == nby and board[nay][nax] == '#':
							minus += 1
						visit_list.append((nax, nay, nbx, nby, add_A, add_B))
						q.append(((nax, nay), (nbx, nby), cost + add_A + add_B - minus))
				else:
					if visited_A[nay][nax] < cost + add_A:
						continue
					visited_A[nay][nax] = cost + add_A
					q.append(((nax, nay), (bx, by), cost + add_A))
		else :
			for j in range(4):
				bdx, bdy = delta[j]
				nbx, nby = bx + bdx, by + bdy
				if board[nby][nbx] == '*' :
					continue
				add = get_cost(visited_A, board, nbx, nby)
				if visited_B[nby][nbx] < cost + add:
					continue
				visited_B[nby][nbx] = cost + add
				q.append(((ax, ay), (nbx, nby), cost + add))
		for x1, y1, x2, y2, cost_A, cost_B in visit_list:
			visited_A[y1][x1] = cost_A
			visited_B[y2][x2] = cost_B
	print(result)