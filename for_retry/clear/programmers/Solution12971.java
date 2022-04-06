package programmers;

public class Solution12971 {
	public int solution(int sticker[]) {
		int answer = 0;

		if (sticker.length == 1) {
			return sticker[0];
		} else if (sticker.length == 2) {
			return Math.max(sticker[0], sticker[1]);
		}

		int[] dp = new int[sticker.length];

		dp[0] = sticker[0];
		dp[1] = Math.max(sticker[0], sticker[1]);
		for (int i = 2; i < sticker.length - 1; i++) {
			dp[i] = Math.max(dp[i - 1], dp[i - 2] + sticker[i]);
		}

		int[] dpNotIncludeFirst = new int[sticker.length];
		dpNotIncludeFirst[0] = 0;
		dpNotIncludeFirst[1] = sticker[1];

		for (int i = 2; i < sticker.length; i++) {
			dpNotIncludeFirst[i] = Math.max(dpNotIncludeFirst[i - 1], dpNotIncludeFirst[i - 2] + sticker[i]);
		}
		return Math.max(dp[sticker.length - 2], dpNotIncludeFirst[sticker.length - 1]);
	}
}