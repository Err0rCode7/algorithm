from collections import deque
import sys

sys.setrecursionlimit(10000)

def is_valid(instr) :
	stack = []
	for c in instr:
		if c == '(' :
			stack.append('(')
		else :
			if len(stack) == 0 :
				return False
			stack.pop()
	if len(stack) == 0 :
		return True
	else :
		return False

def solution(p) :
	if is_valid(p) :
		return (p)
	else :
		if len(p) == 0:
			return (p)
		sum = 0
		flag = False
		u = ""
		v = ""
		for c in p :
			if sum == 0 and flag :
				v += c
			elif c == "(":
				flag = True
				sum += 1
				u += c
			elif c == ")" :
				flag = True
				sum -= 1
				u += c
		if is_valid(u) :
			return (u + solution(v))
		else :
			result = "(" + solution(v) + ")"
			u = u[1:-1]
			for c in u :
				if c == '(' :
					result += ')'
				elif c == ')':
					result += '('
			return (result)
