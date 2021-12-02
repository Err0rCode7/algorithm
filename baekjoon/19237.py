from collections import deque
import sys, heapq

input = sys.stdin.readline

n, m, k = map(int, input().rstrip().split())

# 위 아래 왼쪽 오른쪽
dx = [0, 0, 0, -1, 1]
dy = [0, -1, 1, 0, 0]

board = [[-1] * (n + 2) for _ in range(n + 2)]
# x, y
sharks_pos = [[0, 0] for _ in range(m + 1)]

for y in range(1, n + 1):
	line = list(map(int, input().rstrip().split()))
	
	for x in range(n):
		board[y][x + 1] = line[x]
		if line[x] == 0:
			continue
		shark_number = line[x]
		sharks_pos[shark_number][0] = x + 1
		sharks_pos[shark_number][1] = y

sharks_vector = list(map(int, input().rstrip().split()))
sharks_vector.insert(0, 0)

sharks_rules = [[[] for _ in range(5)] for _ in range(m + 1)]
for shark_number in range(1, m + 1):
	for vector in range(1, 5):
		line = list(map(int, input().rstrip().split()))
		sharks_rules[shark_number][vector].extend(line)

sharks = deque([i for i in range(1, m + 1)])

# x, y, time
smell_time_q = deque()

#shark, time
smell = [[[0, 0] for _ in range(n + 2)] * (n + 2) for _ in range(n + 2)]

for i in range(len(sharks)):
	shark_number = sharks[i]
	x, y = sharks_pos[shark_number]
	smell[y][x][0] = k
	smell[y][x][1] = shark_number

time = 0

while time < 1000:
	if len(sharks) <= 1:
		break
	print("#### round: ", time, sharks)
	## 시간 카운팅
	time += 1

	## 상어 이동
	for i in range(len(sharks)):
		shark_number = sharks.popleft()
		vector = sharks_vector[shark_number]
		pre_x, pre_y = sharks_pos[shark_number]
		my_smell_pos = []
		move = False
		dead = False
		# 4 방향
		print("sharks_number: ", shark_number)
		print("pre:: ", (pre_x, pre_y))
		for _dir in sharks_rules[shark_number][vector]:
			nx, ny = pre_x + dx[_dir], pre_y + dy[_dir]
			print("nx, ny", nx, ny)
			if board[ny][nx] == -1:
				continue
			## 냄새 체크
			if board[ny][nx] != 0 and board[ny][nx] < shark_number:
				dead = True
				break
			# 빈 공간 발견시 이동
			if (board[ny][nx] == 0 or board[ny][nx] > shark_number) and smell[ny][nx][0] == 0:
				move = True
				board[ny][nx] = shark_number
				sharks_pos[shark_number][0], sharks_pos[shark_number][1] = nx, ny
				sharks_vector[shark_number] = _dir
				sharks.append(shark_number)
				smell[ny][nx][0] = k
				smell[ny][nx][1] = shark_number
				smell_time_q.append((nx, ny, k))
				break
			# 자신의 냄새 공간 파악
			if smell[ny][nx][1] == shark_number:
				my_smell_pos.append((nx, ny, _dir))
		# 수가 더 낮은 상어를 만나면 죽는다.
		if board[pre_y][pre_x] == shark_number:
			board[pre_y][pre_x] = 0
		if dead:
			continue
		# 빈 공간이 없으면 자신의 냄새로 이동
		if not move and my_smell_pos:
			nx, ny, n_vector = my_smell_pos[0]
			board[ny][nx] = shark_number
			sharks_pos[shark_number][0], sharks_pos[shark_number][1] = nx, ny
			sharks_vector[shark_number] = n_vector
			sharks.append(shark_number)
			smell[ny][nx][0] = k
			smell[ny][nx][1] = shark_number
			smell_time_q.append((nx, ny, k))

		print("next:: ", sharks_pos[shark_number])

	## 냄새 카운팅
	while smell_time_q:
		x, y, remain = smell_time_q.popleft()
		if remain != smell[y][x][0]:
			continue
		remain -= 1
		if remain <= 0:
			smell[y][x][0] = 0
			smell[y][x][1] = 0
		else :
			smell_time_q.append((x, y, remain))
			smell[y][x][0] = remain

	# ## 냄새 뿌리기
	# for i in range(len(sharks)):
	# 	shark_number = sharks[i]
	# 	x, y = sharks_pos[shark_number]
	# 	smell[y][x][0] = k
	# 	smell[y][x][1] = shark_number

	# if time == 14:
		# break
print(time if time < 1000 else -1)