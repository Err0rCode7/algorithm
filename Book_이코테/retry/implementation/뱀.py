import sys
from collections import deque

input = sys.stdin.readline

N = int(input().rstrip())
K = int(input().rstrip())


board = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(K):
	y, x = map(int, input().rstrip().split())
	board[y][x] = 2

L = int(input().rstrip())

queue = deque()
for i in range(L):
	time, curve = input().rstrip().split()
	curve = 1 if curve == 'D' else -1
	queue.append((int(time), curve))

tail = deque([(1, 1)])
time, direction = 0, 0
cur_x, cur_y = 1, 1
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
curve_time, curve = queue.popleft()
while True :
	time += 1
	cur_x, cur_y = cur_x + dx[direction], cur_y + dy[direction]
	if cur_x <= 0 or cur_x > N or cur_y <= 0 or cur_y > N or board[cur_y][cur_x] == 1:
		break

	if board[cur_y][cur_x] == 0 :
		x, y = tail.popleft()
		board[y][x] = 0
	tail.append((cur_x, cur_y))
	board[cur_y][cur_x] = 1
	if time == curve_time:
		direction += curve
		if direction < 0 :
			direction += 4
		elif direction > 3 :
			direction -= 4
		curve_time = 0
		if queue :
			curve_time, curve = queue.popleft()
print(time)

"""
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D

10
4
1 2
1 3
1 4
1 5
4
8 D
10 D
11 D
13 L

10
5
1 5
1 3
1 2
1 6
1 7
4
8 D
10 D
11 D
13 L
"""
