package programmers;

public class Solution12900 {
	public int solution(int n) {
		if (n == 1)
			return 1;
		else if (n == 2)
			return 2;
		else if(n == 3)
			return 3;
		int[] dp = new int[n + 1];

		dp[1] = 1;
		dp[2] = 2;
		dp[3] = 3;

		for (int i = 4; i < n + 1; i++) {
			dp[i] = (dp[i - 1] + dp[i - 2]) % 1_000_000_007;
		}

		return dp[n];
	}
}
