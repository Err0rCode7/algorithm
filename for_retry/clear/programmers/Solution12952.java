package programmers;

import java.util.*;

public class Solution12952 {
	private int[][] map;
	private int answer = 0;
	private int n;
	public int solution(int n) {
		this.n = n;
		this.map = new int[n][n];
		dfs(0);
		return answer;
	}

	private void dfs(int cur) {
		if (cur == n) {
			answer++;
			// for (int i = 0; i < n; i++)
			//     System.out.println(Arrays.toString(map[i]));
			// System.out.println();
			return ;
		}
		for (int i = 0; i < n; i++) {

			if (check(cur, i) == false) continue;
			map[i][cur] = 1;
			dfs(cur + 1);
			map[i][cur] = 0;
		}
	}

	private boolean check(int x, int y) {
		// System.out.println(x + " " + y);
		int y1 = y - 1;
		int y2 = y + 1;
		x--;

		for (; x >= 0; x--) {

			if (map[y][x] == 1 || (y1 >= 0 && map[y1][x] == 1) || (y2 < n && map[y2][x] == 1))
				return false;

			y1--;
			y2++;
		}
		return true;
	}
}