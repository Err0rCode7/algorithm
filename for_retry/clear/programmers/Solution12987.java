package programmers;

import java.util.Arrays;
import java.util.Deque;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;

public class Solution12987 {
	public int solution(int[] A, int[] B) {
		int N = A.length;
		Arrays.sort(B);
		Arrays.sort(A);

		int idxA = 0;
		int idxB = 0;
		int count = 0;

		while (idxA < N && idxB < N) {
			if (B[idxB] > A[idxA]) {
				++count;
				++idxB;
				++idxA;
			} else {
				++idxB;
			}
		}

		return count;
	}

	static class Solution2 {
		public int solution(int[] A, int[] B) {

			Queue<Integer> maxHeap = new PriorityQueue<>((o1, o2) -> o2 - o1);
			Deque<Integer> que = new LinkedList<>();
			int N = A.length;
			Arrays.sort(B);
			for (int i = 0; i < N; i++) {
				maxHeap.add(A[i]);
				que.add(B[i]);
			}
			int count = 0;
			for (int i = 0; i < N; i++) {
				Integer aPoll = maxHeap.poll();
				if (aPoll >= que.peekLast()) {
					que.pollFirst();
				} else {
					++count;
					que.pollLast();
				}
			}

			return count;
		}
	}
}