# 주어진 조건에 맞추어 구현을 하는 문제이다.
# 인풋에 해당하는 벽과 보를 넣거나 삭제하는 문제였다.
# 실패한 코드와 구글링을 통해 성공한 코드 두개의 방식을 해보았다. (실패한 코드는 아직 왜 실패했는지 잘 모르겠다.)
# 성공한 코드에 대해서 말하자면 일단 넣어보고 체크하는 방식이다.
# 인풋이 넣는 방식인 경우에는 일단 넣어보고 체크한 결과 값이 실패이면 결과에서 빼게된다.
# 반대로 삭제하는 방식인 경우 일단 빼고 보고 체크한 결과가 실패이면 결과에서 빼게된다.
# 실패한 코드는 성공한 코드와 다른 방식이였는데, 체크를 하는 것이 아니라 올바른 값만 넣는 아이디어였다.
# 하지만 조건문 처리에서 결함이 있는지 몇몇 테스트 케이스만 성공하고 문제를 해결할 수 없었다.
# 확실히 성공한 코드의 방식이 훨씬 직관적이며 조건문을 훨씬 간단하게 구현할 수 있는 방식인 것으로 생각되며 유용한 방법인것 같다.

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
