package programmers;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution1837 {

	public int solution(int n, int m, int[][] edge_list, int k, int[] gps_log) {

		List<Integer>[] graph = new List[n + 1];
		for (int i = 1; i < n + 1; i++) {
			graph[i] = new ArrayList<>();
		}

		for (int[] edge : edge_list) {
			graph[edge[1]].add(edge[0]);
			graph[edge[0]].add(edge[1]);
		}

		int[][] dp = new int[k][n + 1];
		for (int i = 0; i < k; i++) {
			Arrays.fill(dp[i], Integer.MAX_VALUE);
		}
		dp[0][1] = 0;
		for (int i = 1; i < k; i++) {
			for (int j = 1; j < n + 1; j++) {
				dp[i][j] = Math.min(dp[i][j], dp[i - 1][j]);
				for (Integer pre : graph[j]) {
					if (dp[i - 1][pre] == Integer.MAX_VALUE) continue;
					dp[i][j] = Math.min(dp[i][j], dp[i - 1][pre]);
				}
				if (dp[i][j] != Integer.MAX_VALUE && j != gps_log[i])
					dp[i][j] += 1;
			}
		}

		int answer = dp[k - 1][gps_log[k - 1]];
		if (answer == Integer.MAX_VALUE)
			return -1;
		return answer;
	}
}