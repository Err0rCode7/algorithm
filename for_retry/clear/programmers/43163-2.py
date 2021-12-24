import sys

sys.setrecursionlimit(1000000)

def solution(begin, target, words):

	def is_different_only_one(src, dest):

		if len(src) != len(dest):
			return False
		count = 0
		for i in range(len(src)):
			if src[i] != dest[i]:
				count += 1
			if count > 1 :
				return False
		return True

	def dfs(begin, target, cost, words, used, used_count):

		if begin == target:
			return cost

		result = int(1e9)
		for i in range(len(words)):
			if used[i] or not is_different_only_one(begin, words[i]):
				continue

			used[i] = True
			result = min(result, dfs(words[i], target, cost + 1, words, used, used_count + 1))
			used[i] = False
		return result
	used = [0] * (len(words))
	answer = dfs(begin, target, 0, words, used, 0)
	if answer >= int(1e9):
		return 0
	return answer

print(solution("hit"	, "cog", ["hot", "dot", "dog", "lot", "log", "cog"]	))
print(solution("hit"	, "cog", ["hot", "dot", "dog", "lot", "log"]	))