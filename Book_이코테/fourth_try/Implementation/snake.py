'''
뱀

사각 보드에서 뱀이 밟는 위치에 따라 뱀의 길이를 다루는 문제


0 2 2 2 2 0 0 2 0 0
0 0 0 0 0 0 2 2 0 0
0 0 0 0 0 0 2 2 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0

'''

import sys
from collections import deque

def getRotatedDirIndex(curDirIndex, rotateDir) :
	dirX = [1, 0, -1, 0]
	dirY = [0, 1, 0, -1]

	if rotateDir == 'L' :
		curDirIndex -= 1
	else :
		curDirIndex += 1
	
	if curDirIndex > 3 :
		curDirIndex %= 4
	elif curDirIndex < 0 :
		curDirIndex = 4 + curDirIndex

	return curDirIndex


input = sys.stdin.readline

n = int(input().rstrip())

board = [[0] * (n + 1) for _ in range(n + 1)]

k = int(input().rstrip())

for i in range(k) :
	y, x = map(int, input().rstrip().split())
	board[y][x] = 2

l = int(input().rstrip())

rotateTimes = deque()
for i in range(l) :
	
	time, direction = input().rstrip().split()
	time = int(time)
	rotateTimes.append((time, direction))

body = deque()
body.append((1, 1))
curY, curX = 1, 1
time = 0

rotateTime = -1
curDirIndex = 0
direction = 0

dirX = [1, 0, -1, 0]
dirY = [0, 1, 0, -1]

while True :
	time += 1
	curY, curX = curY + dirY[curDirIndex], curX + dirX[curDirIndex]
	body.append((curY, curX))

	if not (0 < curY <= n and 1 <= curX <= n) or board[curY][curX] == 1 :
		break

	if board[curY][curX] == 0:
		y, x = body.popleft()
		board[y][x] = 0

	board[curY][curX] = 1

	if rotateTime == -1 :
		if rotateTimes :
			rotateTime, direction = rotateTimes.popleft()

	if rotateTime == time :
		curDirIndex = getRotatedDirIndex(curDirIndex, direction)
		rotateTime = -1

print(time)