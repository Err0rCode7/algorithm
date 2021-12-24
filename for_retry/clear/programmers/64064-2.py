from itertools import permutations

def solution(user_id, banned_id):
	perms = list(permutations(user_id, len(banned_id)))

	def equal(a, ban):
		if len(a) != len(ban):
			return False
		
		for i in range(len(a)):
			if ban[i] == '*':
				continue
			if ban[i] != a[i]:
				return False
		return True
	answer = set()
	
	def is_valid_users(users, bans):
		for i in range(len(bans)):
			if not equal(users[i], bans[i]) :
				return False
		return True
	answer = set()
	for users in perms:

		if is_valid_users(users, banned_id):
			users_set = frozenset(users)
			if users_set not in answer:
				answer.add(users_set)

	return len(answer)

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"]	, ["fr*d*", "abc1**"]	))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"]	, ["*rodo", "*rodo", "******"]	))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"]	, ["fr*d*", "*rodo", "******", "******"]	))