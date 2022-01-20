import java.io.*;
import java.util.*;
import static java.lang.Integer.*;

public class Main11657 {

	static class Solution {
		private final static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		private final static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		private static boolean stop = false;
		public static void main(String[] args) throws IOException {
			solution();
		}
		public static void solution() throws IOException {
			StringTokenizer tokenizer = new StringTokenizer(br.readLine());
			int n = parseInt(tokenizer.nextToken());
			int m = parseInt(tokenizer.nextToken());
			int[][] cost = new int[n + 1][n + 1];
			for (int i = 0; i < n + 1; i++) {
				Arrays.fill(cost[i], MAX_VALUE);
			}
			int[] result = new int[n + 1];
			Arrays.fill(result, MAX_VALUE);
			Map<Integer, List<Integer>> graph = new HashMap<>();
			for (int i = 0; i < m; i++) {
				tokenizer = new StringTokenizer(br.readLine());
				int a = parseInt(tokenizer.nextToken());
				int b = parseInt(tokenizer.nextToken());
				int c = parseInt(tokenizer.nextToken());
				cost[a][b] = min(cost[a][b], c);
				if (graph.containsKey(a)) {
					graph.get(a).add(b);
				} else {
					ArrayList<Integer> list = new ArrayList<>();
					list.add(b);
					graph.put(a, list);
				}
			}
			boolean[] visited = new boolean[n + 1];
			visited[1] = true;
			result[1] = 0;
			dfs(graph, cost, result, visited, 1, 0);
			if (stop)
				System.out.println(-1);
			else {
				for (int i = 2; i < n + 1; i++) {
					if (result[i] == MAX_VALUE)
						bw.write(-1 + "\n");
					else
						bw.write(result[i] + "\n");
				}
			}
			bw.flush();
			bw.close();
			br.close();
		}

		public static void dfs(Map<Integer, List<Integer>> graph, int[][] cost, int[] result, boolean[] visited, int cur, int curCost) {
			// System.out.println(cur);
			if (!graph.containsKey(cur)) return;
			for (int next: graph.get(cur)) {
				if (stop)
					return;
				if (visited[next]) {
					// System.out.println("visited" + next);
					// System.out.println(curCost + " " + cost[cur][next]);

					if (curCost + cost[cur][next] < result[next]) {
						stop = true;
					}
					continue;
				}
				if (result[next] > curCost + cost[cur][next]) {
					visited[next] = true;
					result[next] = min(result[next], curCost + cost[cur][next]);
					dfs(graph, cost, result, visited, next, curCost + cost[cur][next]);
					visited[next] = false;
				}
			}
		}
	}
}
