
testcase = []
testcase.append((5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]))
testcase.append((5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))

def check(result, x, y) :
	for x, y, a in result:
		if a == 1 and ([x, y - 1, 0] in result or [x + 1, y - 1, 0] in result \
			or ([x - 1, y, 1] in result and [x + 1, y, 1] in result)) :
			continue
		elif a == 0 and (y == 0 or ([x - 1, y, 1] in result or [x, y, 1] in result or \
			[x, y - 1, 0] in result)) :
			continue
		else :
			return False
	return True

def solution(n, build_frame) :

	result = []
	for cmd in build_frame :
		x, y, a, b = cmd

		if b == 1 :
			result.append([x, y, a])
			if not check(result, x, y) :
				result.remove([x, y, a])

		elif b == 0 :
			if [x, y, a] in result :
				result.remove([x, y, a])
				if not check(result, x, y) :
					result.append([x, y, a])

	return sorted(result, key= lambda x:(x[0], x[1], x[2]))

n, frames = testcase.pop()
print(solution(n, frames))
