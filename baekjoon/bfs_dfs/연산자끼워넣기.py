from itertools import permutations
import sys

sys.setrecursionlimit(10000)

n = int(input())
numbers = list(map(int, input().split()))
case = list(map(int, input().split()))
opers = []
_max = int(1e9) * -1
_min = int(1e9)

# 순열을 이용한 풀이
'''
index = 0
for i in case :
	if index == 0:
		for j in range(i) :
			opers.append("+")
	elif index == 1 :
		for j in range(i) :
			opers.append("-")
	elif index == 2 :
		for j in range(i) :
			opers.append("*")
	elif index == 3 :
		for j in range(i) :
			opers.append("/")
	index += 1

def operation(oper, a, b) :
	if oper == "+" :
		return a + b
	elif oper == "-" :
		return a - b
	elif oper == "*" :
		negative = 1
		if a < 0 :
			negative *= -1
		if b < 0 :
			negative *= -1
		return negative * (abs(a) * abs(b))
	elif oper == "/" :
		negative = 1
		if a < 0 :
			negative *= -1
		if b < 0 :
			negative *= -1
		return negative * (abs(a) // abs(b))

pm = permutations(opers, len(opers))
for p in pm :
	num_index = 0
	result = numbers[num_index]
	for oper in p :
		if num_index == len(numbers) - 1:
			break
		result = operation(oper, result, numbers[num_index + 1])
		num_index += 1
	_max = max(_max, result)
	_min = min(_min, result)

'''

#DFS를 이용한 풀이

def dfs(now, num_index):
	global case, numbers, _max, _min
	if num_index == len(numbers) :
		_max = max(_max, now)
		_min = min(_min, now)
	else :
		if case[0] > 0 :
			case[0] -= 1
			dfs(now + numbers[num_index], num_index + 1)
			case[0] += 1
		if case[1] > 0 :
			case[1] -= 1
			dfs(now - numbers[num_index], num_index + 1)
			case[1] += 1
		if case[2] > 0 :
			case[2] -= 1
			dfs(now * numbers[num_index], num_index + 1)
			case[2] += 1
		if case[3] > 0 :
			case[3] -= 1
			dfs(int(now / numbers[num_index]), num_index + 1)
			case[3] += 1

dfs(numbers[0], 1)

print(_max)
print(_min)
