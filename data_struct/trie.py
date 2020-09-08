# 자료구조 Trie

# 문자열을 저장하고 빠른 탐색을 하기 위해 사용된다.
# 2중 for문인 O(n^2) 보다 훨씬 빠르게 찾을 수 있고 해쉬보단 조금 느리지만 공간복잡도를 줄일 수 있는 자료구조

# 연길 리스트의 형태로 python에서는 딕셔너리를 이용한다. 마지막 값에 마지막 표식을 저장한다.
# 연결 리스트 해쉬의 형태라고 생각하면 편하다.
# hello를 저장하면 {'h': {'e': {'l': {'l': {'o': {'*'}}}}}} 의 형태로 저장된다.

class Trie :
	head = {}

	def add(self, word):
		cur = self.head

		for ch in word:
			if ch not in cur:
				cur[ch] = {}
			cur = cur[ch]
		cur['*'] = True

	def search(self, word) :
		cur = self.head

		for ch in word :
			if ch not in cur :
				return False
			cur = cur[ch]
		return ('*' in cur)

dictionary = Trie()

dictionary.add("hi")
dictionary.add("hello")
print(dictionary.search("hi"))
print(dictionary.search("hello"))
print(dictionary.search("hel"))
print(dictionary.search("hey"))
