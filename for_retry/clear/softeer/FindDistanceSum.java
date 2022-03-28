package softeer;

import java.util.*;
import java.io.*;


public class FindDistanceSum
{
	private static int[] subtreeSize;
	private static long[] sum;
	private static List<int[]>[] graph;
	private static int n;
	public static void main(String args[]) throws Exception
	{
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));

		n = Integer.parseInt(in.readLine());
		graph = new List[n + 1];

		for (int i = 1; i < n + 1; ++i) {
			graph[i] = new ArrayList<>();
		}

		for (int i = 0; i < n - 1; ++i) {
			StringTokenizer st = new StringTokenizer(in.readLine());

			// a to b : cost
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int cost = Integer.parseInt(st.nextToken());

			graph[a].add(new int[]{b, cost});
			graph[b].add(new int[]{a, cost});
		}

		subtreeSize = new int[n + 1];
		sum = new long[n + 1];
		dfs(1, 1);
		setupSum(1, 1);
		// System.out.println(Arrays.toString(subtreeSize));
		// System.out.println(Arrays.toString(sum));


		for (int i = 1; i < n + 1; i++) {
			out.write(String.valueOf(sum[i]) + "\n");
		}
		out.flush();
	}

	private static void dfs(int cur, int parent) {
		int size = 1; // with cur
		for (int[] nextNode : graph[cur]) {
			int child = nextNode[0];
			long edgeCost = (long)nextNode[1];
			if (child == parent) continue;
			dfs(child, cur);
			size += subtreeSize[child];
			sum[cur] += sum[child] + edgeCost * subtreeSize[child];
		}
		subtreeSize[cur] = size;
	}

	private static void setupSum(int cur, int parent) {
		for (int[] nextNode : graph[cur]) {
			int child = nextNode[0];
			long edgeCost = (long)nextNode[1];

			if (child == parent) continue;
			sum[child] = sum[cur] + (n - subtreeSize[child]) * edgeCost - (subtreeSize[child] * edgeCost);
			setupSum(child, cur);
		}
	}
}