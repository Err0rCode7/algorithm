package softeer;

import java.util.*;
import java.io.*;


public class AssemblyLine_2
{
	public static void main(String args[]) throws Exception
	{
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

		StringTokenizer st = new StringTokenizer(in.readLine());
		int k = Integer.parseInt(st.nextToken());
		int n = Integer.parseInt(st.nextToken());

		int[][] workCost = new int[n][k];
		int[] edgeCost = new int[n];
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(in.readLine());
			for (int j = 0; j < k; j++) {
				workCost[i][j] = Integer.parseInt(st.nextToken());
			}
			if (i != n - 1)
				edgeCost[i] = Integer.parseInt(st.nextToken());
		}
		int[][] dp = new int[n][k];
		int min = Integer.MAX_VALUE;
		for (int i = 0; i < n; i++) {
			int preMin = min;
			min = Integer.MAX_VALUE;
			for (int j = 0; j < k; j++) {
				if (i == 0) {
					dp[i][j] = workCost[i][j];
				} else {
					dp[i][j] = workCost[i][j] + preMin + edgeCost[i - 1];
					if (dp[i][j] > workCost[i][j] + dp[i - 1][j])
						dp[i][j] = workCost[i][j] + dp[i - 1][j];
				}
				min = Math.min(min, dp[i][j]);
			}
		}
		System.out.println(min);
	}
}