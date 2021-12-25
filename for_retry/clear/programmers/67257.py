from collections import defaultdict
from itertools import permutations

class node:
	
	def __init__(self, value, is_op, op):
		self.pre = None
		self.next = None
		self.value = value
		self.op = op
		self.is_op = is_op

	def is_op(self):
		return self.is_op

	def get_op(self):
		return self.op
	def get_number(self):
		return self.value

def solution(expression):

	def get_linked_list(expression):

		pre_str = ""
		op = None
		ops = defaultdict(list)
		for i in range(len(expression)):
			if '0' <= expression[i] <= '9':
				pre_str += expression[i]
			else :
				number = node(int(pre_str), False, None)
				pre_str = ""
				if op != None:
					number.pre = op
					op.next = number

				op = node(0, True, expression[i])
				ops[expression[i]].append(op)

				number.next = op
				op.pre = number
		number = node(int(pre_str), False, None)
		number.pre = op
		op.next = number

		return ops

	def calc_op(left, right, op):
		if op == '*':
			return left * right
		elif op == '-':
			return left - right
		else:
			return left + right

	ops = get_linked_list(expression)
	perms = list(permutations(ops.keys(), len(ops.keys())))

	answer = 0
	for op_list in perms:
		number = 0
		ops = get_linked_list(expression)
		# print()
		for op in op_list:
			# print(op)
			for op_node in ops[op]:
				left = op_node.pre.get_number()
				right = op_node.next.get_number()
				result = calc_op(left, right, op)
				# print(left, right, result)
				number = node(result, False, None)
				if op_node.pre.pre != None:
					number.pre = op_node.pre.pre
					op_node.pre.pre.next = number
				if op_node.next.next != None:
					number.next = op_node.next.next
					op_node.next.next.pre = number
		if number != 0:
			answer = max(answer, abs(number.get_number()))
	return answer

print(solution("100-200*300-500+20"	))
print(solution("50*6-3*2"	))