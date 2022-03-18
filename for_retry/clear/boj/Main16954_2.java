package boj;

import static java.lang.Integer.*;

import java.io.*;
import java.util.*;

public class Main16954_2 {
	public static void main(String[] args) throws IOException {
		Solution.solution();
	}

	static class Solution {
		static final BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		static final BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
		static int n;
		static String[] map;
		static Queue<int[]> que;
		static int[] dx = new int[] {0, 1, 0, -1, 0, 1, 1, -1, -1};
		static int[] dy = new int[] {0, 0, 1, 0, -1, 1, -1, 1, -1};

		public static void solution() throws IOException {
			n = 8;

			String[] map = new String[n];
			for (int i = 0; i < n; i++) {
				map[i] = in.readLine();
			}

			Queue<int[]> que = new LinkedList<>();
			que.add(new int[] {0, n - 1, 0});
			boolean[][][] visited = new boolean[n][n][9];
			// for (int i = 0; i < n; i++) {
			// 	for (int j = 0; j < n; j++) {
			// 		Arrays.fill(visited[i][j], MAX_VALUE);
			// 	}
			// }

			// visited[n - 1][0] = 0;
			while (!que.isEmpty()) {
				int[] pos = que.poll();
				int time = pos[2];

				for (int i = 0; i < 9; i++) {
					int nx = pos[0] + dx[i];
					int ny = pos[1] + dy[i];

					if (nx < 0 || nx >= n || ny < 0 || ny >= n)
						continue;
					if (ny == 0) {
						System.out.println(1);
						return;
					}
					if (ny - time >= 0 && map[ny - time].charAt(nx) == '#')
						continue;
					if (ny - 1 - time >= 0 && map[ny - 1 - time].charAt(nx) == '#')
						continue;
					if (visited[ny][nx][i])
						continue;
					visited[ny][nx][i] = true;
					que.add(new int[] {nx, ny, time + 1});
				}
			}

			System.out.println(0);
		}
	}
}
