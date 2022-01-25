package boj;

import static java.lang.Integer.*;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main2931 {
	static class Solution {
		static int r, c;
		static char[][] map;
		static boolean[][] visited;
		static int[] m, z, target;
		static int[] dx = new int[] {0, 1, 0, -1, -200};
		static int[] dy = new int[] {1, 0, -1, 0, -200};
		static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		public static void solution() throws IOException {
			StringTokenizer tokenizer = new StringTokenizer(in.readLine());
			r = parseInt(tokenizer.nextToken());
			c = parseInt(tokenizer.nextToken());
			map = new char[r][c];
			m = new int[2];
			z = new int[2];
			for (int i = 0; i < r; i++) {
				tokenizer = new StringTokenizer(in.readLine());
				String token = tokenizer.nextToken();
				for (int j = 0; j < c; j++) {
					map[i][j] = token.charAt(j);
					if (map[i][j] == 'M') {
						m[0] = j;
						m[1] = i;
					} else if (map[i][j] == 'Z') {
						z[0] = j;
						z[1] = i;
					}
				}
			}

		}

		public boolean dfs(int x, int y, int dir, boolean used) {
			if (x == z[0] && y == z[1])
				return true;
			visited[y][x] = true;
			int[] nxy = getNxy(x, y, dir);
			if (0 <= nxy[0] && nxy[0] < c && 0 <= nxy[1] && nxy[1] < r
				&& (!visited[nxy[1]][nxy[0]] || map[nxy[1]][nxy[0]] == '+')) {

				if (dfs(nxy[0], nxy[1], nxy[2], used))
					return true;
			}
			visited[y][x] = false;
			return false;
		}

		private boolean canGo(int nx, int ny, int dir) {
			if (dir == 0 && (map[ny][nx] == '|' || map[ny][nx] == '+' || map[ny][nx] == '2' || map[ny][nx] == '3')) {
				return true;
			} else if (dir == 1 && (map[ny][nx] == '2' || map[ny][nx] == '1' || map[ny][nx] == '+' || map[ny][nx] == '-')) {
				return true;
			} else if (dir == 2 && (map[ny][nx] == '|' || map[ny][nx] == '+' || map[ny][nx] == '1' || map[ny][nx] == '4')) {
				return true;
			} else if (dir == 3 && (map[ny][nx] == '-' || map[ny][nx] == '+' || map[ny][nx] == '3' || map[ny][nx] == '4')) {
				return true;
			}
			return false;
		}

		private int[] getNxy(int x, int y, int dir) {
			int[] next = new int[3];
			if(map[y][x] == '1') {
				if (dir == 2)
					dir = 1;
				else if (dir == 3)
					dir = 4;
				else
					dir = 5;
			} else if(map[y][x] == '2') {
				if (dir == 2)
					dir = 3;
				else if (dir == 1)
					dir = 4;
				else
					dir = 5;
			} else if(map[y][x] == '3') {
				if (dir == 4)
					dir = 3;
				else if (dir == 1)
					dir = 2;
				else
					dir = 5;
			} else if(map[y][x] == '4') {
				if (dir == 4)
					dir = 1;
				else if (dir == 3)
					dir = 2;
				else
					dir = 5;
			}
			next[0] = x + dx[dir];
			next[1] = y + dy[dir];
			next[2] = dir;
			return next;
		}
	}
}
