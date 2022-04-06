package programmers;

import java.util.*;

public class Solution87694 {
	private int MAX_SIZE = 51;
	private List<Rectangcle> rts = new ArrayList<>();
	private int[] dx = {1, 0, -1, 0};
	private int[] dy = {0, 1, 0, -1};
	private int answer = 0;
	private char[][] map = new char[MAX_SIZE * 2][MAX_SIZE * 2];
	public int solution(int[][] rectangle, int characterX, int characterY, int itemX, int itemY) {


		for (int[] rec: rectangle) {
			int lx = rec[0] * 2;
			int ly = rec[1] * 2;
			int rx = rec[2] * 2;
			int ry = rec[3] * 2;
			Rectangcle rectangcle = new Rectangcle(lx, ly, rx, ry);
			rts.add(rectangcle);

			for (int x = lx; x <= rx; ++x) {
				for (int y = ly; y <= ry; ++y) {
					map[y][x] = '1';
				}
			}
		}

		characterX *= 2;
		characterY *= 2;
		itemX *= 2;
		itemY *= 2;

		bfs(characterX, characterY, itemX, itemY);

		return answer;
	}

	private void bfs(int x, int y, int tx, int ty) {
		Queue<int[]> que = new LinkedList<>();
		que.add(new int[]{x, y});

		boolean[][] visited = new boolean[MAX_SIZE * 2][MAX_SIZE * 2];
		visited[y][x] = true;

		int depth = 0;
		while (!que.isEmpty()) {
			int size = que.size();
			for (int i = 0; i < size; i++) {
				int[] pos = que.poll();
				// System.out.println(Arrays.toString(pos) + " " + map[pos[1]][pos[0]]);
				if (pos[0] == tx && pos[1] == ty) {
					answer = depth / 2;
					return;
				}

				for (int k = 0; k < 4; k++) {
					int nx = pos[0] + dx[k];
					int ny = pos[1] + dy[k];
					// System.out.println(nx + " " + ny);
					if (nx < 0 || ny < 0 || nx >= MAX_SIZE * 2 || ny >= MAX_SIZE * 2) continue;
					// System.out.println(isInMiddle(nx, ny));
					if (pos[0] == 4 && pos[1] == 8) {
						// System.out.println(nx + " " + ny);
						// System.out.println(map[ny][nx] + " " + " " + visited[ny][nx] +isInMiddle(nx, ny));
					}
					if (map[ny][nx] != '1' || visited[ny][nx] || isInMiddle(nx, ny)) continue;
					// System.out.println(nx + " " + ny);
					visited[ny][nx] = true;
					que.add(new int[]{nx, ny});
				}
			}
			depth++;
		}
	}

	private boolean isInMiddle(int x, int y) {
		for (Rectangcle rec : rts) {
			if (rec.isIn(x, y)) {
				// System.out.println(rec.lx + " " + rec.rx + " " + rec.ly + " " + rec.ry);
				return true;
			}
		}
		return false;
	}

	static class Rectangcle {
		int lx;
		int ly;
		int rx;
		int ry;

		Rectangcle(int lx, int ly, int rx, int ry) {
			this.lx = lx;
			this.ly = ly;
			this.rx = rx;
			this.ry = ry;
		}

		public boolean isIn(int x, int y) {
			return (x < rx && x > lx && y < ry && y > ly);
		}
	}
}