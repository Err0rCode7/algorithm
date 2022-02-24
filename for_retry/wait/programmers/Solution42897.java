package programmers;

import java.util.Arrays;

public class Solution42897 {
	public int solution(int[] money) {
		int[] dp = new int[money.length];
		int[] dpForCycle = new int[money.length - 1];
		Arrays.fill(dp, Integer.MAX_VALUE);
		Arrays.fill(dpForCycle, Integer.MAX_VALUE);

		dp[0] = money[0];
		dp[1] = Math.max(money[0], money[1]);
		for (int i = 2; i < money.length - 1; i++) {
			dp[i] = Math.max(dp[i - 1], dp[i - 2] + money[i]);
		}

		dpForCycle[0] = money[1];
		dpForCycle[1] = Math.max(money[1], money[2]);
		for (int i = 2; i < money.length - 1; i++) {
			dpForCycle[i] = Math.max(dpForCycle[i - 1], dpForCycle[i - 2] + money[i + 1]);
		}

		return Math.max(dp[money.length - 2], dpForCycle[money.length - 2]);
	}
}