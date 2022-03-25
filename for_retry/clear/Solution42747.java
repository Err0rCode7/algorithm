package programmers;

import java.util.*;

public class Solution42747 {
	public int solution(int[] citations) {
		int answer = 0;

		Integer[] array = Arrays.stream(citations).boxed().sorted((o1, o2) -> o2 - o1).toArray(Integer[]::new);

		int max = array[0];
		int min = array[array.length - 1];

		for (int i = max; i >= 0; --i) {
			int right = bSearch(array, i - 1);
			if (right >= i && array.length - right <= i) {
				answer = i;
				break;
			}
		}
		return answer;
	}

	private int bSearch(Integer[] array, int target) {
		int s = 0;
		int e = array.length;

		while (s < e) {
			int m = s + (e - s) / 2;

			if (array[m] <= target) {
				e = m;
			} else {
				s = m + 1;
			}

		}
		return s;
	}
}
