def find_next_dir(before, after, start):
	# left 1, right 0
	cur = start + 1
	_min = 1e9
	move_right = 1
	while True:
		if cur >= len(before) - 1:
			cur = 1
		if after[cur] != before[cur]:
			_min = min(_min, move_right)
			break
		if start == cur:
			break
		move_right += 1
		cur += 1
	cur_left = cur
	cur = start - 1
	move_left = 1
	while True:
		if cur <= 0:
			cur = len(before) - 2
		if after[cur] != before[cur]:
			_min = min(move_left, _min)
			break
		if start == cur:
			break
		move_left += 1
		cur -= 1
	cur_right = cur
	if start == cur:
		return (0, 0, 0)
	if _min == move_left:
		return (1, cur_left, move_left)
	return (0, cur_right, move_right)

def solution(name):
	alpha = "0ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	alpha_len = 26
	alpha_dict = {}
	for i in range(alpha_len):
		alpha_dict[alpha[i + 1]] = i
	cur = 1

	before = ['A' for _ in range(len(name) + 2)]
	after = ['A' for _ in range(len(name) + 2)]
	for i in range(1, len(name) + 1):
		after[i] = name[i - 1]
	cur = 1
	move_count = 0
	while True:
		if after[cur] != 'A':

			move_count += min(alpha_dict[after[cur]], alpha_len - alpha_dict[after[cur]])
			before[cur] = after[cur]
		_dir, index, count = find_next_dir(before, after, cur)
		if count == 0:
			break
		cur = index
		move_count += count
		
	print(move_count)

	return move_count

solution("JEROEN")
solution("JAN")