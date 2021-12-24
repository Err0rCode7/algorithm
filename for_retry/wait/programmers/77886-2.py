
def solve(s):
	stack = []

	count = 0
	for i in range(0, len(s)):

		stack.append(s[i])
		if i < 2 :
			continue

		while len(stack) >= 3 and stack[-3:] == ['1', '1', '0']:
			stack.pop()
			stack.pop()
			stack.pop()
			count +=1
	i = len(stack)
	while i - 1 >= 0 and stack[i - 1] == '1':
		i -= 1

	answer = ""
	if i > 0:
		for c in stack[:i]:
			answer += c
	answer += "110" * count
	for c in stack[i:]:
		answer += c
	return answer
def solution(s):
	answer = []
	for string in s:
		answer.append(solve(string))

	return answer

print(solution(["1110","100111100","0111111010"]	))
