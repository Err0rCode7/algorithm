package programmers;

import java.util.Comparator;
import java.util.LinkedList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Queue;

public class Solution42627 {
	public int solution(int[][] jobs) {
		Queue<int[]> heap = new PriorityQueue<>((o1, o2) -> {
			if (o1[0] - o2[0] == 0)
				return o1[1] - o2[1];
			return o1[0] - o2[0];
		});

		for (int i = 0; i < jobs.length; i++) {
			int start = jobs[i][0];
			int time = jobs[i][1];

			heap.add(new int[]{start, time});
		}

		int curTime = 0;
		int result = 0;
		List<int[]> wait = new LinkedList<>();
		while (!heap.isEmpty()) {

			while (!heap.isEmpty() && heap.peek()[0] < curTime) {
				wait.add(heap.poll());
			}

			int[] selected;
			if (wait.size() > 0) {
				wait.sort(Comparator.comparingInt(o -> o[1]));
				selected = wait.remove(0);
				heap.addAll(wait);
				wait.clear();
			} else {
				selected = heap.poll();
			}

			int start = selected[0];
			int time = selected[1];

			int waitTime = 0;
			if (curTime > start) {
				waitTime = curTime - start;
			}
			result += time + waitTime;
			curTime = start + time + waitTime;
		}
		return result / jobs.length;
	}

	private static class Solution {
		public int solution(int[][] jobs) {

			Queue<Job> heap = new PriorityQueue<>((o1, o2) -> o1.requestTime - o2.requestTime);
			for (int[] job : jobs) {
				heap.add(new Job(job[0], job[1]));
			}

			int curTime = 0;
			int answer = 0;
			Queue<Job> buffer = new PriorityQueue<>((o1, o2) -> o1.time - o2.time);
			while (!heap.isEmpty()) {
				while (!heap.isEmpty() && heap.peek().requestTime <= curTime) {
					buffer.add(heap.poll());
				}

				if (!buffer.isEmpty()) {
					Job job = buffer.poll();
					answer += (curTime - job.requestTime) + job.time;
					curTime += job.time;
					while (!buffer.isEmpty()) {
						heap.add(buffer.poll());
					}
				} else {
					curTime = heap.peek().requestTime;
				}
			}
			return answer / jobs.length;
		}

		private static class Job {
			int requestTime;
			int time;

			public Job(int requestTime, int time) {
				this.requestTime = requestTime;
				this.time = time;
			}
		}
	}
}