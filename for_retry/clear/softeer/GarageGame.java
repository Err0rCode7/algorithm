package softeer;

import java.util.*;
import java.io.*;


public class GarageGame
{
	private static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
	private static int n;
	private static int[][] board;
	private static int[] dx;
	private static int[] dy;

	private static int answer;
	public static void main(String args[]) throws Exception
	{
		n = Integer.parseInt(in.readLine());
		board = new int[3 * n][n];

		for (int i = 0; i < 3 * n; ++i) {
			StringTokenizer st = new StringTokenizer(in.readLine());

			for(int j = 0; j < n; ++j) {
				board[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		dx = new int[]{1, 0, -1, 0};
		dy = new int[]{0, 1, 0, -1};

		answer = 0;

		selectTarget(0, 0);

		System.out.println(answer);
	}

	private static void selectTarget(int depth, int sum) {

		if (sum + (3 - depth) * n * n * 2 <= answer) return;

		boolean[][] visited = new boolean[n][n];
		int[][] origin = new int[3*n][n];

		arraycopy(board, origin);
		for (int y = 2 * n; y < 3 * n; ++y) {
			for (int x = 0; x < n; ++x) {
				int target = origin[y][x];
				if (target == 0 || visited[y - 2 * n][x]) continue;
				arraycopy(origin, board);
				Queue<int[]> que = new LinkedList<>();
				que.add(new int[]{x, y});
				visited[y - 2 * n][x] = true;
				int count = 0;
				int lx = x;
				int rx = x;
				int by = y;
				int ty = y;
				while (!que.isEmpty()) {
					int[] poll = que.poll();
					// System.out.println(Arrays.toString(poll));
					lx = Math.min(lx, poll[0]);
					rx = Math.max(rx, poll[0]);
					by = Math.min(by, poll[1]);
					ty = Math.max(ty, poll[1]);
					board[poll[1]][poll[0]] = 0;
					count++;
					for (int i = 0; i < 4; ++i) {
						int nx = poll[0] + dx[i];
						int ny = poll[1] + dy[i];
						// System.out.println(nx +" " +ny + " " + " " + target);
						if (nx < 0 || ny < 2 * n || nx >= n || ny >= 3 * n) continue;
						if (board[ny][nx] != target || visited[ny - 2 * n][nx]) continue;

						visited[ny - 2 * n][nx] = true;
						que.add(new int[]{nx, ny});
					}
				}

				int nextSum = sum + count + (ty - by + 1) * (rx - lx + 1);
				// System.out.println(ty + " " + by + " " + rx + " " + lx);
				// System.out.println(nextSum + " " + target + " " + ((ty - by + 1) * (rx - lx + 1)));
				if (depth >= 2) {
					answer = Math.max(answer, nextSum);
					continue;
				} else {

					for (int a = lx; a <= rx; ++a) {
						for (int b = ty; b >= by; --b) {
							if (board[b][a] != 0) continue;
							int jump = 0;
							for (int l = b - 1; l >= 0; --l) {
								if (board[l][a] != 0) {
									jump = b - l;
									break;
								}
							}

							if (jump == 0)
								continue;

							for (int l = b; l >= jump; --l) {
								board[l][a] = board[l - jump][a];
								board[l-jump][a] = 0;
							}
						}
					}
					selectTarget(depth + 1, nextSum);
				}


			}
		}
	}

	private static void arraycopy(int[][] src, int[][] dest) {
		for (int y = 0; y < 3 * n; ++y) {
			for (int x = 0; x < n; ++x) {
				dest[y][x] = src[y][x];
			}
		}
	}

}