from collections import deque
import sys

input = sys.stdin.readline

class Node:
	def __init__(self):
		self.number = 0
		self.pre = None
		self._next = None

def solution(n, k, cmd):

	head = None
	pre = None
	result = ['O' for _ in range(n)]
	deleted_cmd = deque()
	for i in range(n):
		_new = Node()
		_new.number = i
		if pre != None:
			_new.pre = pre
			pre._next = _new
		pre = _new
		if i == k:
			head = _new
	for string in cmd :
		# print(string)
		if len(string) > 1:
			command, move = string[0], int(string[2:])
			if command == 'U':
				for i in range(move):
					head = head.pre
			else:
				for i in range(move):
					head = head._next
		else :
			command = string[0]
			if command == 'C':
				deleted = head
				result[deleted.number] = 'X'
				pre = head.pre
				_next = head._next
				if _next != None:
					_next.pre = pre
					head = _next
				if pre != None:
					pre._next = _next
				if head != _next:
					head = pre
				deleted_cmd.append(deleted)
			else :
				backup = deleted_cmd.pop()
				result[backup.number] = 'O'
				pre = backup.pre
				_next = backup._next

				if pre != None:
					pre._next = backup
				if _next != None:
					_next.pre = backup
		# print(result)
		# print(head.number)
	answer = ""
	for s in result:
		answer += s
	return answer
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))

