package boj;

import static java.lang.Integer.*;

import java.io.*;
import java.util.*;

public class Main2839 {
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
			int[] dp = new int[5001];
			Arrays.fill(dp, 50000);
			dp[0] = 0;
			dp[3] = 1;
			dp[5] = 1;
			for (int i = 5; i < n + 1; i++) {
				dp[i] = min(dp[i - 3], dp[i - 5]) + 1;
			}
			if (dp[n] >= 50000)
				System.out.println(-1);
			else
				System.out.println(dp[n]);
		}
	}
}