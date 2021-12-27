import sys, heapq

input = sys.stdin.readline

n = int(input())

left_heap = [] # 최대 힙
right_heap = [] # 최소 힙
LEFT = -1
RIGHT = 1

# mid = 0
# result = []
# for count in range(n): # 시그마 Nlog(N) -> 시간초과
# 	number = int(input())
# 	result.append(number)
# 	result.sort()
# 	length = len(result)
# 	if length % 2 != 0:
# 		print(result[length // 2])
# 	else :
# 		print(min(result[length // 2], result[length// 2 - 1]))

mid = 0
for count in range(n): # Nlog(N) -> 통과
	number = int(input())
	if count == 0:
		mid = number
	else:
		if mid < number:
			if len(right_heap) > len(left_heap):
				heapq.heappush(left_heap, (-mid, mid))
				mid = heapq.heappushpop(right_heap, (number, number))[1]
			elif len(right_heap) < len(left_heap):
				heapq.heappush(right_heap, number)
				mid = heapq.heappushpop(left_heap, (-mid, mid))[1]
			else: # equal
				heapq.heappush(right_heap, (number, number))
				mid = heapq.heappushpop(left_heap, (-mid, mid))[1]
		else:
			if len(right_heap) > len(left_heap):
				heapq.heappush(left_heap, (-number, number))
				mid = heapq.heappushpop(right_heap, (mid, mid))[1]
			elif len(right_heap) < len(left_heap):
				heapq.heappush(right_heap, (mid, mid))
				mid = heapq.heappushpop(left_heap, (-number, number))[1]
			else: # equal
				heapq.heappush(right_heap, (mid, mid))
				mid = heapq.heappushpop(left_heap, (-number, number))[1]
	print(mid)
	# print("\t", mid, left_heap, right_heap)
