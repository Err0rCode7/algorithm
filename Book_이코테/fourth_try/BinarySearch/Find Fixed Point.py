import sys
input = sys.stdin.readline

n = int(input())
points = list(map(int, input().rstrip().split()))

bot = 0
top = n
mid = n // 2

while bot < top:
	mid_value = points[mid]
	if mid_value == mid :
		print(mid)
		break
	
	if mid_value > mid :
		top = mid - 1
		mid = (bot + top) // 2
	else :
		bot = mid + 1
		mid = (bot + top) // 2
if bot >= top :
	print(-1)