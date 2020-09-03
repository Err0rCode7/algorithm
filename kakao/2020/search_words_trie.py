
words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

class node :

	def __init__(self, val) :
		self.val = val
		self.child = {}
		self.count = 0

def add(parent, word) :
	cur = parent
	for ch in word :
		if ch not in cur.child :
			cur.child[ch] = node(ch)
		cur.count += 1
		cur = cur.child[ch]
	cur.child['*'] = True

def search(parent, word) :
	cur = parent

	for c in word :
		if '?' == c :
			break
		if c not in cur.child :
			return 0
		cur = cur.child[c]
	return cur.count

def solution(words, queries):

	trie_list = [node(None) for _ in range(int(1e5))]
	trie_list_rev = [node(None) for _ in range(int(1e5))]
	answer = []
	for word in words :
		add(trie_list[len(word)], word)
		add(trie_list_rev[len(word)], word[::-1])

	for query in queries :
		if query[0] == '?' :
			answer.append(search(trie_list_rev[len(query)], query[::-1]))
		else :
			answer.append(search(trie_list[len(query)], query))
	return answer

print(solution(words, queries))





