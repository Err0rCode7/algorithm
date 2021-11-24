import sys
import bisect

input = sys.stdin.readline

n, x = map(int, input().rstrip().split())
numbers = list(map(int, input().rstrip().split()))

bot = 0
top = len(numbers)
mid = (bot + top)//2
count = 0
while True and bot < top:
	if numbers[mid] == x :
		for i in range(mid, -1, -1):
			if x == numbers[i]:
				count += 1
			else :
				break
		for i in range(mid + 1, len(numbers)):
			if x == numbers[i]:
				count += 1
			else :
				break
		break

	if numbers[mid] > x:
		bot = mid + 1
		mid = (bot + top)//2
	else :
		top = mid - 1
		mid = (bot + top)//2
print(count if count > 0 else -1)
