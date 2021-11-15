from itertools import permutations

def solution(n, weak, dist):

	weak_origin_len = len(weak)

	for i in range(weak_origin_len):
		weak.append(weak[i] + n)

	workers_perms = permutations(dist, len(dist))
	worker_count = len(dist) + 1
	for workers in workers_perms:
		for i in range(weak_origin_len):
			weak_window = [weak[k] for k in range(i, i + weak_origin_len)]
			worker_idx = 0
			coverage = weak_window[0] + workers[worker_idx]
			for j in range(weak_origin_len) :
				if coverage < weak_window[j] :
					worker_idx += 1
					if worker_idx >= len(dist):
						break
					
					coverage = weak_window[j] + workers[worker_idx]
			worker_count = min(worker_count, worker_idx + 1)
	if worker_count > len(dist) :
		return -1
	return worker_count

questions = []

questions.append((12,
	[1, 5, 6, 10],
	[1, 2, 3, 4],
	2))
questions.append((12,
	[1, 3, 4, 9, 10],
	[3, 5, 7],
	1))
questions.append((200,
	[0, 100],
	[1, 1],
	2))
questions.append((200,
	[0, 10, 50, 80, 120, 160],
	[1, 10, 5, 40, 30],
	3))

for question in questions:
	print(solution(question[0], question[1], question[2]) == question[3])