# test case

# Q:
# solution([3, 1, 2], 5)
# A:
# 1

def solution(food_times, k):

	food_times_with_index = []
	for i, v in enumerate(food_times):
		food_times_with_index.append((v, i + 1))
	food_times_with_index.sort(key= lambda x: x[0])

	food_index = 0

	cycle_value = food_times_with_index[food_index][0]
	cycle_len = len(food_times_with_index) - food_index
	cycle = 0

	while(True):
		# print("k", k)
		# print("cycle_len", cycle_len)
		# print("cycle_value", cycle_value)
		# print("cycle", cycle)
		# print("food index", food_index)
		if k < cycle_len * cycle_value :
			if k == cycle_len * cycle_value :
				food_index += 1
			break
		cycle = food_times_with_index[food_index][0]
		k -= cycle_len * cycle_value
		
		food_index += 1
		for i in range(food_index, len(food_times_with_index)) :
			if food_times_with_index[food_index - 1] != food_times_with_index[food_index] :
				break
			food_index += 1

		if food_index >= len(food_times_with_index):
			return -1
		
		cycle_len = len(food_times_with_index) - food_index
		cycle_value = food_times_with_index[food_index][0] - cycle


	result = food_times_with_index[food_index:]

	return sorted(result, key= lambda x: x[1])[k % len(result)][1]


print(solution([3, 1, 2], 4))
print(solution([1, 3, 4, 5], 4))

'''
3 1 2

:3
2 1

:2
1

'''