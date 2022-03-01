package programmers;

import java.util.Arrays;

public class Solution42885 {
	public int solution(int[] people, int limit) {

		Arrays.sort(people);

		int s = 0;
		int e = people.length - 1;
		int answer = 0;
		while (s <= e) {

			if (s == e) {
				answer += 1;
				break;
			}

			if (people[s] + people[e] <= limit) {
				s += 1;
				e -= 1;
			} else {
				e -= 1;
			}
			answer += 1;
		}
		return answer;
	}
}
