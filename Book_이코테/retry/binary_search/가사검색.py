import bisect

def	count_by_value(array, left_value, right_value):
	left = bisect.bisect_left(array, left_value)
	right = bisect.bisect_right(array, right_value)
	return (right - left)

def solution(words, queries):

	result = []
	words_list = [[] for i in range(10001)]

	rev_words_list = [[] for i in range(10001)]
	for string in words:
		words_list[len(string)].append(string)
		rev_words_list[len(string)].append(string[::-1])

	for i in range(10001):
		words_list[i].sort()
		rev_words_list[i].sort()

	for query in queries:
		if query[0] != '?':
			result.append(count_by_value(words_list[len(query)],
							query.replace('?', 'a'), query.replace('?', 'z')))
		else:
			query = query[::-1]
			result.append(count_by_value(rev_words_list[len(query)],
							query.replace('?', 'a'), query.replace('?', 'z')))
	return (result)

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))
