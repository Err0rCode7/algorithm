'''
곱하기 혹은 더하기

숫자 스트링을 곱하기 더하기 조합으로 만들 수 있는 가장 큰 수
'''

import sys

input = sys.stdin.readline

numbers = input().rstrip()

_sum = 0

for number in numbers :
	number = int(number)
	if _sum == 0 :
		_sum += number
	else :
		_sum *= number

print(_sum)