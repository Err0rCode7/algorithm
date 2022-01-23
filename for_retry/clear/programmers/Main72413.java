package programmers;

import static java.lang.Integer.*;

public class Main72413 {
	public static void main(String[] args) {
		int result = new Solution().solution(6, 4, 6, 2, new int[][] {
			{4, 1, 10}, {3, 5, 24}, {5, 6, 2}, {3, 1, 41}, {5, 1, 24}, {4, 6, 50}, {2, 4, 66}, {2, 3, 22}, {1, 6, 25}
		});
		System.out.println(result);
		result = new Solution().solution(7, 3, 4, 1, new int[][] {
			{5, 7, 9}, {4, 6, 4}, {3, 6, 1}, {3, 2, 3}, {2, 1, 6}
		});
		System.out.println(result);
		result = new Solution().solution(6, 4, 5, 6, new int[][] {
			{2, 6, 6}, {6, 3, 7}, {4, 6, 7}, {6, 5, 11}, {2, 5, 12}, {5, 3, 20}, {2, 4, 8}, {4, 3, 9}
		});
		System.out.println(result);
	}
	static class Solution {
		public int solution(int n, int s, int a, int b, int[][] fares) {

			int[][] graph = new int[n + 1][n + 1];
			for (int i = 0; i < n + 1; i++) {
				for (int j = 0; j < n + 1; j++) {
					if (i == j)
						graph[i][j] = 0;
					else
						graph[i][j] = MAX_VALUE;
				}
			}
			for (int[] fare : fares) {
				graph[fare[0]][fare[1]] = fare[2];
				graph[fare[1]][fare[0]] = fare[2];
			}
			for (int k = 1; k < n + 1; k++) {
				for (int i = 1; i < n + 1; i++) {
					for (int j = 1; j < n + 1; j++) {
						if (graph[i][k] != MAX_VALUE && graph[k][j] != MAX_VALUE)
							graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j]);
					}
				}
			}
			int answer = MAX_VALUE;
			for (int i = 1; i < n + 1; i++) {
				if (graph[s][i] != MAX_VALUE && graph[i][a] != MAX_VALUE && graph[i][b] != MAX_VALUE)
					answer = min(answer, graph[s][i] + graph[i][a] + graph[i][b]);
			}

			return answer;
		}
	}
}

