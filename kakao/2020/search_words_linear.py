words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

def is_same(query, word) :
	n = len(query)
	if n != len(word) :
		return False
	i = 0
	while i < n :
		if query[i] != '?' and query[i] != word[i]:
			return False
		i += 1
	return True

def solution(words, queries):
	answer = []
	for query in queries :
		count = 0
		for word in words :
			if is_same(query, word) :
				count += 1
		answer.append(count)
	return answer

print(solution(words, queries))





