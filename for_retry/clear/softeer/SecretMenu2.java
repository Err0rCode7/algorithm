package softeer;

import java.util.*;
import java.io.*;


public class SecretMenu2
{
	public static void main(String args[]) throws Exception
	{
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

		StringTokenizer st = new StringTokenizer(in.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		int k = Integer.parseInt(st.nextToken());

		int[] arrA = new int[n];
		int[] arrB = new int[m];
		st = new StringTokenizer(in.readLine());
		for (int i = 0; i < n; ++i) {
			arrA[i] = Integer.parseInt(st.nextToken());
		}
		st = new StringTokenizer(in.readLine());
		for (int j = 0; j < m; ++j) {
			arrB[j] = Integer.parseInt(st.nextToken());
		}
		int length = 0;
		int[][] dp = new int[n][m];
		for (int j = 0; j < n; ++j) {
			for (int g = 0; g < m; ++g) {
				if (arrA[j] == arrB[g]) {
					if (j == 0 || g == 0) {
						dp[j][g] = 1;
					} else {
						dp[j][g] = dp[j - 1][g - 1] + 1;
					}
					length = Math.max(length, dp[j][g]);
				}
			}

		}

		System.out.println(length);
	}
}