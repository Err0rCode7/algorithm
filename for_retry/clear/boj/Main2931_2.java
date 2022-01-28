package boj;
import static java.lang.Integer.*;

import java.io.*;
import java.util.*;

class Main2931_2 {
	public static void main(String[] args) throws IOException {
		Solution.solution();
	}

	static class Solution {
		static int r, c;
		static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		// static BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
		static char[][] map;
		static int[] M = new int[2];
		static int[] Z = new int[2];
		static int[] dx = new int[] {1, 0, -1, 0};
		static int[] dy = new int[] {0, 1, 0, -1};
		static char[] blocks = new char[] {'|', '-', '1', '2', '3', '4', '+'};

		public static void solution() throws IOException {
			StringTokenizer tokenizer = new StringTokenizer(in.readLine());
			r = parseInt(tokenizer.nextToken());
			c = parseInt(tokenizer.nextToken());
			map = new char[r][c];

			for (int i = 0; i < r; i++) {
				String line = in.readLine();
				for (int j = 0; j < c; j++) {
					map[i][j] = line.charAt(j);
					if (map[i][j] == 'M') {
						M[0] = j;
						M[1] = i;
					} else if (map[i][j] == 'Z') {
						Z[0] = j;
						Z[1] = i;
					}
				}
			}

			Queue<int[]> que = new LinkedList<>();
			boolean[][] visited = new boolean[r][c];
			for (int i = 0; i < 4; i++) {
				int x = M[0] + dx[i];
				int y = M[1] + dy[i];

				if (0 > x || x >= c || 0 > y || y >= r)
					continue;

				if (map[y][x] == '.' || map[y][x] == 'Z')
					continue;

				que.add(new int[] {x, y});
				visited[y][x] = true;
				break;
			}

			while (que.size() > 0) {
				int[] poll = que.poll();
				for (int i = 0; i < 4; i++) {
					int nx = poll[0] + dx[i];
					int ny = poll[1] + dy[i];
					if (canGo(poll[0], poll[1], nx, ny) && !visited[ny][nx]) {
						if (map[ny][nx] == '.') {
							for (char block : blocks) {
								map[ny][nx] = block;
								boolean take = true;
								for (int j = 0; j < 4; j++) {
									int tx = nx + dx[j];
									int ty = ny + dy[j];
									if (canGo(nx, ny, tx, ty) != canGo(tx, ty, nx, ny)) {
										take = false;
										break;
									}
								}
								if (take)
									break;
							}
							System.out.println((ny + 1) + " " + (nx + 1) + " " + map[ny][nx]);
							return;
						}
						if (map[ny][nx] != 'Z') {
							visited[ny][nx] = true;
							que.add(new int[] {nx, ny});
						}
					}
				}
			}
			// solve();
			// out.flush();
			// out.close();
			in.close();
		}

		public static boolean canGo(int x, int y, int tx, int ty) {
			if (0 > tx || tx >= c || 0 > ty || ty >= r)
				return false;

			if (0 > x || x >= c || 0 > y || y >= r)
				return false;

			if (map[y][x] == '|') {
				return tx == x && (ty == y + 1 || ty == y - 1);
			} else if (map[y][x] == '-') {
				return ty == y && (tx == x + 1 || tx == x - 1);
			} else if (map[y][x] == '1') {
				return (tx == x && ty == y + 1) || (tx == x + 1 && ty == y);
			} else if (map[y][x] == '2') {
				return (tx == x && ty == y - 1) || (tx == x + 1 && ty == y);
			} else if (map[y][x] == '3') {
				return (tx == x && ty == y - 1) || (tx == x - 1 && ty == y);
			} else if (map[y][x] == '4') {
				return (tx == x && ty == y + 1) || (tx == x - 1 && ty == y);
			} else
				return map[y][x] == '+';
		}
	}
}

