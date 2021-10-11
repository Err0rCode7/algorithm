from itertools import permutations


def solution(n, weak, dist):

	weak_len = len(weak)

	for i in range(weak_len):
		weak.append(weak[i] + n)

	answer = len(dist) + 1
	for i in range(1, weak_len):
		perm = permutations(dist, i)
		start_point = [weak[j] for j in range(i, i + weak_len)]
		for agents in perm:
			count, agents_idx = 1, 0
			point = start_point[0] + agents[agents_idx]
			for idx in range(weak_len):
				if point < start_point[idx]:
					count += 1
					if count > len(agents):
						break
					agents_idx += 1
					point = start_point[idx] + agents[agents_idx]
			answer = min(answer, count)

	if answer > len(dist):
		return (-1)
	return (answer)

test_case = [(12, [1, 5, 6, 10], [1, 2, 3, 4]), (12, [1, 3, 4, 9, 10], [3, 5, 7])]

for a, b, c in test_case:
	print(solution(a, b, c))
