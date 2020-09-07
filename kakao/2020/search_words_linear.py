# 구현 + 효율성 문제
# query에 해당하는 word가 몇개 인지 찾는 문제
# 문자는 소문자 알파벳과 '?'이 존재하며 '?'는 모든 소문자 알파벳을 대체할 수 있다.
# 2중 포문을 이용하여 길이를 비교하고 길이가 같으면 0번째 문자부터 마지막 문자까지 값이 같은지 비교한다.
# 효율성 4, 5번만 통과한 방식으로 낮은 점수를 얻었다.
# 자료구조 Trie에 대해 처음 알게 되었으며 효율성을 통과하는 코드를 구현해볼 수 있었다.
# 자료구조 Trie는 문자열 탐색을 할 때 사용되는 자료구조로 연결리스트 형태의 해쉬이다.
# 각 문자열에 한 문자씩 연결리스트 형태로 연결하여 문자열을 탐색할 수 있다.
# 추가로 이 문제에 trie를 사용하기 위해서는 '?'가 접두사(prefix)인 경우와 접미사(suffix)인 경우를 생각하여 해야하고
# 길이에 따라서 각각의 trie를 만들어야한다. 또한, query에 해당하는 문자열의 수를 알기 위해 trie depth마다 연결되어있는 자식들의 갯수를 저장해야한다.
# 접두사와 접미사를 해결하기 위해서는 한 개의 trie를 접두사용으로, 반대의 순서인 trie를 접미사용으로 만들어서 쿼리가 접미사로 들어올 때는 word의 순서를 reverse하여
# 접미사 trie에서 찾는 형태로 진행하여 문제를 풀 수 있다.

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





