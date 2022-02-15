package boj;

import static java.lang.Integer.*;

import java.io.*;
import java.util.*;

public class Main3108 {
	public static void main(String[] args) throws IOException {
		Solution.solution();
	}

	static class Solution {
		static final BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		static final BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
		static int n, m, k;
		static int[][] map;
		static String target;
		static Queue<int[]> que;
		static int[] dx = new int[] {1, 0, -1, 0};
		static int[] dy = new int[] {0, 1, 0, -1};
		static int[][] rects;
		public static void solution() throws IOException {

			n = parseInt(in.readLine());
			rects = new int[n][4];
			map = new int[2001][2001];
			boolean[][] visited = new boolean[2001][2001];
			for (int i = 0; i < n; i++) {
				StringTokenizer tokenizer = new StringTokenizer(in.readLine());
				for (int j = 0; j < 4; j++) {
					rects[i][j] = (parseInt(tokenizer.nextToken()) + 500) * 2;
				}
				for (int j = rects[i][0]; j <= rects[i][2]; j++) {
					map[rects[i][1]][j] = 1;
					map[rects[i][3]][j] = 1;
				}

				for (int j = rects[i][1]; j <= rects[i][3]; j++) {
					map[j][rects[i][0]] = 1;
					map[j][rects[i][2]] = 1;
				}
			}
			int count = 0;
			for (int i = 0; i < n; i++) {
				int x1 = rects[i][0];
				int y1 = rects[i][1];
				if (visited[y1][x1]) {
					continue;
				}
				dfs(x1, y1, visited);
				count += 1;
			}

			if (map[1000][1000] == 1) count -= 1;

			System.out.println(count);
		}

		public static void dfs(int x, int y, boolean[][] visited) {
			visited[y][x] = true;
			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];
				if (nx >= 0 && nx <= 2000 && ny >= 0 && ny <= 2000 && !visited[ny][nx] && map[ny][nx] == 1) {
					dfs(nx, ny, visited);
				}
			}
		}
	}
}
