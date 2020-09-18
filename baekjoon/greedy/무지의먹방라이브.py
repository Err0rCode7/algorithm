import heapq

food_times = [1, 1, 1]
k = 5

def solution(food_times, k) :

	times = []
	for i in range(len(food_times)) :
		times.append((food_times[i], i + 1))
	heapq.heapify(times)
	first = times[0][0]
	cycle = len(times)
	time_sum = 0
	while k >= cycle * (first - time_sum) :
		k -= cycle * (first - time_sum)
		heapq.heappop(times)
		if not times :
			return (-1)
		time_sum = first
		first = times[0][0]
		cycle = len(times)
	times.sort(key= lambda x:x[1])
	return(times[k % len(times)][1])

print(solution(food_times, k))
