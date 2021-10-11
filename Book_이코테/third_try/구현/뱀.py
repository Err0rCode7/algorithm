# boj 3190

# test case
'''
Q:
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D
A:
9
Q:
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
A:
21
Q:
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
A:
13
'''

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
k = int(input())

board = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(k) :
	y, x = map(int, input().rstrip().split())

	board[y][x] = 'A'
l = int(input())

commandList = []

for i in range(l):
	time, direction = input().rstrip().split()
	commandList.append((int(time), direction))

time = 0

commandTime, direction = commandList[0]
commandIndex = 1

dirIndex = 0
dirX = [1, 0, -1, 0]
dirY = [0, 1, 0, -1]

x, y = 1, 1

queue = deque()
queue.append((x, y))

while(True) :
	time += 1

	x += dirX[dirIndex]
	y += dirY[dirIndex]

	if not (0 < x < len(board)) or not (0 < y < len(board)) or board[y][x] == 'T':
		break
	
	if board[y][x] != 'A' :
		xTail, yTail = queue.popleft()
		board[yTail][xTail] = 0
	board[y][x] = 'T'
	queue.append((x, y))

	if commandTime == time :
		if direction == 'L':
			dirIndex -= 1
		else :
			dirIndex += 1
		
		if dirIndex < 0 :
			dirIndex = 3
		if dirIndex > 3 :
			dirIndex = 0
		if len(commandList) > commandIndex:
			commandTime, direction = commandList[commandIndex]
			commandIndex += 1
		else :
			commandTime = -1

print(time)