import sys
from collections import deque

input = sys.stdin.readline
N, K = map(int, input().rstrip().split())

info = []
virus = []
for y in range(N):
	one_info = list(map(int, input().rstrip().split()))
	info.append(one_info)
	for x, virus_number in enumerate(one_info) :
		virus.append((virus_number, x, y, 0))

S, X, Y = map(int, input().rstrip().split())

queue = deque(sorted(virus, key= lambda x: x[0]))
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
while queue :
	number, x, y, count = queue.popleft()
	if count == S:
		continue
	for i in range(4):
		nx, ny = x + dx[i], y + dy[i]
		if not (0 <= nx < N and 0 <= ny < N) or info[ny][nx] != 0:
			continue
		info[ny][nx] = number
		queue.append((number, nx, ny, count + 1))

print(info[X - 1][Y - 1])