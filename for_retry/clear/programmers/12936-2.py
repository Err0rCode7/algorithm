from math import factorial

def get_comb_count(n, k, remains, result):
	if n == 1:
		return
	size = factorial(n) // len(remains)

	# 1부터가 아닌 0 부터 시작
	prefix_number =  k // size
	offset = k % size
	if offset == 0:
		result.append(remains[prefix_number - 1])
		remains.remove(remains[prefix_number - 1])
		result.extend(list(reversed(remains)))
		return
	result.append(remains[prefix_number])
	remains.remove(remains[prefix_number])
	get_comb_count(n - 1, offset, remains, result)


def solution(n, k):
	remains = [i for i in range(1, n + 1)]
	result = []

	get_comb_count(n, k, remains, result)

	return result

print(solution(3, 5))