import heapq

def solution(n, works):

	runtime_work = []
	for work in works:
		heapq.heappush(runtime_work, work)
	
	cycle_sum = 0
	rest = 0
	while runtime_work:
		# print(runtime_work)
		length = len(runtime_work)
		cycle_sum += n // length
		rest = n % length
		min_work = runtime_work[0]
		# print(n, cycle, cycle_sum, rest, min_work, runtime_work)
		if cycle_sum < min_work :
			break
		# print(n, cycle, cycle_sum, rest, min_work, runtime_work)
		_sum = 0
		while runtime_work and runtime_work[0] <= cycle_sum:
			poped = heapq.heappop(runtime_work)
			_sum += (cycle_sum - poped) * length
		rest += _sum
		n = rest
	
	answer = 0
	stop_flag = len(runtime_work) - rest
	while runtime_work:
		work = heapq.heappop(runtime_work)
		work -= cycle_sum
		if stop_flag == 0 :
			work -= 1
		else :
			stop_flag -= 1
		if work > 0:
			answer += work ** 2
	return answer

print(solution(4, [4, 3, 3, 2])) # 18
print(solution(16, [4, 3, 3, 2])) # 0 
print(solution(9, [4, 3, 3])) # 1
print(solution(4, [4, 3, 3]))# 12
print(solution(1, [2, 1, 2]))#  6
print(solution(3, [1, 1]))# 0