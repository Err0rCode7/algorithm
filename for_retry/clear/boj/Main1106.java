package boj;

import static java.lang.Integer.*;

import java.io.*;
import java.util.*;

public class Main1106 {
	public static void main(String[] args) throws IOException {
		Solution.solution();
	}

	static class Solution {
		static final BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		static final BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
		static int n, m, k, c;
		static int[][] map;
		static String target;
		static Queue<int[]> que;
		static int[] dx = new int[] {1, 0, -1, 0};
		static int[] dy = new int[] {0, 1, 0, -1};
		static int[] dp;
		static int[][] city;
		static int answer;
		public static void solution() throws IOException {

			StringTokenizer tokenizer = new StringTokenizer(in.readLine());
			c = parseInt(tokenizer.nextToken());
			n = parseInt(tokenizer.nextToken());
			city = new int[n][2]; // cost, userCount
			for (int i = 0; i < n; i++) {
				tokenizer = new StringTokenizer(in.readLine());
				city[i][0] = parseInt(tokenizer.nextToken());
				city[i][1] = parseInt(tokenizer.nextToken());
			}

			dp = new int[1101]; // 인원 당 최소 비용이 얼마인지

			Arrays.fill(dp, MAX_VALUE);
			int answer = MAX_VALUE;
			dp[0] = 0;
			for (int i = 0; i < n; i++) {
				int cost = city[i][0];
				int count = city[i][1];
				for (int j = count; j < 1101; j++) {
					if (dp[j - count] != MAX_VALUE)
						dp[j] = min(dp[j], dp[j - count] + cost);
					if (j >= c)
						answer = min(answer, dp[j]);
				}
			}

			System.out.println(answer);
		}
	}
}