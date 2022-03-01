package programmers;

public class Solution42898 {
	public int solution(int m, int n, int[][] puddles) {
		int[][] map = new int[n][m];

		for (int[] puddle : puddles) {
			map[puddle[1] - 1][puddle[0] - 1] = -1;
		}

		int[][] d = new int[][] {{-1, 0}, {0, -1}};
		map[0][0] = 1;
		for (int y = 0; y < n; y++) {
			for (int x = 0; x < m; x++) {
				if (map[y][x] == -1)
					continue;
				for (int k = 0; k < d.length; k++) {
					int dx = d[k][0];
					int dy = d[k][1];
					if (x + dx < 0 || x + dx >= m || y + dy < 0 || y + dy >=n || map[y + dy][x + dx] == -1)
						continue;
					map[y][x] += map[y + dy][x + dx];
					map[y][x] %= 1_000_000_007;
				}
			}
		}

		return map[n - 1][m - 1];
	}
}