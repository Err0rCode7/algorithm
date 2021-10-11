'''
문자열 뒤집기

문자열은 0과 1로 구성되어있고 0을 1로 1을 0으로 뒤집을 수 있다.

하나의 문자로 만드는 데 뒤집는 횟수의 최솟값을 구하는 문제
'''

import sys

input = sys.stdin.readline

binaryString = input().rstrip()

zeroBlockCount = 0
oneBlockCount = 0

pre = -1

for n in binaryString :
	n = int(n)

	if pre != n :
		if n == 0 :
			zeroBlockCount += 1
		else :
			oneBlockCount += 1
	pre = n

print(min(zeroBlockCount, oneBlockCount))