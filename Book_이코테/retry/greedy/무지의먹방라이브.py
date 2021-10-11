import heapq

ft = [3, 2, 2]
k = 5

def solution(food_times, k):

	foods = []
	for i in range(1, len(food_times) + 1) :
		heapq.heappush(foods, (food_times[i - 1], i))

	rest = k
	time, total = foods[0][0], 0
	length = len(foods)
	while rest >= (time - total) * length:
		rest -= (time - total) * length
		heapq.heappop(foods)
		length = len(foods)
		if length == 0:
			return (-1)
		total = time
		time = foods[0][0]
	foods.sort(key=lambda x: x[1])
	return (foods[rest % len(foods)][1])

print(solution(ft, k))
