package programmers;

public class Solution49191 {
	public int solution(int n, int[][] results) {
		boolean[][] graph = new boolean[n + 1][n + 1];

		for (int[] result : results) {
			graph[result[0]][result[1]] = true;
		}

		for (int k = 1; k < n + 1; k++) {
			for (int a = 1; a < n + 1; a++) {
				if (!graph[a][k]) continue;
				for (int b = 1; b < n + 1; b++) {
					if (graph[a][k] && graph[k][b])
						graph[a][b] = true;
				}
			}
		}

		int answer = 0;
		for (int a = 1; a < n + 1; a++) {
			int count = 0;
			for (int b = 1; b < n + 1; b++) {
				if (a == b) continue;

				if (graph[a][b] || graph[b][a])
					count += 1;
				else
					break;
			}
			if (count == n - 1)
				++answer;
		}

		return answer;
	}
}
