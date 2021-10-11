'''
무지의 먹방 라이브

먹방 라이브 도중에 네트워크가 끊겼을 때 어느 접시부터 다시 시작해야 하는 지 찾는 문제

[3, 1, 2]	5	1
'''

import heapq

def solution(food_times, k):
	
	# index, weight(= time)

	queue = []
	for index, time in enumerate(food_times) :
		heapq.heappush(queue, (time, index + 1))
	eatingCount = 0

	while queue :
		time, index = queue[0]
		if (time - eatingCount) * len(queue) <= k :
			k -= (time - eatingCount) * len(queue)
			while queue and queue[0][0] == time :
				heapq.heappop(queue)
			eatingCount = time
		else : 
			break
	if not queue :
		return -1
	queue.sort(key= lambda x: x[1])

	return queue[k % len(queue)][1]

print(1 == solution([3, 1, 2], 5))