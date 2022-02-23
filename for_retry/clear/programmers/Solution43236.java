package programmers;

import java.util.Arrays;

public class Solution43236 {
	public int solution(int distance, int[] rocks, int n) {
		Arrays.sort(rocks);

		int s = 1;
		int e = 1_000_000_000;
		int answer = 0;
		while (s <= e) {
			int mid = (s + e) / 2;
			int pre = 0;
			int count = 0;
			for (int rock : rocks) {
				if (rock - pre < mid) {
					count += 1;
				} else {
					pre = rock;
				}
			}

			if (distance - pre < mid) {
				count += 1;
			}

			if (count > n) {
				e = mid - 1;
			} else {
				s = mid + 1;
				answer = Math.max(answer, mid);
			}
		}

		return answer;
	}
}
