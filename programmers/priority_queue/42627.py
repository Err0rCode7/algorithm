import heapq

def get_process_time(wait, time):
	start, job = wait
	per_time = 0
	if start > time :
		time = start
	elif time > start:
		per_time += time - start
	per_time += job
	return per_time

def solution(jobs):
	heapq.heapify(jobs)
	n = len(jobs)
	time = 0
	take = 0
	while jobs:
		wait = []
		while jobs and jobs[0][0] <= time:
			wait.append(heapq.heappop(jobs))
		if not wait :
			time = jobs[0][0]
			continue
		if len(wait) > 1 :
			wait.sort(key=lambda x: (x[1], x[0]))
			for i in range(1, len(wait)):
				heapq.heappush(jobs, wait[i])
		take += get_process_time(wait[0], time)
		time += wait[0][1]
	return int(take / n)

print(solution([[0, 3], [1, 9], [2, 6]]))