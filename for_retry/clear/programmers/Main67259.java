package programmers;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class Main67259 {
	static class Solution2 {
		public int solution(int[][] board) {
			int n = board.length;
			int[][][] visited = new int[n][n][4];

			for (int i=0; i<n; ++i) {
				for (int j = 0; j < n; j++) {
					for (int k = 0; k < 4; k++) {
						visited[i][j][k] = Integer.MAX_VALUE;
					}
				}
			}

			Queue<Node> que = new LinkedList<>();
			Arrays.fill(visited[0][0], 0);
			que.add(new Node(0, 0, -1, 0));
			int[] dx = {0, 1, 0, -1};
			int[] dy = {1, 0, -1, 0};

			while (!que.isEmpty()) {
				Node cur = que.poll();
				// System.out.println(cur.x + " " + cur.y + " " + cur.dir + " " + cur.cost);
				for (int i = 0; i < 4; ++i) {
					int nx = cur.x + dx[i];
					int ny = cur.y + dy[i];

					if (0 > nx || nx >= n || 0 > ny || ny >= n || board[ny][nx] == 1) continue;
					int add = 100;
					if (cur.dir != -1 && !(Math.abs(cur.dir - i) == 2 || Math.abs(cur.dir - i) == 0)) {
						add += 500;
					}

					if (cur.cost + add <= visited[ny][nx][i]){
						visited[ny][nx][i] = cur.cost + add;
						que.add((new Node(nx, ny, i, cur.cost + add)));
					}
				}
			}
			return Arrays.stream(visited[n - 1][n - 1])
				.min().getAsInt();
		}

		class Node {
			int x;
			int y;
			int dir;
			int cost;

			public Node(int x, int y, int dir, int cost) {
				this.x = x;
				this.y = y;
				this.dir = dir;
				this.cost = cost;
			}
		}

		public static void main(String[] args) {
			Solution2 solution = new Solution2();
			System.out.println(solution.solution(new int[][] {
				{0, 0, 1, 0},
				{0, 0, 0, 0},
				{0, 1, 0, 1},
				{1, 0, 0, 0}
			}));
		}
	}
}
