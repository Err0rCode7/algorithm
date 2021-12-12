import heapq

def solution(play_time, adv_time, logs):

	def parse_time_to_second(time):
		return int(time[0:2]) * 3600 + int(time[3:5]) * 60 + int(time[6:8])

	def parse_log_to_second(log):
		start = parse_time_to_second(log[0:8])
		end = parse_time_to_second(log[9:17])
		return (start, end)
	
	def convert_second_to_date(second):
		hour = str(second // 3600).zfill(2)
		minute = str((second % 3600) // 60).zfill(2)
		second = str((second % 3600) % 60).zfill(2)
		return hour + ":" + minute + ":" + second
	
	play_time_sec = parse_time_to_second(play_time)
	adv_time_sec = parse_time_to_second(adv_time)
	logs_sec_heap = []
	for log in logs :
		start, end = parse_log_to_second(log)
		heapq.heappush(logs_sec_heap, (start, True))
		heapq.heappush(logs_sec_heap, (end, False))
	accum_user_count = [0] * (play_time_sec + 1)
	user_count = 0
	total = 0
	max_range = 0
	answer = 0
	for sec in range(play_time_sec + 1):
		while logs_sec_heap and logs_sec_heap[0][0] == sec:
			time, is_start = heapq.heappop(logs_sec_heap)
			if is_start:
				user_count += 1
			else:
				user_count -= 1
		total += user_count
		accum_user_count[sec] = total
		if sec >= adv_time_sec:
			new_range = accum_user_count[sec - 1]
			if sec != adv_time_sec:
				new_range -= accum_user_count[sec - adv_time_sec - 1]
			if max_range < new_range:
				max_range = new_range
				answer = sec - adv_time_sec

	return convert_second_to_date(answer)

print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
print(solution("99:59:59"	, "25:00:00"	, ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]	))
print(solution("50:00:00"		, "50:00:00"	, ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]		))

def solution_dp(play_time, adv_time, logs):

	def parse_time_to_second(time):
		return int(time[0:2]) * 3600 + int(time[3:5]) * 60 + int(time[6:8])

	def parse_log_to_second(log):
		start = parse_time_to_second(log[0:8])
		end = parse_time_to_second(log[9:17])
		return (start, end)
	
	def convert_second_to_date(second):
		hour = str(second // 3600).zfill(2)
		minute = str((second % 3600) // 60).zfill(2)
		second = str((second % 3600) % 60).zfill(2)
		return hour + ":" + minute + ":" + second
	
	play_time_sec = parse_time_to_second(play_time)
	adv_time_sec = parse_time_to_second(adv_time)
	user_count_in_time = [0] * (play_time_sec + 1)
	dp = [0] * (play_time_sec + 1)
	for log in logs:
		start, end = parse_log_to_second(log)
		dp[start] += 1
		dp[end] -= 1
	
	user_count = 0
	for i in range(play_time_sec + 1):
		user_count += dp[i]
		user_count_in_time[i] += user_count
	total = 0
	for i in range(0, adv_time_sec):
		total += user_count_in_time[i]

	answer = total
	answer_time = 0
	# two points
	for end in range(adv_time_sec, play_time_sec):
		start = end - adv_time_sec
		total = total - user_count_in_time[start] + user_count_in_time[end]
		if answer < total:
			answer = total
			answer_time = start + 1
	return convert_second_to_date(answer_time)

print(solution_dp("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
print(solution_dp("99:59:59"	, "25:00:00"	, ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]	))
print(solution_dp("50:00:00"		, "50:00:00"	, ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]		))

def solution_dp_with_range_sum(play_time, adv_time, logs):

	def parse_time_to_second(time):
		return int(time[0:2]) * 3600 + int(time[3:5]) * 60 + int(time[6:8])

	def parse_log_to_second(log):
		start = parse_time_to_second(log[0:8])
		end = parse_time_to_second(log[9:17])
		return (start, end)
	
	def convert_second_to_date(second):
		hour = str(second // 3600).zfill(2)
		minute = str((second % 3600) // 60).zfill(2)
		second = str((second % 3600) % 60).zfill(2)
		return hour + ":" + minute + ":" + second
	
	play_time_sec = parse_time_to_second(play_time)
	adv_time_sec = parse_time_to_second(adv_time)
	dp = [0] * (play_time_sec + 1)
	for log in logs :
		start, end = parse_log_to_second(log)
		dp[start] += 1
		dp[end] -= 1
	accum_user_count = [0] * (play_time_sec + 1)
	user_count = 0
	total = 0
	max_range = 0
	answer = 0
	for sec in range(play_time_sec + 1):
		user_count += dp[sec]
		total += user_count
		accum_user_count[sec] = total
		if sec >= adv_time_sec:
			new_range = accum_user_count[sec - 1]
			if sec != adv_time_sec:
				new_range -= accum_user_count[sec - adv_time_sec - 1]
			if max_range < new_range:
				max_range = new_range
				answer = sec - adv_time_sec

	return convert_second_to_date(answer)

print(solution_dp_with_range_sum("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
print(solution_dp_with_range_sum("99:59:59"	, "25:00:00"	, ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]	))
print(solution_dp_with_range_sum("50:00:00"		, "50:00:00"	, ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]		))