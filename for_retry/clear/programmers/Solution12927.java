package programmers;

import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Queue;

public class Solution12927 {
	public long solution(int n, int[] works) {

		Map<Integer, Integer> map = new HashMap<>();

		for (int work : works) {
			if (map.containsKey(work))
				map.replace(work, map.get(work) + 1);
			else
				map.put(work, 1);
		}

		Queue<int[]> maxHeap = new PriorityQueue<>((o1, o2) -> o2[0] - o1[0]);
		for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
			maxHeap.add(new int[] {entry.getKey(), entry.getValue()});
		}

		while (!maxHeap.isEmpty() && n > 0) {
			int[] poll = maxHeap.poll();
			int height = !maxHeap.isEmpty() ? poll[0] - maxHeap.peek()[0] :
				poll[0];
			int allCycleCost = height * poll[1];

			if (n >= allCycleCost) {
				if (poll[0] != height) {
					poll[0] -= height;
					maxHeap.peek()[1] += poll[1];
				}
				n -= allCycleCost;
			} else {
				int count = n / poll[1];
				int r = n % poll[1];
				n = 0;
				poll[0] -= count;
				if (!maxHeap.isEmpty()) {
					if (1 + count == height) {
						maxHeap.peek()[1] += r;
					} else {
						maxHeap.add(new int[] {poll[0] - 1, r});
					}
				} else {
					if (poll[0] - 1 > 0) {
						maxHeap.add(new int[] {poll[0] - 1, r});

					}
				}
				poll[1] -= r;
				if (poll[1] != 0) {
					maxHeap.add(poll);
				}
			}
		}
		long answer = 0;
		for (int[] poll : maxHeap) {
			answer += ((long)Math.pow(poll[0], 2) * poll[1]);
		}
		return answer;
	}
}