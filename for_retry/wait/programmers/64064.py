import bisect

def count_by_range(iter, left, right):

	left = bisect.bisect_left(iter, left)
	right = bisect.bisect_right(iter, right)
	return right - left


def solution(user_id, banned_id):

	user_id.sort()
	banned_id.sort()
	user_counts_by_banned = []
	users = [[] for _ in range(9)]
	users_reverse = [[] for _ in range(9)]
	for i in range(len(user_id)):
		users[len(user_id[i])].append(user_id[i])
		users_reverse[len(user_id[i])].append(user_id[i][::-1])
	
	for i in range(9):
		users[i].sort()
		users_reverse[i].sort()

	for i in range(len(banned_id)):
		left = banned_id[i].replace('*', '0')
		right = banned_id[i].replace('*', 'z')
		count = 0
		_users = []
		if banned_id[i][0] == '*':
			left = left[::-1]
			right = right[::-1]
			count = count_by_range(users_reverse[len(banned_id[i])], left, right)
			left = bisect.bisect_left(users_reverse[len(banned_id[i])], left)
			_users = users_reverse[len(banned_id[i])][left:left + count]
			for j in range(len(_users)):
				_users[j] = _users[j][::-1]
		else :
			count = count_by_range(users[len(banned_id[i])], left, right)
			left = bisect.bisect_left(users[len(banned_id[i])], left)
			_users = users[len(banned_id[i])][left:left + count]
		
		user_counts_by_banned.append((count, _users))

	dups = [[0, False, []] for i in range(len(banned_id))]
	for i in range(len(banned_id)):
		dups[i][2].append(i)
		for j in range(len(banned_id)):
			if banned_id[i] == banned_id[j] and i != j:
				dups[i][0] += 1
				dups[j][0] += 1
				dups[i][2].append(j)

	result = 1

	for i in range(len(user_counts_by_banned)):
		count, users = user_counts_by_banned[i]
		if dups[i][1] == False:
			if dups[i][0] > 0:
				count = count // dups[i][0]
				for index in dups[i][2]:
					dups[index][1] = True
			if count != 0:
				result *= count

	for user in user_id:
		dup_count = -1

		for i in range(len(user_counts_by_banned)):
			count, users = user_counts_by_banned[i]

			if dups[i][0] != 0:
				continue
			if user in users:
				dup_count += 1
		if dup_count > 0:
			result -= dup_count
	return result

tc = [
	[
		["frodo", "fradi", "crodo", "abc123", "frodoc"],
	["fr*d*", "abc1**"]
	],
	[
		["frodo", "fradi", "crodo", "abc123", "frodoc"],
		["*rodo", "*rodo", "******"]
	],
	[
		["frodo", "fradi", "crodo", "abc123", "frodoc"],
		["fr*d*", "*rodo", "******", "******"]
	]
]
for a, b in tc:
	print(solution(a, b))
