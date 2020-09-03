test_case = [
	(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]),
	(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]])
	]

def check(result, n) :

	for x, y, content in result :
		if content == 1 :
			if [x, y - 1, 0] in result or [x + 1, y - 1, 0] in result or \
				([x - 1, y, 1] in result and [x + 1 ,y ,1] in result):
				continue
			return False
		elif content == 0 :
			if y == 0 or [x - 1, y, 1] in result or [x, y, 1] in result or [x, y - 1, 0] in result :
				continue
			return False
	return True

def solution(n, build_frame):

	result = []

	for build in build_frame :
		x, y, content_type, do_type = build
		# 건설
		if do_type == 1 :
			result.append([x, y, content_type])
			if not check(result, n) :
				result.remove([x, y, content_type])
		# 제거
		elif do_type == 0 :
			result.remove([x, y, content_type])
			if not check(result, n) :
				result.append([x, y, content_type])

	# parse
	result.sort()
	answer = result
	return answer

print(solution(test_case[0][0], test_case[0][1]))
print(solution(test_case[1][0], test_case[1][1]))
