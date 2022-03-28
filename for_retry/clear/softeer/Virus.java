package softeer;

import java.util.*;
import java.io.*;


public class Virus
{
	static int[] dp;
	public static void main(String args[]) throws Exception
	{
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(in.readLine());
		int k = Integer.parseInt(st.nextToken());
		int p = Integer.parseInt(st.nextToken());
		int n = Integer.parseInt(st.nextToken());

		// long answer = k;
		// long num = 10000;
		// while (n > 0) {
		//     answer = (answer * p) % 1000000007;
		//     n--;
		// }
		// System.out.println(answer);

		System.out.println((k * spread(n, p)) % 1000000007);
	}

	private static long spread(int n, int p) {
		if (n == 1)
			return p;
		else if (n == 0)
			return 1;
		long result = 0;
		result = spread(n / 2, p);
		result = (result * result) % 1000000007;
		if (n % 2 == 1) {
			result = (result * p) % 1000000007;
		}

		// System.out.println(result);
		return result;
	}
}