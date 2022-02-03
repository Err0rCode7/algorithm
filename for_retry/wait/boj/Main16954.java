package boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class Main16954 {
	public static void main(String[] args) throws IOException {
		boolean solution = Solution.solution();
		if (solution)
			System.out.println(1);
		else
			System.out.println(0);
	}

	static class Solution {
		static final BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		static final int n = 8;
		static int[] dx_non_vertical = new int[] {1, -1, 1, -1};
		static int[] dy_non_vertical = new int[] {1, 1, -1, -1};
		static int[] dx = new int[] {1, 0, -1, 0};
		static int[] dy = new int[] {0, 1, 0, -1};
		static char[][] map;
		static Queue<int[]> walls;
		public static boolean solution() throws IOException {

			map = new char[n][n];
			walls = new LinkedList<>();
			for (int i = 0; i < n; i++) {
				String line = in.readLine();
				for (int j = 0; j < line.length(); j++) {
					map[i][j] = line.charAt(j);
					if (map[i][j] == '#') walls.add(new int[] {j, i});
				}
			}

			Queue<int[]> que = new LinkedList<>();
			que.add(new int[] {0, n - 1}); // x, y
			while (!que.isEmpty()) {
				if (walls.size() <= 0)
					return true;
				// move character
				int size = que.size();
				boolean[][] visited = new boolean[n][n];

				for (int i = 0; i < size; i++) {
					int[] poll = que.poll();
					int x = poll[0];
					int y = poll[1];
					if (map[y][x] == '#') continue;

					que.add(new int[] {x, y});
					visited[y][x] = true;
					for (int j = 0; j < 8; j++) {
						int nx, ny;
						if (j >= 4) {

							nx = x + dx_non_vertical[j % 4];
							ny = y + dy_non_vertical[j % 4];
						} else {
							nx = x + dx[j];
							ny = y + dy[j];
						}

						if (0 > nx || nx >= n || 0 > ny || ny >= n || map[ny][nx] == '#' || visited[ny][nx]) continue;

						if (ny == 0) return true;

						if (map[ny - 1][nx] == '#') continue;
						visited[ny][nx] = true;
						que.add(new int[] {nx, ny});
					}

				}

				// move walls
				int wallSize = walls.size();
				((List<int[]>)walls).sort(Comparator.comparingInt(o -> -o[1]));

				for (int i = 0; i < wallSize; i++) {
					int[] pos = walls.poll();
					map[pos[1]][pos[0]] = '.';
					if (pos[1] + 1 < n) {
						pos[1] += 1;
						map[pos[1]][pos[0]] = '#';
						walls.add(pos);
					}
				}
			}
			return false;
		}
	}
}