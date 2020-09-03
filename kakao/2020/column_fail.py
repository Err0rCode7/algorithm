n = 5
test_case = [
	(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]),
	(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]])
	]

def is_between(row, x, n) :
	if x > 0 and x + 1 < n + 1 :
		left, right = row[x - 1], row[x + 1]
		if 1 in left and \
			1 in right :
			return True
	return False

def is_between_only(box, x, y, n) :
	if (x + 1 < n + 1 and y > 0 and 0 in box[y - 1][x + 1]) \
		or (y > 0 and 0 in box[y - 1][x]) :
		return False
	if x > 0 and x + 1 < n + 1 :
		left, right = box[y][x - 1], box[y][x + 1]
		if len(left) > 0 and 1 in left and \
			len(right) > 0 and 1 in left :
			return True
	return False

def is_on_col(box, x, y, n) :
	if y == 0 :
		return False
	if 0 in box[y - 1][x] :
		return True
	return False

def is_valid_pos(x, y, n) :
	if x >= n + 1 or x < 0 or y >= n + 1 or y < 0:
		return False
	return True

def can_delete(box, x, y, n) :
	obj = box[y + 1][x]
	if len(obj) == 0 :
		return True
	if 1 in obj :
		if is_between(box[y + 1], x, n) :
			return True
	return False

def solution(n, build_frame):

	result = [[[] for _ in range(n + 1)] for _ in range(n + 1)]
	for build in build_frame :
		x, y, content_type, do_type = build
		#print(build)
		# 건설
		print(build)
		if do_type == 1 and is_valid_pos(x, y, n):
			# 보의 경우 + 바닥 제외
			if content_type == 1 and y != 0 and x != n and 1 not in result[y][x] :
				# 양쪽이 보인 경우이거나 한쪽이 기둥인 경우
				if is_between(result[y], x, n) or (is_on_col(result, x, y, n) or is_on_col(result, x + 1, y, n)):
					#print("보 append")
					result[y][x].append(1)
			# 기둥일경우
			if content_type == 0 and 0 not in result[y][x] and y < n:
				# 바닥이거나 기둥이나 보 위 일때
				if y == 0 or is_on_col(result, x, y, n) \
					or 1 in result[y][x] \
					or (x > 0 and 1 in result[y][x - 1]) :
					result[y][x].append(0)
					#print("기둥 append")
		# 삭제
		elif do_type == 0 and is_valid_pos(x, y, n) :
			# 보의 경우
			if content_type == 1 and 1 in result[y][x]:
				# 양쪽이 보인 경우이거나 한쪽이 기둥인 경우
				if not (is_between_only(result, x, y, n)) and \
					not (is_between_only(result, x + 1, y, n)) and \
					not (is_between_only(result, x - 1, y, n))  :
					result[y][x].remove(1)
					#print("보 remove")
			# 기둥일경우
			if content_type == 0 and 0 in result[y][x] :
				# 위에 보이고 삭제할 수 있을 때
				if can_delete(result, x, y, n) :
					#print("기둥 remove")
					result[y][x].remove(0)
	# parse
	answer = []
	for x in range(n + 1) :
		for y in range(n + 1) :
			result[y][x].sort()
			for i in result[y][x] :
				answer.append([x, y, i])
	return answer

print(solution(test_case[0][0], test_case[0][1]))
print(solution(test_case[1][0], test_case[1][1]))
