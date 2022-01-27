package boj;

import static java.lang.Integer.*;

import java.io.*;
import java.util.*;

class Main2151 {
	public static void main(String[] args) throws IOException {
		Solution.solution();
	}

	static class Solution {
		static int n, m, answer = MAX_VALUE;
		static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		// static BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
		static char[][] map;
		static List<int[]> door = new ArrayList<>(2);
		// |
		static int[] dx2 = new int[] {-1, -1, 1, 1};
		static int[] dy2 = new int[] {-1, 1, 1, -1};
		// -
		static int[] dx1 = new int[] {1, 1, -1, -1};
		static int[] dy1 = new int[] {1, -1, -1, 1};

		// /
		static int[] dx3 = new int[] {0, -1, 0, 1};
		static int[] dy3 = new int[] {-1, 0, 1, 0};
		// \
		static int[] dx4 = new int[] {0, 1, 0, -1};
		static int[] dy4 = new int[] {1, 0, -1, 0};

		static int[] crossX = new int[] {1, 1, -1, -1};
		static int[] crossY = new int[] {-1, 1, 1, -1};

		static int[] notCrossX = new int[] {1, 0, -1, 0};
		static int[] notCrossY = new int[] {0, 1, 0, -1};

		static char[] mirrors = new char[] {'-', '|', '/', '\\'};

		public static void solution() throws IOException {
			n = parseInt(in.readLine());
			map = new char[n][n];

			for (int i = 0; i < n; i++) {
				String line = in.readLine();
				for (int j = 0; j < n; j++) {
					map[i][j] = line.charAt(j);
					if (map[i][j] == '#') {
						door.add(new int[] {j, i});
					}
				}
			}
			solve();
			// out.flush();
			// out.close();
			in.close();
		}

		public static void solve() throws IOException {
			Queue<int[]> heap = new PriorityQueue<>(Comparator.comparingInt(o -> o[0]));
			int[] a = door.get(0);
			heap.add(new int[] {0, a[0], a[1]}); // 거울 개수, x, y

			while (heap.size() > 0) {
				int[] poll = heap.poll();
				int cost = poll[0];
				int x = poll[1];
				int y = poll[2];
			}

		}

		public static void dfs(int x, int y, int dir, boolean cross, int count) {

			if (x == door.get(1)[0] && y == door.get(1)[1]) {
				answer = min(answer, count);
				return;
			}

			if (!cross) {
				// 3, 4
				int nx = x + notCrossX[dir];
				int ny = y + notCrossX[dir];
				while (0 <= nx && nx < n && 0 <= ny && ny < n && map[ny][nx] == '.') {
					nx = x + notCrossX[dir];
					ny = y + notCrossX[dir];
				}
				if (0 <= nx && nx < n && 0 <= ny && ny < n && map[ny][nx] != '*') {
					if (map[ny][nx] == '!') {
						for (int i = 2; i < 4; i++) {
							map[ny][nx] = mirrors[i];
							dfs(nx, ny, (dir + 3) % 4, cross, count + 1);
						}
						map[ny][nx] = '!';
					} else if (map[ny][nx] == '\\' || map[ny][nx] == '/') {
						dfs(nx, ny, (dir + 3) % 4, cross, count);
					}
				}
			} else {
				// 1, 2
				int nx = x + crossX[dir];
				int ny = y + crossX[dir];
				while (0 <= nx && nx < n && 0 <= ny && ny < n && map[ny][nx] == '.') {
					nx = x + crossX[dir];
					ny = y + crossX[dir];
				}
				if (0 <= nx && nx < n && 0 <= ny && ny < n && map[ny][nx] != '*') {

				}

			}
		}
	}
}
