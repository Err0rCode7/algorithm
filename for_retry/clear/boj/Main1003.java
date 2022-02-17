package boj;

import static java.lang.Integer.*;

import java.io.*;
import java.util.*;

public class Main1003 {
	public static void main(String[] args) throws IOException {
		Solution.solution();
	}

	static class Solution {
		static final BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		static final BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
		static int n, m, k, t;
		static int[][] map;
		static String target;
		static Queue<int[]> que;
		static int[] dx = new int[] {1, 0, -1, 0};
		static int[] dy = new int[] {0, 1, 0, -1};
		static int[][] dp;
		static int answer;

		public static void solution() throws IOException {
			t = parseInt(in.readLine());
			dp = new int[41][2];
			for (int j = 0; j < 41; j++) {
				Arrays.fill(dp[j], -1);
			}
			for (int i = 0; i < t; i++) {

				int[] result = fibo(parseInt(in.readLine()));
				System.out.println(result[0] + " " + result[1]);
			}
		}

		public static int[] fibo(int n) {
			if (n == 0){
				dp[n][0] = 1;
				dp[n][1] = 0;
				return dp[n];
			}
			else if (n == 1) {
				dp[n][0] = 0;
				dp[n][1] = 1;
				return dp[n];
			}
			if (dp[n][0] != -1 && dp[n][1] != -1) {
				return dp[n];
			}
			int[] a = fibo(n - 1);
			int[] b = fibo(n - 2);
			dp[n][0] = a[0] + b[0];
			dp[n][1] = a[1] + b[1];
			return dp[n];
		}
	}
}