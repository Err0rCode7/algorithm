def solution(lines):
	log_times = []
	START = -1
	END = -2
	for i in range(len(lines)):
		a, time, size = lines[i].split()
		to_second = float(time[0:2]) * 3600 + float(time[3:5]) * 60 + float(time[6:])
		size = float(size[:-1])
		log_times.append((to_second - size + 0.001, START))
		log_times.append((to_second, END))
	log_times.sort()
	s, e = 0, 0
	count = 0
	answer = 1
	while e < len(log_times):

		if log_times[e][0] - log_times[s][0] < 1.0:
			if log_times[e][1] == START:
				count += 1
			e += 1
		else :
			if log_times[s][1] == END:
				count -= 1
			s += 1
		answer = max(count, answer)

	return answer

print(solution([
"2016-09-15 01:00:04.001 2.0s",
"2016-09-15 01:00:07.000 2s"
]))

print(solution([
"2016-09-15 01:00:04.002 2.0s",
"2016-09-15 01:00:07.000 2s"
]))

print(solution([
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]
))

print(solution(["2016-09-15 23:59:59.999 0.001s"]))