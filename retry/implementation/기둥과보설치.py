
def is_valid(result, n):

	for x, y, a in result :
		if a == 0 and \
		(y == 0 or [x, y, 1] in result or [x - 1, y, 1] in result or [x, y - 1, 0] in result):
			continue
		elif a == 1 and \
		([x, y - 1, 0] in result or [x + 1, y - 1, 0] in result or ([x - 1, y, 1] in result and [x + 1, y, 1] in result)):
			continue
		else:
			return False
	return True


def solution(n, build_frame):
	# build_frame = > [x, y, a, b]
	# x, y 좌표점
	# a : 0 기둥 , 1 보
	# b : 0 삭제 , 1 설치

	result = []
	for x, y, a, b in build_frame :
		if b == 0:
			if [x, y, a] in result:
				result.remove([x, y, a])
				if not is_valid(result, n):
					result.append([x, y, a])
		elif b == 1:
			if [x, y, a] not in result:
				result.append([x, y, a])
				if not is_valid(result, n):
					result.remove([x, y, a])

	result.sort(key=lambda x:(x[0], x[1], x[2]))
	return (result)

print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]))
