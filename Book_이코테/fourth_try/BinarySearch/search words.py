import bisect

def count_by_range(iteration, left_value, right_value):
	left = bisect.bisect_left(iteration, left_value)
	right = bisect.bisect_right(iteration, right_value)
	return right - left


def solution(words, queries) :
	result = []
	words_by_len = [[] for _ in range(10001)]
	rev_words_by_len = [[] for _ in range(10001)]
	for word in words :
		words_by_len[len(word)].append(word)
		rev_words_by_len[len(word)].append(word[::-1])

	for i in range(10001):
		words_by_len[i].sort()
		rev_words_by_len[i].sort()

	for query in queries:
		if query[0] != '?':
			result.append(count_by_range(words_by_len[len(query)], query.replace('?', 'a'), query.replace('?', 'z')))
		else :
			result.append(count_by_range(rev_words_by_len[len(query)], query[::-1].replace('?', 'a'), query[::-1].replace('?', 'z')))

	return result

tcs =(["frodo", "front", "frost", "frozen", "frame", "kakao"],
	["fro??", "????o", "fr???", "fro???", "pro?"]
) # result [3, 2, 4, 1, 0]

print(solution(tcs[0], tcs[1]))