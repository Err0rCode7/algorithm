package boj;

import static java.lang.Integer.*;

import java.io.*;
import java.util.*;

public class Main17404 {
	public static void main(String[] args) throws IOException {
		Solution.solution();
	}

	static class Solution {
		static final BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		static final BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
		static int n, m, k;
		static String[] map;
		static String target;
		static Queue<int[]> que;
		static int[] dx = new int[] {1, 0, -1, 0};
		static int[] dy = new int[] {0, 1, 0, -1};
		static int[][] graph;
		public static void solution() throws IOException {
			n = parseInt(in.readLine());
			graph = new int[n + 1][3];
			for (int i = 1; i < n + 1; i++) {
				StringTokenizer tokenizer = new StringTokenizer(in.readLine());
				for (int j = 0; j < 3; j++) {
					graph[i][j] = parseInt(tokenizer.nextToken());
				}
			}

			Queue<Solution.Node> que = new PriorityQueue<>(Comparator.comparingInt(o -> o.cost));
			que.add(new Solution.Node(graph[1][0], 1, 0, 0)); // cost, curNode, curColor
			que.add(new Solution.Node(graph[1][1], 1, 1, 1));
			que.add(new Solution.Node(graph[1][2], 1, 2, 2));

			int[][][] visited = new int[n + 1][3][3];
			for (int i = 1; i < n + 1; i++) {
				for (int j = 0; j < 3; j++) {
					Arrays.fill(visited[i][j], MAX_VALUE);
				}
			}

			int answer = MAX_VALUE;
			while (!que.isEmpty()) {
				Solution.Node cur = que.poll();
				int root = cur.rootColor;
				if (visited[cur.nodeNum][cur.color][root] < cur.cost)
					continue;
				if (cur.nodeNum == n){
					answer = min(cur.cost, answer);
					continue;
				}

				for (int nextColor = 0; nextColor < 3; nextColor++) {
					if (nextColor == cur.color) continue;
					// System.out.println(cur.path.charAt(0) - '0' + " " + nextColor + " " + visited[cur.nodeNum + 1][nextColor]);
					if (cur.nodeNum == n - 1 && nextColor == root) continue;

					if (visited[cur.nodeNum + 1][nextColor][root] <= cur.cost + graph[cur.nodeNum + 1][nextColor])
						continue;
					visited[cur.nodeNum + 1][nextColor][root] = cur.cost + graph[cur.nodeNum + 1][nextColor];
					que.add(
						new Solution.Node(cur.cost + graph[cur.nodeNum + 1][nextColor],
							cur.nodeNum + 1,
							nextColor,
							root));
				}
			}
			System.out.println(answer);
		}

		static class Node {
			int cost;
			int nodeNum;
			int color;
			int rootColor;

			public Node(int cost, int curNode, int curColor, int rootColor) {
				this.cost = cost;
				this.nodeNum = curNode;
				this.color = curColor;
				this.rootColor = rootColor;
			}
		}
	}
}
