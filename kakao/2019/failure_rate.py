
testcases = []
testcases.append((5, [2, 1, 2, 6, 2, 4, 3, 3]))
testcases.append((4, [4,4,4,4,4]))

def solution(N, stages) :

	failure_rate = []
	in_stage = [0 for _ in range(N + 2)]

	for stage in stages :
		in_stage[stage] += 1
	for stage in stages :
		for pre_stage in range(1, stage) :
			in_stage[pre_stage] += 1
	#print(in_stage)
	for i in range(1, N + 1) :
		if in_stage[i] == 0 :
			failure_rate.append((0, i))
		else :
			failure_rate.append((float((in_stage[i] - in_stage[i + 1]) / in_stage[i]), i))
	failure_rate.sort(key=lambda x:(-x[0], x[1]))
	answer = []
	for a, b in failure_rate :
		answer.append(b)
	#print(b)
	return answer

for testcase in testcases :
	print(solution(testcase[0], testcase[1]))
