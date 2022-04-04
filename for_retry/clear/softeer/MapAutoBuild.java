package softeer;

import java.util.*;
import java.io.*;


public class MapAutoBuild
{
	static int[] dp;
	public static void main(String args[]) throws Exception
	{
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

		int n = Integer.parseInt(in.readLine());

		dp = new int[16];
		dp[0] = 2;
		dp[1] = 3;
		dp[2] = 5;

		solve(n);

		System.out.println(dp[n] * dp[n]);
	}

	private static int solve(int n) {
		if (n <= 2) {
			return dp[n];
		}
		int res = solve(n - 1);
		dp[n] = res + (res - 1);
		return dp[n];
	}
}