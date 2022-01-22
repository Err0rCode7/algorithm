package boj;

import java.io.*;
import java.util.*;
import static java.lang.Integer.*;

public class Main11657 {

	public static void main(String[] args) throws IOException {
		// Solution1.solution(); graph 탐색
		// Solution2.solution(); graph 탐색
		// Solution3.solution(); bellman ford
	}
}
class Solution1 {
	private final static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	private final static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	private static boolean stop = false;

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

class Solution2 {
	static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
	// static BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
	static int n, m;
	static int[][] distGraph;
	static boolean stop;
	static int[] result;
	static boolean[] visited;
	static List<Set<Integer>> pathGraph;

	public static void solution() throws IOException {
		StringTokenizer tokenizer = new StringTokenizer(in.readLine());
		n = parseInt(tokenizer.nextToken());
		m = parseInt(tokenizer.nextToken());

		distGraph = new int[n + 1][n + 1];
		for (int i = 0; i < n + 1; i++) {
			Arrays.fill(distGraph[i], MAX_VALUE);
		}

		pathGraph = new ArrayList<>(n + 1);

		for (int i = 0; i < n + 1; i++) {
			pathGraph.add(new HashSet<>());
		}

		for (int i = 0; i < m; i++) {
			tokenizer = new StringTokenizer(in.readLine());
			int a = parseInt(tokenizer.nextToken());
			int b = parseInt(tokenizer.nextToken());
			int c = parseInt(tokenizer.nextToken());
			distGraph[a][b] = min(distGraph[a][b], c);
			pathGraph.get(a).add(b);
		}

		result = new int[n + 1];
		Arrays.fill(result, MAX_VALUE);
		visited = new boolean[n + 1];

		dfs(0, 1);

		if (stop)
			System.out.println(-1);
		else {
			for (int i = 2; i < n + 1; i++) {
				if (result[i] == MAX_VALUE)
					System.out.println(-1);
				else
					System.out.println(result[i]);
			}
		}
	}

	public static void dfs(int accumCost, int cur) {
		if (stop) return;
		result[cur] = min(accumCost, result[cur]);
		visited[cur] = true;
		for (int next : pathGraph.get(cur)) {
			if (visited[next]) {
				if (accumCost + distGraph[cur][next] < result[next]) {
					stop = true;
				}
				continue;
			}
			if (accumCost + distGraph[cur][next] < result[next])
				dfs(accumCost + distGraph[cur][next], next);
		}
		visited[cur] = false;
	}
}

class Solution3 {
	static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
	static int n, m;

	public static void solution() throws IOException {
		StringTokenizer tokenizer = new StringTokenizer(in.readLine());
		n = parseInt(tokenizer.nextToken());
		m = parseInt(tokenizer.nextToken());

		List<int []> edges = new ArrayList<>();
		for (int i = 0; i < m; i++) {
			tokenizer = new StringTokenizer(in.readLine());
			int a = parseInt(tokenizer.nextToken());
			int b = parseInt(tokenizer.nextToken());
			int c = parseInt(tokenizer.nextToken());
			edges.add(new int[] {a, b, c});
		}

		long[] result = new long[n + 1];
		Arrays.fill(result, MAX_VALUE);
		result[1] = 0;
		boolean invalid = false;
		for (int i = 0; i < n; i++) {
			for (int[] edge : edges) {
				int a = edge[0];
				int b = edge[1];
				int dist = edge[2];

				if (result[a] == MAX_VALUE) continue;

				if (result[b] > result[a] + dist) {
					result[b] = result[a] + dist;
					if (i == n - 1) {
						invalid = true;
					}
				}
			}
		}

		if (invalid) {
			System.out.println(-1);
		} else {
			for (int i = 2; i < n + 1; i++) {
				if (result[i] == MAX_VALUE) {
					System.out.println(-1);
				} else{
					System.out.println(result[i]);
				}
			}
		}
	}
}