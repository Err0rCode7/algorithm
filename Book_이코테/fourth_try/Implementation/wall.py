'''
기둥과 보 설치


'''

def solution(n, build_frame):
	# 1. build_map을 만들고 build_frame을 하나씩 실행
	# build_map은 n * n
	# 2. 규칙 검사를 실행
	# 규칙 검사에 맞지않으면 롤백

	build_map = [[2 * [0] for _ in range(n + 1)] for _ in range(n + 1)]
	result = []
	for x, y, a, b in build_frame:
		if b == 0:
			result.remove([x, y, a])
		else :
			result.append([x, y, a])
		pre = build_map[y][x][a]
		build_map[y][x][a] = b
		for r_x, r_y, r_a in result :
			if not is_valid(r_x, r_y, r_a, build_map) :
				build_map[y][x][a] = pre
				if b == 0:
					result.append([x, y, a])
				else :
					result.remove([x, y, a])
				break

	# return 하는 배열은 x좌표 기준으로 오름차순 정렬하며, x좌표가 같을 경우 y좌표 기준으로 오름차순 정렬해주세요.
	# x, y좌표가 모두 같은 경우 기둥이 보보다 앞에 오면 됩니다.
	return sorted(result, key=lambda x: (x[0], x[1], x[2]))

def is_valid(x, y, a, build_map):
	result = False
	try :
		if a == 1:
			# 보
			# 보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.
			if build_map[y - 1][x][0] == 1 or \
				build_map[y - 1][x + 1][0] == 1 or \
				(build_map[y][x - 1][1] == 1 and build_map[y][x + 1][1] == 1):
				result = True
		else :
			# 기둥
			# 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
			if (y < len(build_map) - 1) and (y == 0 or build_map[y - 1][x][0] == 1 or build_map[y][x][1] == 1 or build_map[y][x - 1][1] == 1):
				result = True
	except :
		return result
	return result




inputList = []

inputList.append(
	(5,
	[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]],
	[[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]
))
inputList.append(
	(5,
	[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]],
	[[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]
))

for n, build_frame, answer in inputList:
	result = solution(n, build_frame)
	print(result)
	resultForPrint = True
	if len(answer) != len(result):
		resultForPrint = False
	else :
		for i in range(len(answer)):
			x, y, a = answer[i]
			r_x, r_y, r_a = result[i]
			if not (x == r_x and y == r_y and a == r_a):
				resultForPrint = False
	print(resultForPrint)
