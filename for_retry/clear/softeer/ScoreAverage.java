package softeer;

import java.util.*;
import java.io.*;


public class ScoreAverage
{
	static int n, k;
	static int[] accumlation;
	public static void main(String args[]) throws Exception
	{
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(in.readLine());
		n = Integer.parseInt(st.nextToken());
		k = Integer.parseInt(st.nextToken());
		st = new StringTokenizer(in.readLine());
		accumlation = new int[n + 1];
		for (int i = 1; i < n + 1; i++) {
			int score = Integer.parseInt(st.nextToken());
			accumlation[i] = accumlation[i - 1] + score;
		}

		for (int i = 0; i < k; i++) {
			st = new StringTokenizer(in.readLine());
			int start = Integer.parseInt(st.nextToken());
			int end = Integer.parseInt(st.nextToken());

			double result = accumlation[end] - accumlation[start - 1];
			result /= end - start + 1;
			result *= 100;
			result = Math.round(result);
			String roundResult = String.valueOf((int)result);
			out.write(roundResult.substring(0, roundResult.length() - 2));
			out.write(".");
			out.write(roundResult.substring(roundResult.length() - 2, roundResult.length()));
			out.write("\n");
		}
		out.flush();
	}
}