def solution(n):
	result = []
	while n > 0:
		rest = n % 3
		_next = n // 3
		if _next > 0 and rest == 0:
			result.append(4)
			_next -= 1
		else :
			result.append(rest)
		n = _next
	answer = ""
	for num in result[::-1]:
		answer += str(num)
	return answer