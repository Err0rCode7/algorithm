package programmers;


public class Solution12899 {
	public String solution(int n) {
		StringBuilder answer = new StringBuilder();
		int[] base = {4, 1, 2};

		while (n != 0) {

			int q = n / 3;
			int r = n % 3;
			answer.insert(0, base[r]);
			if (r == 0)
				q -= 1;
			n = q;
		}
		return answer.toString();
	}
}
