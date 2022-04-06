package programmers;

import java.util.LinkedList;
import java.util.Queue;

public class Solution42587 {
	public int solution(int[] priorities, int location) {
		Queue<int[]> que = new LinkedList<>();
		int[] counts = new int[10];
		int maxPriority = 0;
		for (int i = 0; i < priorities.length; i++) {
			que.add(new int[]{i, priorities[i]});
			counts[priorities[i]] += 1;
			if (maxPriority < priorities[i])
				maxPriority = priorities[i];
		}

		int answer = 1;
		while (!que.isEmpty()) {
			if (counts[maxPriority] <= 0) {
				maxPriority -= 1;
				continue;
			}

			int[] poll = que.poll();

			if (poll[1] != maxPriority) {
				que.add(poll);
				continue;
			}

			if (poll[0] == location)
				break;

			counts[maxPriority] -= 1;

			answer += 1;
		}
		return answer;
	}
}