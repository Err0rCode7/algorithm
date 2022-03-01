package programmers;

import java.util.HashSet;
import java.util.Set;

public class Solution42839 {
	// private Map<String, Boolean> cache;
	private Set<String> cache;
	public int solution(String numbers) {
		int MAX = 9999999;
		int[] primeNumbers = new int[MAX + 1];

		for (int i = 1; i < primeNumbers.length; i++) {
			primeNumbers[i] = i;
		}

		primeNumbers[1] = 0;
		for (int i = 2; i < primeNumbers.length; i++) {

			if (primeNumbers[i] == 0)
				continue;
			for (int j = i*2; j < primeNumbers.length && j > 0; j += i) {
				primeNumbers[j] = 0;
			}
		}
		cache = new HashSet<>();
		int answer = dfs(new boolean[numbers.length()], "", numbers, primeNumbers, 0);
		return answer;
	}

	public int dfs(boolean[] visited, String number, String numbers, int[] primeNumbers, int size) {
		int result = 0;
		int cur = 0;
		if (number.length() != 0)
			cur = Integer.parseInt(number);
		if (primeNumbers[cur] != 0) {
			primeNumbers[cur] = 0;
			result += 1;
		}
		if (size >= numbers.length()) {
			return result;
		}

		for (int i = 0; i < numbers.length(); i++) {
			if (visited[i]) continue;

			String next = number + numbers.charAt(i);
			if (!cache.contains(next)) {
				visited[i] = true;
				cache.add(next);
				result += dfs(visited, next, numbers, primeNumbers, size + 1);
				visited[i] = false;
			}

			// next = number + (int)((numbers.charAt(i) - '0') * Math.pow(10, size));
			// if (cache.contains(next)) continue;
			// visited[i] = true;
			// cache.add(next);
			// result += dfs(visited, next, numbers, primeNumbers, size + 1);
			// visited[i] = false;
		}
		return result;
	}
}
