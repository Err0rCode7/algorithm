from collections import deque

def solution(s):
	stack = deque()
	for i in range(len(s)):
		if not stack :
			stack.append(s[i])

			continue
		if stack[-1] == s[i]:
			stack.pop()
		else :
			stack.append(s[i])
	if stack:
		return 0
	return 1

print(solution("baabaa"))
print(solution("cdcd"))