package programmers;

public class Solution60062 {
	private static int[] cycleWeak;
	private static int[] dist;
	private static int answer;
	public int solution(int n, int[] weak, int[] dist) {
		answer = Integer.MAX_VALUE;
		cycleWeak = new int[weak.length * 2];
		Solution60062.dist = dist;
		for (int i = 0; i < cycleWeak.length; i++) {
			if (i >= weak.length) {
				cycleWeak[i] = weak[i % weak.length] + n;
			} else {
				cycleWeak[i] = weak[i];
			}
		}

		for (int i = 0; i < weak.length; i++) {
			boolean[] selected = new boolean[dist.length];
			dfs(i, 0, selected, 0);
		}
		if (answer == Integer.MAX_VALUE)
			return -1;
		return answer;
	}

	public void dfs(int start, int removedWeakSize, boolean[] selected, int depth) {
		if (cycleWeak.length / 2 <= removedWeakSize) {
			answer = Math.min(answer, depth);
			return;
		}

		for (int i = 0; i < dist.length; i++) {
			if (selected[i])
				continue;
			int threshold = cycleWeak[start] + dist[i];
			int count = 1;
			for (int curIdx = start + 1; curIdx < cycleWeak.length; curIdx++) {
				if (cycleWeak[curIdx] <= threshold) {
					count += 1;
				} else
					break;
			}

			int newStart = start + count;
			selected[i] = true;
			dfs(newStart, removedWeakSize + count, selected, depth + 1);
			selected[i] = false;
		}
	}
}