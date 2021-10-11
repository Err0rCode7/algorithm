'''
만들 수 없는 금액

N개의 동전을 가지고 만들 수 없는 금액의 최솟값을 구하라.

Test Case

3 2 1 1 9

1	1	2	3	9
	2	3	5	10
		4	6	11
			7	12
				13
				14
				15
				16
'''
import sys

input = sys.stdin.readline

n = int(input())

coins = list(map(int, input().rstrip().split()))

coins.sort()

maxPrice = 1


for coin in coins :
	if coin <= maxPrice:
		maxPrice += coin
	else :
		break

print(maxPrice)