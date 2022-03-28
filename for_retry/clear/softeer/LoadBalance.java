package softeer;

import java.util.*;
import java.io.*;


public class LoadBalance
{
	static List<Integer>[] graph;
	static long[] visited;
	public static void main(String args[]) throws Exception
	{
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));

		StringTokenizer st = new StringTokenizer(in.readLine());
		int n = Integer.parseInt(st.nextToken());
		long k = Long.parseLong(st.nextToken());

		graph = new List[n + 1];
		int[] inCount = new int[n + 1];
		for (int i = 1; i < n + 1; ++i) {
			graph[i] = new ArrayList<>();
			st = new StringTokenizer(in.readLine());
			int r = Integer.parseInt(st.nextToken());
			for (int j = 0; j < r; ++j) {
				int next = Integer.parseInt(st.nextToken());
				graph[i].add(next);
				inCount[next] += 1;
			}
		}

		visited = new long[n + 1];
		// dfs(k, 1);

		Queue<Integer> que = new LinkedList<>();
		que.add(1);
		visited[1] = k;
		while (!que.isEmpty()) {
			int cur = que.poll();

			if (graph[cur].size() == 0)
				continue;
			long rest = visited[cur] % graph[cur].size();
			long balancedCount = visited[cur] / graph[cur].size();
			for (int next : graph[cur]) {
				long balancedRequestCount = balancedCount;
				if (rest > 0) {
					rest--;
					balancedRequestCount++;
				}
				inCount[next] -= 1;
				visited[next] += balancedRequestCount;
				if (inCount[next] == 0 && graph[next].size() > 0)
					que.add(next);
			}
		}

		for (int i = 1; i < n + 1; ++i) {
			out.write(String.valueOf(visited[i]));
			if (i != n)
				out.write(" ");
		}
		out.flush();
		out.close();
		in.close();
	}

	private static void dfs(int requestCount, int node) {
		visited[node] += requestCount;
		// System.out.println(node);
		if (graph[node].size() == 0) {
			return;
		}
		int rest = requestCount % graph[node].size();
		int balancedCount = requestCount / graph[node].size();
		for (int next : graph[node]) {
			int balancedRequestCount = balancedCount + (rest > 0 ? 1 : 0);
			rest--;

			dfs(balancedRequestCount, next);
		}
	}
}