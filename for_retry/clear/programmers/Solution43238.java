package programmers;

import java.util.*;

public class Solution43238 {
	public long solution(int n, int[] times) {
		long s = 0;
		long e = 1_000_000_000L * 1_000_000_000L;

		long answer = 1_000_000_000L * 1_000_000_000L;
		while (s <= e) {

			long count = 0;
			long mid = (s + e) / 2;
			for (int i = 0; i < times.length; i++) {
				count += mid / times[i];
			}

			if (n <= count) {
				answer = Math.min(mid, answer);
				e = mid - 1;
			} else {
				s = mid + 1;
			}
		}
		return answer;
	}
}
