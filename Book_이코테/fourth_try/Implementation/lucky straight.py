'''
럭키 스트레이트

현재 캐릭터의 점수를 N이라고 할 때, 자릿수를 기준으로 점수 N을 반으로 나누어 왼쪽 부분의 각 자릿수의 합과 오른쪽 부분의 각 자릿수의 합을 더한 값이 동일한 상황을 럭키 스트레이트로 판정하는 문제
'''

import sys

def sumDigitFromString(string) :
	_sum = 0
	for c in string :
		_sum += int(c)

	return _sum

input = sys.stdin.readline

n = input().rstrip()

left = n[:len(n)//2]
right = n[len(n)//2:]

if sumDigitFromString(left) == sumDigitFromString(right) :
	print("LUCKY")
else :
	print("READY")