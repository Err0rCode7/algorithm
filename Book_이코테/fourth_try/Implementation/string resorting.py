'''
문자열 재정렬

알파벳 대문자와 숫자(0~9)로 구성된 문자열 입력을 모든 알파벳을 오름차순으로 정렬하고 이어서 모든 숫자를 더한 값을 붙여 출력하는 문제
'''

import sys

input = sys.stdin.readline

s = input().rstrip()

_sumPoint = 0
_sumString = []

for c in s :
	try :
		_sumPoint += int(c)
	except :
		_sumString.append(c)

_sumString.sort()

for c in _sumString:
	print(c, end="")
print(_sumPoint)