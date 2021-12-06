def solution(gems):

	gem_ids = set(gems)
	
	s, e = 0, 0

	answer = []
	gems_dict = {}
	cur_set = set()
	_mindist = 1e9
	flag = True
	while s < len(gems) and e < len(gems):
		if flag:
			flag = False
			if gems[e] not in cur_set:
				gems_dict[gems[e]] = 1
				cur_set.add(gems[e])
			else:
				gems_dict[gems[e]] += 1
		if len(cur_set) == len(gem_ids):
			if _mindist > abs(e - s):
				_mindist = abs(e - s)
				answer = [s, e]
		else :
			e += 1
			flag = True
			continue

		if gems_dict[gems[s]] == 1:
			gems_dict[gems[s]] = 0
			cur_set.remove(gems[s])
		else :
			gems_dict[gems[s]] -= 1
		s += 1
	answer[0] += 1
	answer[1] += 1
	return answer


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]	))
print(solution(["AA", "AB", "AC", "AA", "AC"]	))
print(solution(["XYZ", "XYZ", "XYZ"]	))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]	))
print(solution(["DIA","EM", "EM", "RUB", "DIA"])) # 3, 5
print(solution(["A","A","A","B","B"])) # 3, 4
print(solution(["A"])) # 1, 1
print(solution(["A","B","B","B","B","B","B","C","B","A"])) # 8, 10