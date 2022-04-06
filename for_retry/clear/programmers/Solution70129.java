package programmers;

import java.util.*;

public class Solution70129 {
	private int count = 0;
	private int depth = 0;
	public int[] solution(String s) {

		while (!s.equals("1")) {
			depth++;
			int size = 0;
			for (int i = 0; i < s.length(); i++) {
				if (s.charAt(i) == '1')
					size++;
				else
					count++;
			}

			StringBuilder sb = new StringBuilder();

			while (true) {
				sb.append(size % 2);
				size /= 2;
				if (size == 0)
					break;
			}

			s = sb.reverse().toString();
		}
		return new int[]{depth, count};
	}
}