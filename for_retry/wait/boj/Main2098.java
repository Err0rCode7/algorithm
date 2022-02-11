package boj;

import static java.lang.Integer.*;

import java.io.*;
import java.util.*;

public class Main2098 {
	public static void main(String[] args) throws IOException {
		Solution.solution();
	}

	static class Solution {
		static final BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		static final BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
		static int n;
		static int[][] w;
		static Queue<int[]> que;
		static int[] dx = new int[] {0, 1, 0, -1, 0, 1, 1, -1, -1};
		static int[] dy = new int[] {0, 0, 1, 0, -1, 1, -1, 1, -1};

		public static void solution() throws IOException {
			n = parseInt(in.readLine());

			w = new int[n + 1][n + 1];
			for (int i = 0; i < n; i++) {
				StringTokenizer tokenizer = new StringTokenizer(in.readLine());
				for (int j = 0; j < n; j++) {
					w[i + 1][j + 1] = parseInt(tokenizer.nextToken());
				}
			}
			int result = MAX_VALUE;
			for (int i = 1; i < n + 1; i++) {
				result = min(result, dijstra(i));
			}
			System.out.println(result);
		}

		public static int dijstra(int start) {
			int[][][] visited = new int[start + 1][n + 1][n + 2];
			for (int i = 1; i < start + 1; i++) {
				for (int j = 1; j < n + 1; j++) {
					Arrays.fill(visited[i][j], MAX_VALUE);
				}
			}
			Queue<Node> heap = new PriorityQueue<>(Comparator.comparingInt(o -> o.cost));
			heap.add(new Node(start, start, Integer.toString(start), 0));
			visited[start][start][0] = 0;
			while (heap.size() > 0) {

				Node node = heap.poll();
				if (visited[start][node.cur][node.path.length()] < node.cost)
					continue;
				if (node.cur == start && node.path.length() == n + 1){
					return node.cost;
				}

				for (int next = 1; next < n + 1; next++) {
					if (next != start && node.path.contains(Integer.toString(next)))
						continue;
					if (next == start && node.path.length() != n)
						continue;
					if (visited[start][next][node.path.length() + 1] <= node.cost + w[node.cur][next])
						continue;
					visited[start][next][node.path.length() + 1] =  node.cost + w[node.cur][next];
					heap.add(new Node(start, next, node.path + next, node.cost + w[node.cur][next]));
				}
				// start == end, path length 비교
			}
			return MAX_VALUE;
		}

		static class Node {
			int pre;
			int cur;
			String path;
			int cost;

			public Node(int pre, int cur, String path, int cost) {
				this.pre = pre;
				this.cur = cur;
				this.path = path;
				this.cost = cost;
			}
		}
	}
}
