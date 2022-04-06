package programmers;

import static java.lang.Math.*;

public class Main12904 {
	static class Solution {
		public int solution(String s){
			int answer = 1;

			for (int i = 0; i < s.length(); i++) {

				int l1 = i - 1, r1 = i + 1, l2 = i - 1, r2 = i;
				int answer1 = 1;
				int answer2 = 0;
				boolean flag1 = false;
				boolean flag2 = false;
				while (true) {
					if (flag1 && flag2)
						break;
					if (l1 >= 0 && r1 < s.length() && s.charAt(l1) == s.charAt(r1)) {
						answer1 += 2;
					} else {
						flag1 = true;
					}

					if (l2 >= 0 && r2 < s.length() && s.charAt(l2) == s.charAt(r2)) {
						answer2 += 2;
					} else {
						flag2 = true;
					}

					l1 -= 1; l2 -= 1;
					r1 += 1; r2 += 1;
				}
				answer = max(answer, answer1);
				answer = max(answer, answer2);
			}
			return answer;
		}
	}
}


