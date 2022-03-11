package programmers;

import java.util.ArrayList;
import java.util.List;

public class Solution42586 {
	public int[] solution(int[] progresses, int[] speeds) {
		if (speeds.length == 0)
			return new int[]{};

		List<Integer> result = new ArrayList<>();
		int threshold = (100 - progresses[0]) / speeds[0] + ((100 - progresses[0]) % speeds[0] > 0 ? 1 : 0);
		int count = 1;
		for (int i = 1; i < progresses.length; i++) {
			int cur = (100 - progresses[i]) / speeds[i] + ((100 - progresses[i]) % speeds[i] > 0 ? 1 : 0);

			if (cur > threshold) {
				result.add(count);
				threshold = cur;
				count = 1;
			} else {
				count++;
			}
		}
		result.add(count);
		return result.stream().mapToInt(Integer::intValue).toArray();
	}
}