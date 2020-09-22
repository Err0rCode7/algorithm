from itertools import permutations

def solution(n, weak, dist) :

	weak_len = len(weak)
	for i in range(len(weak)):
		weak.append(n + weak[i])
	for i in range(1, len(dist) + 1) :
		pm = permutations(dist, i)
		for agents in pm :
			for j in range(weak_len) :
				temp = 0
				count = 0
				a_index = 0
				k = j
				offset = 0
				while offset < weak_len :
					if weak[j + temp] <= weak[k + offset] <= weak[j + temp] + agents[a_index] :
						count += 1
					else :
						temp = count
						a_index += 1
						offset -= 1
						if a_index >= len(agents):
							break
					if count >= weak_len :
						return i
					offset += 1
	return -1


#print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
#print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
#print(solution(200, [0, 10, 50, 80, 120, 160], [1, 10, 5, 40, 30]))
