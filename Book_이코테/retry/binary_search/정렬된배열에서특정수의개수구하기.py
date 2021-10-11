import bisect
import sys

input = sys.stdin.readline


def binary_search(array, target):
	left = bisect.bisect_left(array, target)
	right = bisect.bisect_right(array, target)
	if len(array) == left or len(array) == right:
		return (-1)
	return (right - left)

N, x = map(int, input().rstrip().split())

array = list(map(int, input().rstrip().split()))

print(binary_search(array, x))
