import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n, l, r = map(int, input().split())

board = []
group_sum = []
group = []
for i in range(n) :
	row = list(map(int, input().split()))
	board.append(row)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
count = 0

def dfs(x, y, board) :
	global count, group_sum
	for i in range(4) :
		nx, ny = x + dx[i], y + dy[i]
		if nx < 0 or ny < 0 or nx >= n or ny >= n :
			continue
		elif l <= abs(board[y][x] - board[ny][nx]) <= r :
			if group[y][x] == 0 and group[ny][nx] != 0:
				count = group[ny][nx]
				print(count, group_sum)
				group_sum[count - 1][0] += board[y][x]
				group_sum[count - 1][1] += 1
				group[y][x] = group[ny][nx]
			elif group[y][x] == 0 and group[ny][nx] == 0 :
				count += 1
				group[y][x] = count
				group[ny][nx] = count
				group_sum.append([0, 0])
				group_sum[count - 1][0] += board[y][x]
				group_sum[count - 1][0] += board[ny][nx]
				group_sum[count - 1][1] += 2
			elif group[y][x] != 0 and group[ny][nx] == 0 :
				group_sum[count - 1][0] += board[ny][nx]
				group_sum[count - 1][1] += 1
				group[ny][nx] = group[y][x]
			else :
				continue
			dfs(nx, ny, board)

def process():
	global count, group_sum, group
	for i in range(2001) :
		count = 0
		group_sum = []
		group = [[0 for _ in range(n)] for _ in range(n)]
		# 국경 ON
		for y in range(n):
			for x in range(n) :
				if group[y][x] == 0 :
					dfs(x, y, board)
		if count == 0 :
			print(i)
			break
		for y in range(n) :
			for x in range(n) :
				if group[y][x] == 0 :
					continue
				board[y][x] = int(group_sum[group[y][x] - 1][0] / group_sum[group[y][x] - 1][1])
		# 국경 변화 X

process()
