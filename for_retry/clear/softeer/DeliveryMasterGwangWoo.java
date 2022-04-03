package softeer;

import java.util.*;
import java.io.*;

public class DeliveryMasterGwangWoo
{
	static int n, m, k;
	static int[] orderedWeight, weight;
	static int answer;
	public static void main(String args[]) throws Exception
	{
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

		StringTokenizer st = new StringTokenizer(in.readLine());

		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		k = Integer.parseInt(st.nextToken());

		st = new StringTokenizer(in.readLine());
		weight = new int[n];
		for (int i = 0; i < n; ++i) {
			weight[i] = Integer.parseInt(st.nextToken());
		}
		answer = Integer.MAX_VALUE;
		boolean[] selected = new boolean[n];
		orderedWeight = new int[n];

		execComb(0, selected);
		System.out.println(answer);
	}

	private static void execComb(int start, boolean[] selected) {
		if (start == n) {
			// System.out.println(Arrays.toString(orderedWeight));
			int result = execSystem();
			if (answer > result)
				answer = result;
			return;
		}

		for (int i = 0; i < n; i++) {
			if (selected[i]) continue;

			orderedWeight[start] = weight[i];
			selected[i] = true;
			execComb(start + 1, selected);
			selected[i] = false;
		}
	}

	private static int execSystem() {
		int idx = 0;
		int accumulation = 0;
		for (int i = 0; i < k; i++) {
			int bucket = 0;

			while (bucket + orderedWeight[idx] <= m) {
				bucket += orderedWeight[idx];
				idx = (idx + 1) >= n ? 0 : idx + 1;
			}

			accumulation += bucket;
		}
		return accumulation;
	}
}