package programmers;

import java.util.Deque;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Set;

public class Solution76502 {
	public int solution(String s) {
		Deque<Character> que = new LinkedList<>();

		for (int i = 0; i < s.length(); i++) {
			que.add(s.charAt(i));
		}

		Deque<Character> stack = new LinkedList<>();
		Set<String> set = new HashSet<>();
		StringBuilder stringBuilder = new StringBuilder();
		for (int i = 0; i < s.length(); i++) {
			que.addLast(que.pollFirst());
			int leftCount = 0;
			for (Character c : que) {
				if (c == '{' || c == '[' || c == '(') {
					stack.addLast(c);
				} else {

					if (stack.isEmpty())
						break;
					if ((stack.peekLast() == '{' && c == '}')
						|| (stack.peekLast() == '(' && c == ')')
						|| (stack.peekLast() == '[' && c == ']')) {
						stack.pollLast();
					} else {
						break;
					}
				}
				stringBuilder.append(c);
			}
			if (stack.isEmpty() && stringBuilder.length() == s.length())
				set.add(stringBuilder.toString());
			stringBuilder.setLength(0);
			stack.clear();
		}
		return set.size();
	}
}
