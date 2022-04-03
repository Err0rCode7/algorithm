package softeer;

import java.util.*;
import java.io.*;

public class H_CleanAlpha
{
	static int p, n;
	public static void main(String args[]) throws Exception
	{
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

		StringTokenizer st = new StringTokenizer(in.readLine());
		p = Integer.parseInt(st.nextToken());
		n = Integer.parseInt(st.nextToken());

		st = new StringTokenizer(in.readLine());
		long startVirusCount = 0;
		for (int i = 0; i < n; i++)  {
			long addedVirus = Integer.parseInt(st.nextToken());
			startVirusCount *= p;
			startVirusCount %= 1_000_000_007;
			startVirusCount += addedVirus;
			startVirusCount %= 1_000_000_007;
		}

		System.out.println(startVirusCount);

	}
}