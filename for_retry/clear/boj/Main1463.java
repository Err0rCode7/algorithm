package boj;
import static java.lang.Integer.*;

import java.io.*;
import java.util.*;

public class Main1463 {
	public static void main(String[] args) throws IOException {
		Solution.solution();
	}

	static class Solution {
		static final BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		static final BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
		static int n, m, k;
		static int[][] map;
		static String target;
		static Queue<int[]> que;
		static int[] dx = new int[] {1, 0, -1, 0};
		static int[] dy = new int[] {0, 1, 0, -1};
		static int[] dp;
		static int answer;

		public static void solution() throws IOException {
			n = parseInt(in.readLine());
			dp = new int[1000001];
			Arrays.fill(dp, 1000002);
			dp[1] = 0;
			for (int i = 2; i < n + 1; i++) {
				dp[i] = min(dp[i - 1] + 1, dp[i]);
				if (i % 3 == 0)
					dp[i] = min(dp[i / 3] + 1, dp[i]);
				if (i % 2 == 0)
					dp[i] = min(dp[i / 2] + 1, dp[i]);
			}
			System.out.println(dp[n]);
		}
	}
}