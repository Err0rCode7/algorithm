from bisect import bisect_left, bisect_right


def count_by_value(iter, left_value, right_value) :

	left = bisect_left(iter, left_value)
	right = bisect_right(iter, right_value)
	return right - left


def solution(words, queries) :

	array = [[] for _ in range(10001)]
	reversed_array = [[] for _ in range(10001)]

	for word in words :
		array[len(word)].append(word)
		reversed_array[len(word)].append(word[::-1])

	for i in range(10001) :
		array[i].sort()
		reversed_array[i].sort()

	answer = []
	for query in queries :
		if query[0] != '?':
			res = count_by_value(array[len(query)], query.replace('?', 'a'), query.replace('?', 'z'))
		else :
			res = count_by_value(reversed_array[len(query)], query[::-1].replace('?', 'a'), query[::-1].replace('?', 'z'))
		answer.append(res)
	return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))
