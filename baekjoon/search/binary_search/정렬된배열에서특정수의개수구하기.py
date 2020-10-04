from bisect import bisect_left, bisect_right
import sys

input = sys.stdin.readline
n, x = map(int, input().rstrip().split())
numbers = list(map(int, input().rstrip().split()))

def search(iter, target, n) :
	left = bisect_left(iter, target)
	right = bisect_right(iter, target)
	if left == n or right == n :
		return -1
	else :
		return (right - left)

print(search(numbers, x, n))
