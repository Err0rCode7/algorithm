package programmers;

import java.util.PriorityQueue;

public class Solution42626 {
	public int solution(int[] scoville, int K) {
		PriorityQueue<Integer> heap = new PriorityQueue<>();
		for (int i : scoville) {
			heap.add(i);
		}

		int count = 0;
		while (!heap.isEmpty()) {
			Integer smallest = heap.poll();
			if (smallest >= K)
				return count;

			if (heap.isEmpty())
				return -1;

			Integer nextSmallest = heap.poll();
			heap.add(smallest + nextSmallest * 2);
			++count;
		}

		return -1;
	}
}
