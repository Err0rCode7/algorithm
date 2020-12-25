import sys

sys.setrecursionlimit(10000)

def isvalid(string):
	stack = []
	for c in string:
		if (c == '('):
			stack.append('(')
		else :
			if not stack:
				return (0)
			stack.pop()
	if stack:
		return (0)
	else:
		return (1)

def solution(p):
	if (p == ""):
		return ""

	stack = []
	first_flag = 1
	index = 0
	for i in p:
		if not first_flag and not stack:
			break
		if not stack or stack[-1] == i:
			first_flag = 0
			stack.append(i)
		elif stack[-1] != i:
			stack.pop()
		index += 1
	u = p[:index]
	v = p[index:]
	if isvalid(u):
		return u + solution(v)
	else:
		new = "(" + solution(v) + ")"
		u = u[1:-1]
		for c in u:
			if c == "(":
				new += ")"
			else:
				new += "("
		return (new)

print(solution("(()())()"))
