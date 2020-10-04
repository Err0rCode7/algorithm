
def solution(N, stages) :
	on_stage = [0 for _ in range(N + 2)]
	thru = [0 for _ in range(N + 2)]
	result = []
	for i in stages :
		on_stage[i] += 1

	for i in range(1, N + 1) :
		thru[i] = sum(on_stage[i:])
		if thru[i] == 0 or on_stage[i] == 0:
			result.append((0, i))
		else :
			result.append((on_stage[i] / thru[i], i))
	print(result)
	answer = []
	for fault, index in sorted(result, key= lambda x:(-x[0], x[1])) :
		answer.append(index)
	return (answer)

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))
