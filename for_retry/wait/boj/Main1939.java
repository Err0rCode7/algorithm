package boj;

import static java.lang.Integer.*;

import java.io.*;
import java.util.*;

public class Main1939 {
	public static void main(String[] args) throws IOException {
		Solution.solution();
	}

	static class Solution {
		static final BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		static final BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
		static int n, m, k;
		static int[][] cost;
		static String target;
		static Queue<int[]> que;
		static int[] dx = new int[] {1, 0, -1, 0};
		static int[] dy = new int[] {0, 1, 0, -1};
		static int[] dp;
		static int answer;
		static Map<Integer, Map<Integer, Integer>> graph;
		public static void solution() throws IOException {

			StringTokenizer tokenizer = new StringTokenizer(in.readLine());
			n = parseInt(tokenizer.nextToken());
			m = parseInt(tokenizer.nextToken());

			graph = new HashMap<>();
			for (int i = 0; i < m; i++) {
				tokenizer = new StringTokenizer(in.readLine());
				int a = parseInt(tokenizer.nextToken());
				int b = parseInt(tokenizer.nextToken());
				int c = parseInt(tokenizer.nextToken());
				if (graph.containsKey(a)) {
					Map<Integer, Integer> map = graph.get(a);
					if (map.containsKey(b)) {
						c = max(map.get(b), c);
					}
					graph.get(a).put(b, c);
				}
				else {
					Map<Integer, Integer> map = new HashMap<>();
					map.put(b, c);
					graph.put(a, map);
				}
				if (graph.containsKey(b)) {
					Map<Integer, Integer> map = graph.get(b);
					if (map.containsKey(a)) {
						c = max(map.get(a), c);
					}
					graph.get(b).put(a, c);
				}
				else {
					Map<Integer, Integer> map = new HashMap<>();
					map.put(a, c);
					graph.put(b, map);
				}
			}

			tokenizer = new StringTokenizer(in.readLine());
			int from = parseInt(tokenizer.nextToken());
			int to = parseInt(tokenizer.nextToken());

			int left = 0;
			int right = 1_000_000_000;
			int answer = 0;
			boolean[] visited = new boolean[n + 1];
			while (left <= right) {
				int mid = (left + right) / 2;

				Arrays.fill(visited, false);
				if (dfs(from, mid, to, visited)) {
					answer = max(answer, mid);
					left = mid + 1;
				} else {
					right = mid - 1;
				}
			}
			System.out.println(answer);
		}

		public static boolean dfs(int node, int threshhold, int target, boolean[] visited) {
			if (target == node)
				return true;
			visited[node] = true;
			if (graph.containsKey(node)) {
				Map<Integer, Integer> map = graph.get(node);
				for (Integer next : map.keySet()) {
					int cost = map.get(next);
					if (visited[next])
						continue;
					if (cost < threshhold)
						continue;
					if (dfs(next, threshhold, target, visited))
						return true;
				}
			}
			return false;
		}
	}
}
