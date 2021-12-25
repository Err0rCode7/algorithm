import heapq

def solution(n, works):
	works.sort(reverse=True)

	heap_work_with_counts = []
	count = 0
	target = works[0]
	for i in range(len(works)):
		if target != works[i]:
			heapq.heappush(heap_work_with_counts, [-target, target, count])
			target = works[i]
			count = 1
		else:
			count += 1
	heapq.heappush(heap_work_with_counts, [-target, target, count])

	while heap_work_with_counts and n > 0:
		weight, value, count = heapq.heappop(heap_work_with_counts)
		cycle = n // count
		if len(heap_work_with_counts) > 0:
			next_weight, next_value, next_count = heap_work_with_counts[0]
			max_cycle = (value - next_value)
			print(cycle, max_cycle, count)
			if max_cycle > cycle:
				# n이 부족함

				# cycle + 나머지 큐에 등록
				if value == next_value + cycle + 1:
					heap_work_with_counts[0][2] += n % count
				elif n % count > 0:
					heapq.heappush(heap_work_with_counts, [-(value - cycle - 1), value - cycle - 1, n % count])

				# cycle 큐에 등록
				if count - n % count > 0:
					heapq.heappush(heap_work_with_counts, [-(value - cycle), value - cycle, count - n % count])
				n = 0
			else :
				n -= max_cycle * count
				heap_work_with_counts[0][2] += count
		else:
			if value - cycle - 1 > 0 and n % count > 0:
				heapq.heappush(heap_work_with_counts, [-(value - cycle - 1), value - cycle - 1, count - n])
			if value - cycle > 0 and count - n % count > 0:
				heapq.heappush(heap_work_with_counts, [-(value - cycle), value - cycle, count - n % count])
			n = 0

	answer = 0
	while heap_work_with_counts:
		weight, value, count = heapq.heappop(heap_work_with_counts)
		for i in range(count):
			answer += value**2
	return answer

print(solution(4, [4, 3, 3]))
print(solution(1, [2, 1, 2]))
print(solution(3, [1, 1]))
print(solution(99, [2, 15, 22, 55, 55]))