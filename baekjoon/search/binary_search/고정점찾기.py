import sys

sys.setrecursionlimit(10000)

input = sys.stdin.readline
n = int(input())
numbers = list(map(int, input().rstrip().split()))

def binary_search(iter, start, end) :
	if start > end :
		return None
	mid = (start + end) // 2
	if iter[mid] == mid :
		return mid
	elif iter[mid] < mid :
		return binary_search(iter, mid + 1, end)
	elif iter[mid] > mid :
		return binary_search(iter, start, mid - 1)

result = binary_search(numbers, 0, n - 1)
if result == None :
	print(-1)
else :
	print(result)
