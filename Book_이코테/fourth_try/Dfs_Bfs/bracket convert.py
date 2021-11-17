import collections, sys

sys.setrecursionlimit(10000)

def isValid(p) :
	stack = collections.deque()

	for i in range(len(p)):
		if p[i] == '(':
			stack.append(i)
		else :
			if not stack :
				return False
			else :
				stack.pop()
	return False if stack else True

def reverse(p):
	result = ""
	for c in p :
		result += '(' if c == ')' else ')'
	return result

def convert(p) :
	if len(p) == 0:
		return p
	
	left, right = 0, 0
	for index in range(len(p)):
		if p[index] == '(':
			left += 1
		if p[index] == ')':
			right += 1
		if left > 0 and left == right:
			break
	u = p[:index + 1]
	v = p[index + 1:]
	if isValid(u):
		return u + convert(v)
	else :
		return '(' + convert(v) + ')' + reverse(u[1:-1])

def solution(p):
	return convert(p)

testcases = [("(()())()", "(()())()"), (")(", "()"), ("()))((()", "()(())()")]

for question, answer in testcases :
	print(solution(question) == answer)