from collections import defaultdict

import heapq

def solution(a):
	# counts = defaultdict(list)
	counts = [0] * (len(a))
	for i in a:
		counts[i] += 1
	
	heap = []
	for i in range(len(a)):
		if counts[i] != 0:
			heapq.heappush(heap, (-counts[i], i))
	
	_max = 0

	def find_star(a, number):
		count = 0
		i = 0
		while i + 1 < len(a): 
			if i + 1 < len(a) and\
			a[i] != a[i + 1] and (a[i] == number or a[i + 1] == number):
				# print(a[i], a[i + 1], number)
				count += 1
				i += 2
			else:
				i += 1
		return count

	while heap:
		count, number = heapq.heappop(heap)
		count *= -1
		if count <= _max:
			break
		star = find_star(a, number)
		# print(star)
		_max = max(star, _max)
	
	return _max * 2

print(solution([0]))
print(solution([5,2,3,3,5,3]	))
print(solution([0,3,3,0,7,2,0,2,2,0]	))