package programmers;

import java.util.HashSet;
import java.util.Set;

public class Solution12981 {
	public int[] solution(int n, String[] words) {
		int[] answer = new int[2];

		Set<String> wordSet = new HashSet<>();
		String pre = words[0];
		wordSet.add(pre);
		int count = 0;
		boolean ok = true;
		for (int i = 1; i < words.length; i++) {
			count = i;
			if (wordSet.contains(words[i]) || (pre.charAt(pre.length() - 1) != words[i].charAt(0))) {
				ok = false;
				break;
			}
			wordSet.add(words[i]);
			pre = words[i];
		}
		if (ok)
			return answer;
		answer[0] = count % n + 1;
		answer[1] = count / n + 1;

		return answer;
	}
}
