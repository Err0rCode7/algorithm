package programmers;

public class Solution87946 {
	private int answer;
	public int solution(int k, int[][] dungeons) {
		answer = 0;

		countDungeonMax(dungeons, 0, k, new boolean[dungeons.length]);
		return answer;
	}

	private void countDungeonMax(int[][] dungeons, int depth, int tiredPoint, boolean[] visited) {
		answer = Math.max(answer, depth);
		if (depth == dungeons.length)
			return;
		for (int i = 0; i < dungeons.length; i++) {
			if (visited[i]) continue;
			if (tiredPoint < dungeons[i][0]) continue;

			visited[i] = true;
			countDungeonMax(dungeons, depth + 1, tiredPoint - dungeons[i][1], visited);
			visited[i] = false;
		}
	}
}