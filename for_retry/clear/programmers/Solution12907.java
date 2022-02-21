package programmers;

public class Solution12907 {
	public int solution(int n, int[] money) {
		int[] dp = new int[n + 1];
		dp[0] = 1;
		for (int i = 0; i < money.length; i++) {
			int coin = money[i];
			for (int j = coin; j < n + 1; j++) {
				dp[j] = dp[j - coin] + dp[j];
			}
		}
		return dp[n];
	}
}
