import sys

input = sys.stdin.readline

N = int(input().rstrip())
array = list(map(int, input().rstrip().split()))

left = 0
right = len(array) - 1

while left <= right:

	mid = (left + right) // 2
	if array[mid] == mid:
		break
	elif array[mid] > mid:
		right = mid - 1
	elif array[mid] < mid:
		left = mid + 1

if left < right:
	print(mid)
else :
	print(-1)
