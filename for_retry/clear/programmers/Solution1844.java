package programmers;

import java.util.LinkedList;
import java.util.Queue;

public class Solution1844 {
	public int solution(int[][] maps) {

		int n = maps.length;
		int m = maps[0].length;
		int[] dx = {1, 0, -1, 0};
		int[] dy = {0, 1, 0, -1};

		Queue<Node> que = new LinkedList<>();
		boolean[][] visited = new boolean[n][m];
		Node start = new Node(0, 0, 1);
		que.add(start);
		visited[0][0] = true;

		while (!que.isEmpty()) {
			Node cur = que.poll();

			if (cur.x == m - 1 & cur.y == n - 1)
				return cur.cost;

			for (int i = 0; i < 4; i++) {
				int nx = cur.x + dx[i];
				int ny = cur.y + dy[i];

				if (nx < 0 || nx >= m || ny >= n || ny < 0 || maps[ny][nx] == 0 || visited[ny][nx]) continue;

				visited[ny][nx] = true;
				que.add(new Node(nx, ny, cur.cost + 1));

			}
		}
		return -1;
	}

	private class Node {
		int x;
		int y;
		int cost;

		public Node(int x, int y, int cost) {
			this.x = x;
			this.y = y;
			this.cost = cost;
		}
	}
}