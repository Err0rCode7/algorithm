import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
character = list(map(int, input().rstrip().split()))
game_map = []

for i in range(n) :
	game_map.append(list(map(int, input().rstrip().split())))

# 0 북 1 동 2 남 3 서
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

game_map[character[1]][character[0]] = 2
rot_count = 1

while True :
	x, y, direction = character

	# 보는 방향에서 왼쪽부터 시작이므로 왼쪽 방향으로 회전
	direction -= 1
	if direction < 0 :
		direction = 3

	# 이동 안했는지 체크
	flag = True

	# 최대 4 방향 확인
	for i in range(4) :
		nx = x + dx[direction]
		ny = y + dy[direction]
		# 바라보는 방향 앞 한칸이 이동 불가일 때 방향 회전
		if nx < 0 or nx >= m or ny < 0 or ny >= n \
		or game_map[ny][nx] > 0 :
			direction -= 1
			if direction < 0 :
				direction = 3
		else : # 이동 가능할 때 이동
			rot_count += 1
			game_map[ny][nx] = 2
			flag = False
			break

	# 이동하지 않았을 때 뒤로 가거나 종료
	if flag :
		direction += 2
		direction %= 4
		nx = x + dx[direction]
		ny = y = dy[direction]
		if game_map[ny][nx] == 1 :
			break
		elif game_map[ny][nx] == 0 :
			game_map[ny][nx] = 2
			rot_count += 1
		direction += 2
		direction %= 4

	# 캐릭터 이동과 이동횟수 저장
	character = (nx, ny, direction)


print(rot_count)
