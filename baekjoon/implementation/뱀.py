from collections import deque

n = int(input())
k = int(input())

board = [[0 for _ in range(n)] for _ in range(n)]

for i in range(k) :
	y, x = map(int, input().rstrip().split())
	board[y - 1][x - 1] = 2

l = int(input())
cmd = []
for i in range(l) :
	x, c = input().rstrip().split()
	x = int(x)
	if c == "L" :
		c = -1
	else :
		c = 1
	cmd.append((x,c))

i = 0;
cmd_index = 0;
board[0][0] = 1
x, y = 0, 0
tail = deque()
tail.append((0,0))
cur_dir = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
while True :

	if cmd_index < len(cmd) :
		second, direction = cmd[cmd_index]
	if i == second :
		cur_dir += direction
		cmd_index += 1
	if cur_dir < 0 :
		cur_dir += 4
	elif cur_dir > 3 :
		cur_dir -= 4
	i += 1
	nx = x + dx[cur_dir]
	ny = y + dy[cur_dir]
	if ny < 0 or nx < 0 or ny >= n or nx >= n \
		or board[ny][nx] == 1 :
		break
	# 꼬리 줄이기
	if board[ny][nx] == 0 :
		tx, ty = tail.popleft()
		board[ty][tx] = 0
	# 머리 늘리기
	tail.append((nx,ny))
	board[ny][nx] = 1
	x, y = nx, ny
print(i)
