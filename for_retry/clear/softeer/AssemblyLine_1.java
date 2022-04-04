package softeer;

import java.util.*;
import java.io.*;


public class AssemblyLine_1
{
	static int k, n;
	public static void main(String args[]) throws Exception
	{
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

		StringTokenizer st = new StringTokenizer(in.readLine());
		k = Integer.parseInt(st.nextToken());
		n = Integer.parseInt(st.nextToken());

		int[][] workCost = new int[k][n];
		int[][][] workEdgeCost = new int[k][k][n]; // a to b in workspace
		int[][] dp = new int[k][n];
		for (int i = 0; i < n - 1; i++) { // Line
			st = new StringTokenizer(in.readLine());
			for (int j = 0; j < k; j++) { // WorkSpace
				workCost[j][i] = Integer.parseInt(st.nextToken());
			}
			for (int j = 0; j < k; j++) { // j to g
				for (int g = 0; g < k; g++) {
					if (j == g) continue;
					workEdgeCost[j][g][i] = Integer.parseInt(st.nextToken());
				}
			}
		}
		st = new StringTokenizer(in.readLine());
		for (int j = 0; j < k; j++) { // WorkSpace
			workCost[j][n - 1] = Integer.parseInt(st.nextToken());

			Arrays.fill(dp[j], Integer.MAX_VALUE);
		}

		for (int i = 0; i < n; i++) { // Line
			for (int j = 0; j < k; j++) { // WorkSpace
				if (i == 0)
					dp[j][i] = workCost[j][i];
				else {
					for (int g = 0; g < k; g++) {
						dp[j][i] = Math.min(dp[j][i], workCost[j][i] + dp[g][i - 1] + workEdgeCost[g][j][i - 1]);
					}
				}


			}
		}
		int answer = Integer.MAX_VALUE;

		for (int i = 0; i < k; i++) {
			answer = Integer.min(dp[i][n - 1], answer);
		}
		System.out.println(answer);
	}
}