import sys

def is_valid(s) :
	stack = []
	for i in range(len(s)) :
		if s[i] == '(' :
			stack.append('(')
		if s[i] == ')' :
			if (len(stack) < 1) :
				return False
			stack.pop()
	return True

def is_balance(s) :
	open_count = 0
	close_count = 0
	for i in range(len(s)) :
		if s[i] == '(' :
			open_count += 1
		if s[i] == ')' :
			close_count += 1
	return (open_count == close_count)

def process(p) :
	v = ""
	u = ""
	i = 0
	open_count = 0
	close_count = 0
	while i < len(p) :
		if open_count > 0 and close_count > 0 and open_count == close_count :
			v = p[i:]
			break
		if p[i] == '(' :
			open_count += 1
			u += p[i]
		if p[i] == ')' :
			close_count += 1
			u += p[i]
		i += 1
	return (u, v)

def solution(p) :
	input = p
	temp = ""
	if not is_valid(input) :
		u, v = process(input)
		print("u: ",u , "v: ", v)
		if (is_valid(u)) :
			temp = u + solution(v)
		else :
			temp = "(" + solution(v) + ")"
			u = u[1:-1]
			add = ""
			for i in range(len(u)) :
				if u[i] == '(' :
					add += ')'
				elif u[i] == ')' :
					add += '('
			temp += add
		answer = temp
	else :
		answer = p
	return answer

string = sys.stdin.readline().rstrip().strip('\"')
print(solution(string))
