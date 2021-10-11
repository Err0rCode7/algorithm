from itertools import permutations
import sys

input = sys.stdin.readline

N = int(input().rstrip())
nums = list(map(int, input().rstrip().split()))
oper = list(map(int, input().rstrip().split()))
opers = []
for i in range(4):
	if i == 0:
		for o in range(oper[i]):
			opers.append('+')
	if i == 1:
		for o in range(oper[i]):
			opers.append('-')
	if i == 2:
		for o in range(oper[i]):
			opers.append('*')
	if i == 3:
		for o in range(oper[i]):
			opers.append('/')
comb_iter = permutations(opers, N - 1)

result_min = int(1e10)
result_max = int(1e10) * -1

for comb in comb_iter:
	result = nums[0]
	index = 1

	for oper in comb:
		if oper == '+':
			result += nums[index]
		elif oper == '-':
			result -= nums[index]
		elif oper == '*':
			is_negative = 1
			if result < 0:
				is_negative *= -1
			if nums[index] < 0:
				is_negative *= -1
			result = abs(result) * abs(nums[index])
			result *= is_negative
		elif oper == '/':
			is_negative = 1
			if result < 0:
				is_negative *= -1
			if nums[index] < 0:
				is_negative *= -1
			result = abs(result) // abs(nums[index])
			result *= is_negative
		index += 1
	result_min = min(result_min, result)
	result_max = max(result_max, result)
print(result_max)
print(result_min)
