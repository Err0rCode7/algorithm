import heapq

testcases = []
testcases.append(([1, 1, 1, 1], 4))

# heap을 이용하여 정확성, 효율성 모두 맞은 풀이
def solution_2(food_times, k) :

	foods = []
	for i in range(len(food_times)) :
		foods.append([food_times[i], i + 1])

	heapq.heapify(foods)
	cycle_time = len(foods)
	time_sum = 0

	while ((foods[0][0] - time_sum) * cycle_time) <= k :
		k -= ((foods[0][0] - time_sum) * cycle_time)
		time_sum = foods[0][0]
		cycle_time -= 1
		heapq.heappop(foods)
		if not foods:
			return (-1)
	foods = sorted(foods, key= lambda x:x[1])
	return (foods[k % len(foods)][1])


# 정확성만 맞은 풀이
def solution(food_times, k) :

	foods = []
	for i in range(len(food_times)) :
		foods.append([food_times[i], i + 1])

	while True :
		food_count = len(foods)
		if food_count == 0 :
			return -1
		if (k < food_count) :
			break
		k -= food_count
		temp = []
		for index in range(len(foods)) :
			foods[index][0] -= 1
			if foods[index][0] != 0:
				temp.append([foods[index][0], foods[index][1]])
		foods = temp
	return (foods[k][1])

print(solution_2(testcases[0][0], testcases[0][1]))
