package softeer;

import java.util.*;
import java.io.*;

public class AssemblyLine
{
	static int n;
	static int[] A, B, aToB, btoA;
	public static void main(String args[]) throws Exception
	{
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

		n = Integer.parseInt(in.readLine());
		A = new int[n];
		B = new int[n];
		aToB = new int[n];
		btoA = new int[n];
		for (int i = 0; i < n; i ++) {
			StringTokenizer st = new StringTokenizer(in.readLine());
			A[i] = Integer.parseInt(st.nextToken());
			B[i] = Integer.parseInt(st.nextToken());
			if (i + 1 != n) {
				aToB[i] = Integer.parseInt(st.nextToken());
				btoA[i] = Integer.parseInt(st.nextToken());
			}
		}
		int[] costA = new int[n];
		int[] costB = new int[n];
		Queue<int[]> heap = new PriorityQueue<>((o1, o2) -> o1[1] - o2[1]);
		heap.add(new int[]{0, A[0], 1}); // idx, cost, isA;
		heap.add(new int[]{0, B[0], 0});
		Arrays.fill(costA, Integer.MAX_VALUE);
		Arrays.fill(costB, Integer.MAX_VALUE);
		costA[0] = A[0];
		costB[0] = B[0];
		while (!heap.isEmpty()) {
			int[] cur = heap.poll();
			int idx = cur[0];
			int cost = cur[1];
			boolean isA = cur[2] == 1;
			// System.out.println(idx);
			if (idx == n - 1)
				continue;
			if (isA) {
				if (costA[idx] < cost)
					continue;

				if (costA[idx + 1] > cost + A[idx + 1]) {
					costA[idx + 1] = cost + A[idx + 1];
					heap.add(new int[]{idx + 1, costA[idx + 1], 1});
				}
				if (costB[idx + 1] > cost + B[idx + 1] + aToB[idx]) {
					costB[idx + 1] = cost + B[idx + 1] + aToB[idx];
					heap.add(new int[]{idx + 1, costB[idx + 1], 0});
				}
			} else {
				if (costB[idx] < cost)
					continue;

				if (costB[idx + 1] > cost + B[idx + 1]) {
					costB[idx + 1] = cost + B[idx + 1];
					heap.add(new int[]{idx + 1, costB[idx + 1], 0});
				}
				if (costA[idx + 1] > cost + A[idx + 1] + btoA[idx]) {
					costA[idx + 1] = cost + A[idx + 1] + btoA[idx];
					heap.add(new int[]{idx + 1, costA[idx + 1], 1});
				}
			}
		}

		System.out.println(Math.min(costA[n - 1], costB[n - 1]));
	}
}