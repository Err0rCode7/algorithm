package programmers;

import java.util.ArrayList;
import java.util.List;

public class Solution86052 {
	private int n, m;
	private int[] dx = {1, 0, -1, 0};
	private int[] dy = {0, 1, 0, -1};
	private String[] grid;
	public int[] solution(String[] grid) {
		n = grid.length;
		m = grid[0].length();
		this.grid = grid;
		boolean[][][] visited = new boolean[n][m][4];

		List<Integer> results = new ArrayList<>();
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				for (int k = 0; k < 4; k++) {
					if (!visited[i][j][k]) {
						// results.add(dfs(j, i, k, visited));
						results.add(searchGraph(j, i, k, visited));
					}
				}
			}
		}
		return results.stream().sorted().mapToInt(Integer::intValue).toArray();
	}

	public int searchGraph(int x, int y, int dir, boolean[][][] visited) {
		int result = 0;
		int nx, ny;
		while (true) {
			char c = grid[y].charAt(x);

			if (c == 'L') {
				dir = dir - 1;
				if (dir < 0)
					dir = 3;
			} else if (c == 'R') {
				dir = (dir + 1) % 4;
			}
			nx = x + dx[dir];
			ny = y + dy[dir];

			if (nx < 0)
				nx = m - 1;
			if (ny < 0)
				ny = n - 1;
			if (nx >= m)
				nx = 0;
			if (ny >= n)
				ny = 0;

			if (visited[ny][nx][dir])
				break;
			x = nx;
			y = ny;
			result += 1;
			visited[ny][nx][dir] = true;
		}
		return result;
	}

	public int dfs(int x, int y, int dir, boolean[][][] visited) {
		int nx, ny;
		char c = grid[y].charAt(x);

		if (c == 'L') {
			dir = dir - 1;
			if (dir < 0)
				dir = 3;
		} else if (c == 'R') {
			dir = (dir + 1) % 4;
		}
		nx = x + dx[dir];
		ny = y + dy[dir];

		if (nx < 0)
			nx = m - 1;
		if (ny < 0)
			ny = n - 1;
		if (nx >= m)
			nx = 0;
		if (ny >= n)
			ny = 0;

		int result = 0;
		if (!visited[ny][nx][dir]) {
			visited[ny][nx][dir] = true;
			result = dfs(nx, ny, dir, visited) + 1;
		}
		return result;
	}
}
