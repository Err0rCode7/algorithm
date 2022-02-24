package programmers;

import java.util.Deque;
import java.util.LinkedList;

public class Solution42584 {
	public int[] solution(int[] prices) {
		Deque<int[]> stack = new LinkedList<>();

		int[] times = new int[prices.length];
		for (int i = 0; i < prices.length; i++) {
			times[i] = prices .length - i - 1;
			while (!stack.isEmpty()) {
				if (stack.peekLast()[1] > prices[i]){
					int[] timePrice = stack.pollLast();
					times[timePrice[0]] = i - timePrice[0];
					continue;
				}
				break;
			}
			stack.addLast(new int[]{i, prices[i]});
		}

		while (!stack.isEmpty()) {
			int[] timePrice = stack.pollLast();
			times[timePrice[0]] = prices.length - 1 - timePrice[0];
		}

		return times;
	}
}
