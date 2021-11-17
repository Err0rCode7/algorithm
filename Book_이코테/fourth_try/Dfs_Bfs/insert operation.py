import sys
from itertools import permutations
from collections import deque

# 우선 순위 적용한 코드
# 두 블록으로 나누어서 풀기
# *와 /로 엮여있는 지 검사를 진행한 후 이런 케이스는 Express는 새로운 stack으로 결과값을 받아서 푼다.

def can_next(opers):
	if opers[0] == '+' or opers[0] == '-':
		return False
	elif opers[0] == '*' or opers[0] == '/':
		return True

def calc_first(left, oper, values, opers):

	if oper == '+':
		return left + calc(values, opers)
	elif oper == '-':
		return left - calc(values, opers)
	elif oper == '*':
		right = values.popleft()
		left = left * right
	elif oper == '/':
		right = values.popleft()
		left = left / right

	oper = opers.popleft()
	if len(opers) > 0 and can_next(opers) :
		return calc_first(left, oper, values, opers)
	else :
		if oper == '*':
			result = left * values.popleft()
			values.appendleft(result)
			return calc(values, opers)
		elif oper == '/':
			result = left / values.popleft()
			values.appendleft(result)
			return calc(values, opers)
		else :
			# error
			pass

def calc(values, opers) :
	result = 0
	if not values :
		return 0
	left = values.popleft()
	if not opers :
		return left
	oper = opers.popleft()
	# print(left, oper, values, opers)
	if len(opers) > 0 and can_next(opers):
		return calc_first(left, oper, values, opers)
	right = values.popleft()
	if oper == '+':
		result += left + right
	elif oper == '-':
		result += left - right
	elif oper == '*':
		result += left * right
	elif oper == '/':
		result += left / right
	values.appendleft(result)
	return calc(values, opers)

input = sys.stdin.readline

N = int(input())

values = list(map(int, input().rstrip().split()))
operation_counts = list(map(int, input().rstrip().split()))

opers = []
for i in range(4) :
	if i == 0:
		for _ in range(operation_counts[i]):
			opers.append('+')
	elif i == 1:
		for _ in range(operation_counts[i]):
			opers.append('-')
	elif i == 2:
		for _ in range(operation_counts[i]):
			opers.append('*')
	elif i == 3:
		for _ in range(operation_counts[i]):
			opers.append('/')

min_value = 1e9
max_value = -1e9

value_combs = permutations(values, len(values))

result = 0.0
for value_comb in value_combs:
	op_combs = permutations(opers, len(opers))
	for op_comb in op_combs:
		print(op_comb, value_comb)
		result = calc(deque(value_comb), deque(op_comb))
		if result == 12:
			print("the thing is")
			print(op_comb, value_comb)
		min_value = min(min_value, result)
		max_value = max(max_value, result)

print(round(min_value))
print(round(max_value))

