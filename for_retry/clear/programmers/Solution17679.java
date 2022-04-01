package programmers;

import java.util.*;

public class Solution17679 {
	public int solution(int m, int n, String[] board) {


		char[][] map = new char[m][n];

		for (int i = 0; i < m; i++) {
			char[] chars = board[i].toCharArray();
			map[i] = chars;
		}
		Checker checker = new Checker(m, n, map);
		int answer = 0;
		while (true) {
			int count = checker.checkAndSet();
			if (count == 0)
				break;
			answer += count;
			fallDown(map, m, n);
			System.out.println(answer);
		}
		return answer;
	}

	private void fallDown(char[][] map, int m, int n) {
		for (int x = 0; x < n; x++) {
			int start = -1;
			for (int y = m - 1; y >= 0; y--) {
				if (map[y][x] == 0) {
					start = y;
					break;
				}
			}

			for (int y = start; y >= 0; y--) {
				if (map[y][x] != 0) {
					map[start--][x] = map[y][x];
					map[y][x] = 0;
				}
			}
		}
	}

	private static class Checker {
		int[] dx = {1, 0, -1, 0};
		int[] dy = {0, 1, 0, -1};
		int x;
		int y;
		int m;
		int n;
		char[][] map;

		Checker(int m, int n, char[][] map) {
			this.m = m;
			this.n = n;
			this.map = map;
		}

		public int checkAndSet() {
			int result = 0;
			boolean[][] visited = new boolean[m][n];
			List<int[]> removePos = new ArrayList<>();
			for (int y = 0; y < m - 1; y++) {
				for (int x = 0; x < n - 1; x++) {
					char cur = map[y][x];
					if (cur == 0) continue;
					if (unsafe(x + 1, y) || unsafe(x, y + 1) || unsafe(x + 1, y + 1)) continue;

					if (map[y][x + 1] == cur && map[y + 1][x] == cur && map[y + 1][x + 1] == cur) {
						removePos.add(new int[]{x, y});
					}
				}
			}
			for (int[] pos : removePos) {
				int x = pos[0];
				int y = pos[1];
				if (map[y][x] != 0)
					result += 1;
				if (map[y][x + 1] != 0)
					result += 1;
				if (map[y + 1][x + 1] != 0)
					result += 1;
				if (map[y + 1][x] != 0)
					result += 1;
				map[y][x] = 0;
				map[y + 1][x] = 0;
				map[y][x + 1] = 0;
				map[y + 1][x + 1] = 0;
			}
			// System.out.println(result);
			return result;
		}


		private boolean unsafe(int x, int y) {
			return (x < 0 || y < 0 || x >= n || y >= m);
		}
	}
}