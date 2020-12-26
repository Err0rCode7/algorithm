
def solution(N, stages):

	in_stage = [0 for _ in range(N + 2)]
	stacked_list = [0 for _ in range(N + 2)]

	for num in stages:
		in_stage[num] += 1
		for i in range(1, num + 1):
			stacked_list[i] += 1

	failure = []
	for i in range(1, N + 1):
		if in_stage[i] == 0 or stacked_list[i] == 0:
			failure.append((0, i))
		else:
			failure.append((in_stage[i] / stacked_list[i], i))
	failure.sort(key= lambda x:-x[0])
	result = []
	for content in failure:
		result.append(content[1])
	return (result)

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))
