package boj;

import static java.lang.Integer.*;

import java.io.*;
import java.util.*;

class Main10217 {
	public static void main(String[] args) throws IOException {
		Solution.solution();
	}

	static class Solution {
		static int n, m, answer = MAX_VALUE;
		static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		// static BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
		static List<List<Path>> graph;

		public static void solution() throws IOException {
			int t = parseInt(in.readLine());
			graph = new ArrayList<>(101);
			for (int i = 0; i < 101; i++) {
				graph.add(new ArrayList<>());
			}
			for (int i = 0; i < t; i++) {
				solve();
			}
			// out.flush();
			// out.close();
			in.close();
		}

		public static void solve() throws IOException {
			StringTokenizer tokenizer = new StringTokenizer(in.readLine());
			n = parseInt(tokenizer.nextToken());
			m = parseInt(tokenizer.nextToken());
			int k = parseInt(tokenizer.nextToken());

			for (int i = 0; i < k; i++) {
				tokenizer = new StringTokenizer(in.readLine());
				int u = parseInt(tokenizer.nextToken());
				int v = parseInt(tokenizer.nextToken());
				int c = parseInt(tokenizer.nextToken());
				int d = parseInt(tokenizer.nextToken());
				graph.get(u).add(new Path(v, c, d));
			}
			// boolean[] visited = new boolean[n + 1];
			// dfs(0, 0, 1, visited);
			Queue<int[]> heap = new PriorityQueue<>(new Comparator<int[]>() {
				@Override
				public int compare(int[] o1, int[] o2) {
					return o1[0] - o2[0];
				}
			});
			heap.add(new int[] {0, 0, 1});
			int[][] graphDist = new int[n + 1][m + 1];
			for (int i = 0; i < n + 1; i++) {
				Arrays.fill(graphDist[i], MAX_VALUE);
			}

			Arrays.fill(graphDist[1], 0);
			int dist = 0, cost = 0, node = 1;
			while (heap.size() > 0) {
				int[] cur = heap.poll();
				dist = cur[0];
				cost = cur[1];
				node = cur[2];
				if (node == n) {
					System.out.println(dist);
					break;
				}

				List<Path> candidate = graph.get(node);
				for (Path path : candidate) {
					int nextCost = path.cost + cost;
					int nextDist = path.dist + dist;
					int next = path.target;
					if (nextCost > m) continue;
					if (graphDist[next][nextCost] > nextDist) {
						graphDist[next][nextCost] = nextDist;
						heap.add(new int[]{nextDist, nextCost, next});
					}
				}
			}
			for (int j = 1; j < n + 1; j++) {
				graph.get(j).clear();
			}
			if (node != n)
				System.out.println("Poor KCM");
		}


		public static void dfs(int dist, int cost, int cur, boolean[] visited) {
			// 시간 초과
			if (cur == n) {
				answer = min(answer, cost);
				return;
			}

			if (cost >= m || dist >= answer)
				return;

			visited[cur] = true;
			List<Path> paths = graph.get(cur);
			for (Path path : paths) {
				if (cost + path.cost <= m && !visited[path.target]) {
					dfs(dist + path.dist, cost + path.cost, path.target, visited);
				}
			}
			visited[cur] = false;
		}

		static class Path {
			int dist;
			int cost;
			int target;

			public Path(int target, int cost, int dist) {
				this.dist = dist;
				this.cost = cost;
				this.target = target;
			}
		}
	}
}

