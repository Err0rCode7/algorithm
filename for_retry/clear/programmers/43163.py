import sys

sys.setrecursionlimit(10000)

def is_only_diff_one_char(a, b):
	if len(a) != len(b):
		return False
	
	count = 0
	for i in range(len(a)):
		if a[i] != b[i]:
			count += 1
		if count > 1:
			return False
	return True

def dfs(visited, words, begin, target, _min, count):
	if begin == target:
		_min[0] = min(_min[0], count)
		return
	
	for word in words:
		if not is_only_diff_one_char(begin, word) or visited[word]:
			continue
		
		visited[word] = True
		dfs(visited, words, word, target, _min, count + 1)
		visited[word] = False
def solution(begin, target, words):
	visited = {}
	_min = [51]
	for word in words:
		visited[word] = False
	dfs(visited, words, begin, target, _min, 0)

	return _min[0] if _min[0] != 51 else 0

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))