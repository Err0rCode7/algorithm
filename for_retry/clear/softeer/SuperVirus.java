package softeer;

import java.util.*;
import java.io.*;


public class SuperVirus
{
	private static long[] dp;
	private static int MOD = 1000000007;
	private static long p;
	public static void main(String args[]) throws Exception
	{
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(in.readLine());
		int k = Integer.parseInt(st.nextToken());
		p = Integer.parseInt(st.nextToken());
		long n = Long.parseLong(st.nextToken());

		long result = 1;
		for (int i = 0; i < 10; i++) {
			result *= p;
			result %= MOD;
		}
		p = result;

		System.out.println((k * dfs(n)) % MOD);
	}

	private static long dfs(long n) {
		// System.out.println(n);
		if (n == 1)
			return p;
		else if (n == 0)
			return 1;
		long result = dfs(n / 2) % MOD;
		result *= result;
		result %= MOD;
		if (n % 2 == 1) {
			result *= p;
			result %= MOD;
		}
		return result;
	}
}