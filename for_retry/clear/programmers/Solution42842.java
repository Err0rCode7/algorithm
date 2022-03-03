package programmers;

import java.util.ArrayList;
import java.util.List;

public class Solution42842 {
	public int[] solution(int brown, int yellow) {
		int[] answer = {0, 0};
		double sqrt = Math.sqrt(yellow);
		List<Integer> modZeroList = new ArrayList<>();
		for (int i = 1; i <= sqrt; i++) {
			if (yellow % i == 0)
				modZeroList.add(i);

		}

		for (Integer height : modZeroList) {
			int width = yellow / height;
			int result = (width + 2) * 2 + height * 2;
			if (result == brown) {
				answer[0] = width + 2;
				answer[1] = height + 2;
				break;
			}
		}

		return answer;
	}
}