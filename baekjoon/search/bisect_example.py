from bisect import bisect_left, bisect_right
import sys

def count_by_range(array, left_value, right_value) :
	right_index = bisect_right(array, right_value)
	left_index = bisect_left(array, left_value)
	return right_index - left_index

n, x = map(int, sys.stdin.readline().rstrip().split())
input_list = list(map(int, sys.stdin.readline().rstrip().split()))
input_list.sort()
count = count_by_range(input_list, x, x)
print(-1 if count == 0 else count)
