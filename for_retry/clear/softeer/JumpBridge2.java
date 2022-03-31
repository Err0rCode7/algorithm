package softeer;

import java.util.*;
import java.io.*;


public class JumpBridge2
{
	public static void main(String args[]) throws Exception
	{
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

		int n = Integer.parseInt(in.readLine());

		StringTokenizer st = new StringTokenizer(in.readLine());

		int[] stones = new int[n];
		for (int i = 0; i < n ; i++) {
			stones[i] = Integer.parseInt(st.nextToken());
		}

		List<Integer> minValue = new ArrayList<>();
		List<Integer> minValueReverse = new ArrayList<>();
		int[] stoneCount = new int[n];
		int[] stoneCountReverse = new int[n];
		for (int i = 0; i < n; i++) {
			int j = n - i - 1;

			int idx = lower_bound(minValue, stones[i]);
			if (idx >= minValue.size()) {
				minValue.add(stones[i]);
			} else {
				minValue.set(idx, stones[i]);
			}
			stoneCount[i] = idx + 1;

			int idxReverse = lower_bound(minValueReverse, stones[j]);
			if (idxReverse >= minValueReverse.size()) {
				minValueReverse.add(stones[j]);
			} else {
				minValueReverse.set(idxReverse, stones[j]);
			}
			stoneCountReverse[j] = idxReverse + 1;
		}
		// System.out.println(Arrays.toString(stoneCount));
		// System.out.println(Arrays.toString(stoneCountReverse));
		int answer = 0;
		for (int i = 0; i < n; i++) {
			answer = Math.max(answer, stoneCount[i] + stoneCountReverse[i] - 1);
		}
		System.out.println(answer);
	}

	private static int lower_bound(List<Integer> minValue, int target) {
		int s = 0;
		int e = minValue.size();

		while (s < e) {
			int m = (s + e) / 2;

			if (minValue.get(m) < target) {
				s = m + 1;
			} else {
				e = m;
			}
		}
		return e;
	}
}