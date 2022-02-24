package programmers;

import java.util.Arrays;

public class Solution43105 {
	public int solution(int[][] triangle) {
		int n = triangle.length;
		int[][] dp = new int[n][n];

		dp[0][0] = triangle[0][0];
		for (int i = 1; i < triangle.length; i++) {
			for (int j = 0; j < i + 1; j++) {
				int result = Integer.MIN_VALUE;
				if (j <= i - 1)
					result = dp[i - 1][j];
				if (j - 1 >= 0)
					result = Math.max(result, dp[i - 1][j - 1]);
				dp[i][j] = result + triangle[i][j];
			}
		}
		return Arrays.stream(dp[n - 1]).max().getAsInt();
	}
}