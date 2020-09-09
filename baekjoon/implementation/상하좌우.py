import sys

input = sys.stdin.readline

n = int(input().rstrip())
cmds = input().rstrip().split()

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

move_type = ['R', 'D', 'L', 'U']

cx, cy = 1, 1
for cmd in cmds :
	for j in range(4) :
		if cmd == move_type[j] :
			nx, ny = cx + dx[j], cy + dy[j]
	if nx < 1 or ny < 1 or nx > n or ny > n :
		continue
	cx, cy = nx, ny

print(cy, cx, end="")
