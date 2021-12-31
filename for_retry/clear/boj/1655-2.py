import heapq, sys

input = sys.stdin.readline
n = int(input())

def max_heap_pop(q):
	return -heapq.heappop(q)

def max_heap_push(q, new):
	return heapq.heappush(q, -new)

def min_heap_pop(q):
	return heapq.heappop(q)

def min_heap_push(q, new):
	return heapq.heappush(q, new)

first = True
left_max_heap = []
right_min_heap = []
cur = 0

for i in range(n):
	new = int(input())

	if first:
		first = False
		cur = new
	else :
		if len(left_max_heap) == len(right_min_heap):
			if cur > new:
				min_heap_push(right_min_heap, cur)
				max_heap_push(left_max_heap, new)
				cur = max_heap_pop(left_max_heap)
			else :
				min_heap_push(right_min_heap, new)
		elif len(left_max_heap) > len(right_min_heap) :
			if cur > new:
				min_heap_push(right_min_heap, cur)
				max_heap_push(left_max_heap, new)
				cur = max_heap_pop(left_max_heap)
			else :
				min_heap_push(right_min_heap, new)
		else:
			if cur > new:
				max_heap_push(left_max_heap, new)
			else :
				max_heap_push(left_max_heap, cur)
				min_heap_push(right_min_heap, new)
				cur = min_heap_pop(right_min_heap)
	print(cur)
