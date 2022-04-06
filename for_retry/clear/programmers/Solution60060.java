package programmers;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class Solution60060 {
	public int[] solution(String[] words, String[] queries) {

		Trie front = new Trie();
		Trie back = new Trie();

		for (String word : words) {
			front.insert(word);
			back.insert(reverse(word));
		}

		return Arrays.stream(queries).mapToInt(
			query -> query.charAt(0) == '?' ?
				back.find(reverse(query), 0) :
				front.find(query, 0)).toArray();
	}

	public String reverse(String s) {
		return new StringBuilder(s).reverse().toString();
	}

	public static class Trie {
		Map<Integer, Integer> lenMap = new HashMap<>();
		Trie[] child = new Trie[26];

		public void insert(String s) {
			Trie node = this;

			lenMap.put(s.length(), lenMap.getOrDefault(s.length(), 0) + 1);

			for (char c : s.toCharArray()) {
				int idx = c - 'a';
				if (node.child[idx] == null) {
					node.child[idx] = new Trie();
				}

				node = node.child[idx];
				node.lenMap.put(s.length(), node.lenMap.getOrDefault(s.length(), 0) + 1);
			}
		}

		public int find(String s, int i) {
			if (s.charAt(i) == '?')
				return lenMap.getOrDefault(s.length(), 0);

			int idx = s.charAt(i) - 'a';
			return child[idx] == null ? 0 : child[idx].find(s, i + 1);
		}
	}

	private class Solution_2 {
		public int[] solution(String[] words, String[] queries) {

			Trie[] tries = new Trie[10001];
			Trie[] rTries = new Trie[10001];
			for (int i = 1; i < 10001; i++) {
				tries[i] = new Trie(0, new HashMap<>());
				rTries[i] = new Trie(0, new HashMap<>());
			}
			StringBuilder stringBuilder = new StringBuilder();
			for (String word : words) {
				tries[word.length()].insert(word, 0);
				rTries[word.length()].insert(
					stringBuilder.insert(0, word).reverse().toString(), 0);
				stringBuilder.setLength(0);
			}
			int[] answer = new int[queries.length];
			for (int i = 0; i < queries.length; i++) {
				String query = queries[i];
				if (query.startsWith("?")) {
					answer[i] = rTries[query.length()].search(
						stringBuilder.insert(0, query).reverse().toString(), 0);
					stringBuilder.setLength(0);
				} else {
					answer[i] = tries[query.length()].search(query, 0);
				}
			}

			return answer;
		}

		class Trie {
			int count;
			Map<Character, Trie> trieMap;

			public Trie(int count, Map<Character, Trie> trieMap) {
				this.count = count;
				this.trieMap = trieMap;
			}

			public void insert(String s, int i) {
				if (s.length() == i) {
					return;
				}
				this.count += 1;
				Character c = s.charAt(i);
				Trie next = trieMap.computeIfAbsent(c,
					key -> new Trie(0, new HashMap<>())
				);

				next.insert(s, i + 1);
			}

			public int search(String s, int i) {
				char c = s.charAt(i);
				if (s.charAt(i) =='?') {
					return count;
				} else {

					if (trieMap.containsKey(c))
						return trieMap.get(c).search(s, i + 1);
				}
				return 0;
			}
		}
	}
}

