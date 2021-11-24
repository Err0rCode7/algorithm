
def solution(N, stages):
	stages.sort(reverse=True)
	failure = [[0, i] for i in range(N + 1)]
	i = 0
	for cur_stage in range(N + 1, -1, -1):
		rest = 0
		while i < len(stages):
			if cur_stage > stages[i]:
				break
			if cur_stage == stages[i] :
				rest += 1
				if cur_stage != N + 1:
					failure[cur_stage][0] = rest / (i + 1)
			i += 1
	result = []
	for failure, index in sorted(failure[1:N + 1],key=lambda x: (-x[0], x[1])):
		result.append(index)
	return result

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))