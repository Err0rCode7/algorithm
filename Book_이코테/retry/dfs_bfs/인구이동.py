from collections import deque
import sys

sys.setrecursionlimit(10000)

input = sys.stdin.readline

N, L, R = map(int, input().rstrip().split())

board = []
union = [[0] * N for _ in range(N)]
for i in range(N):
	line = list(map(int, input().rstrip().split()))
	board.append(line)

def dfs(y, x, union, num, union_list):
	global N, L, R

	flag = False
	dx = [1, 0, -1, 0]
	dy = [0, 1, 0, -1]
	for i in range(4):
		ny, nx = y + dy[i], x + dx[i]
		if ny >= N or ny < 0 or nx >= N or nx < 0:
			continue
		if union[ny][nx] == 0 and \
			(L <= abs(board[y][x] - board[ny][nx]) <= R):
			union[ny][nx] = num
			if len(union_list[num - 1][1]) == 0:
				union_list[num - 1][0] += board[y][x]
				union_list[num - 1][1].append((y, x))
			union_list[num - 1][0] += board[ny][nx]
			union_list[num - 1][1].append((ny, nx))
			dfs(ny, nx, union, num, union_list)
			flag = True
	return (flag)

def move(union_list):
	flag = 0
	index = 1
	union = [[0] * N for _ in range(N)]
	for y in range(N):
		for x in range(N):
			if union[y][x] == 0:
				union_list.append([0,[]])
				union[y][x] = index
				if dfs(y, x, union, index, union_list):
					flag = 1
					index += 1
				else:
					union[y][x] = 0

	return (flag)

count = 0
while True:
	union_list = []
	if not move(union_list):
		break
	for _sum, points in union_list:
		len_points = len(points)
		if len_points == 0:
			break
		value = _sum // len_points
		for y, x in points:
			board[y][x] = value
	count += 1

print(count)

